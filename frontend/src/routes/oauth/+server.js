import { redirect } from "@sveltejs/kit";
import { OAuth2Client } from "google-auth-library";
import { SECRET_CLIENT_ID, SECRET_CLIENT_SECRET } from "$env/static/private";
import { frontendURL } from "../../api-functions/base-URL";

// Function to fetch user data from Google
async function getUserData(access_token) {
  const response = await fetch(
    `https://www.googleapis.com/oauth2/v3/userinfo?access_token=${access_token}`
  );
  const data = await response.json();
  console.log("User data received:", data); // Check data received
  console.log("DATA USER ---------")

  return data.email; // Return the email for further use
}

async function getContacts(access_token) {
  const response = await fetch(
    "https://gmail.googleapis.com/gmail/v1/users/me/messages?q=label:sent&maxResults=25",
    {
      headers: {
        Authorization: `Bearer ${access_token}`,
      },
    }
  );
  const data = await response.json();
  const messages = data.messages || [];

  console.log("data contacts", data);

  // Extract recipients' email addresses from each message
  const emailAddresses = [];

  for (const message of messages) {
    const messageResponse = await fetch(`https://gmail.googleapis.com/gmail/v1/users/me/messages/${message.id}?format=metadata&metadataHeaders=To&metadataHeaders=Cc&metadataHeaders=Bcc`, {
      headers: {
        Authorization: `Bearer ${access_token}`,
      },
    });
    const messageData = await messageResponse.json();
    const headers = messageData.payload.headers || [];

    // Get all email addresses from the To, Cc, and Bcc fields
    const recipients = headers
      .filter(header => ['To', 'Cc', 'Bcc'].includes(header.name))
      .flatMap(header => header.value.split(',').map(email => email.trim()));

    // Extract only valid email addresses using regex
    const cleanedEmails = recipients.map(recipient => {
      // Use regex to find valid email format
      const emailMatch = recipient.match(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/);
      return emailMatch ? emailMatch[0] : null; // Return the email if valid, otherwise null
    }).filter(email => email !== null); // Remove null entries (invalid emails)

    emailAddresses.push(...cleanedEmails);
  }

  // Return a unique list of email addresses
  return [...new Set(emailAddresses)];
}

export const GET = async ({ url, cookies }) => {
  const redirectURL = `${frontendURL}oauth`; // Use the dynamic frontend URL
  const code = await url.searchParams.get("code");

  console.log("Returned code:", code);

  try {
    const oAuth2Client = new OAuth2Client(
      SECRET_CLIENT_ID,
      SECRET_CLIENT_SECRET,
      redirectURL
    );

    const r = await oAuth2Client.getToken(code);
    oAuth2Client.setCredentials(r.tokens);
    console.info("Tokens acquired.");
    const user = oAuth2Client.credentials;
    console.log("Credentials:", user);

    const userEmail = await getUserData(user.access_token);

    // Fetch contacts
    const contacts = await getContacts(user.access_token);

    // Store email, access token, and contacts in cookies
    cookies.set("userEmail", userEmail, {
      path: "/",
      httpOnly: true, // Optional: to prevent JavaScript access (better security)
      maxAge: 60 * 60 * 24 * 7, // 1 week expiration
    });

    cookies.set("accessToken", user.access_token, {
      path: "/",
      httpOnly: true, // Optional: to prevent JavaScript access
      maxAge: 60 * 60 * 24 * 7, // 1 week expiration
    });

    cookies.set("mailingList", JSON.stringify(contacts), {
      path: "/",
      httpOnly: true, // Optional: to prevent JavaScript access
      maxAge: 60 * 60 * 24 * 7, // 1 week expiration
    });

    console.log(
      "User email, access token, and contacts stored in cookies:",
      userEmail,
      contacts
    );
  } catch (err) {
    console.error("Error logging in with OAuth2 user:", err);
  }

  throw redirect(303, `${frontendURL}upload_audio?google_auth=true`); // Redirect to another page with query parameter
};