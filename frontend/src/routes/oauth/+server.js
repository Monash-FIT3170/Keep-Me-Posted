import { redirect } from '@sveltejs/kit';
import { OAuth2Client } from 'google-auth-library';
import { SECRET_CLIENT_ID, SECRET_CLIENT_SECRET } from '$env/static/private';
import { frontendURL } from '../../api-functions/base-URL';

// Function to fetch user data from Google
async function getUserData(access_token) {
  const response = await fetch(`https://www.googleapis.com/oauth2/v3/userinfo?access_token=${access_token}`);
  const data = await response.json();
  console.log('User data received:', data); // Check data received
  
  return data.email; // Return the email for further use
}

// Function to fetch contacts from Google People API
async function getContacts(access_token) {
  const response = await fetch('https://people.googleapis.com/v1/people/me/connections?personFields=emailAddresses', {
    headers: {
      Authorization: `Bearer ${access_token}`,
    },
  });
  const data = await response.json();
  console.log('Contacts data received:', data); // Check contacts data received
  
  // Extract email addresses from contacts
  const contacts = data.connections || [];
  const emailAddresses = contacts
    .flatMap(contact => contact.emailAddresses || [])
    .map(emailObj => emailObj.value);

  return emailAddresses; // Return array of email addresses
}

export const GET = async ({ url, cookies }) => {
  const redirectURL = `${frontendURL}oauth`; // Use the dynamic frontend URL
  const code = await url.searchParams.get('code');

  console.log('Returned code:', code);

  try {
    const oAuth2Client = new OAuth2Client(
      SECRET_CLIENT_ID,
      SECRET_CLIENT_SECRET,
      redirectURL
    );
    
    const r = await oAuth2Client.getToken(code);
    oAuth2Client.setCredentials(r.tokens);
    console.info('Tokens acquired.');
    const user = oAuth2Client.credentials;
    console.log('Credentials:', user);

    const userEmail = await getUserData(user.access_token);

    // Fetch contacts
    const contacts = await getContacts(user.access_token);

    // Store email, access token, and contacts in cookies
    cookies.set('userEmail', userEmail, {
      path: '/',
      httpOnly: true, // Optional: to prevent JavaScript access (better security)
      maxAge: 60 * 60 * 24 * 7, // 1 week expiration
    });

    cookies.set('accessToken', user.access_token, {
      path: '/',
      httpOnly: true, // Optional: to prevent JavaScript access
      maxAge: 60 * 60 * 24 * 7, // 1 week expiration
    });

    cookies.set('mailingList', JSON.stringify(contacts), {
      path: '/',
      httpOnly: true, // Optional: to prevent JavaScript access
      maxAge: 60 * 60 * 24 * 7, // 1 week expiration
    });

    console.log('User email, access token, and contacts stored in cookies:', userEmail, contacts);

  } catch (err) {
    console.error('Error logging in with OAuth2 user:', err);
  }
  
  throw redirect(303, `${frontendURL}upload_audio?google_auth=true`); // Redirect to another page with query parameter
};
