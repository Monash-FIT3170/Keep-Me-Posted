import { Readable } from 'stream';

export async function GET({ request }) {
  const cookies = request.headers.get('cookie') || '';
  console.log('Received cookies:', cookies);

  // Function to find and decode a cookie by name
  function getCookieValue(cookieName) {
    const cookie = cookies.split('; ').find(row => row.startsWith(`${cookieName}=`));
    const encodedValue = cookie ? cookie.split('=')[1] : null;
    return encodedValue ? decodeURIComponent(encodedValue) : null;
  }

  // Get and decode the userEmail, accessToken, and mailingList cookies
  const userEmail = getCookieValue('userEmail');
  const accessToken = getCookieValue('accessToken');
  const mailingList = getCookieValue('mailingList'); // Handle mailingList cookie

  console.log('Decoded user email:', userEmail);
  console.log('Decoded access token:', accessToken);
  console.log('Decoded mailing list:', mailingList);

  // Create a readable stream
  const readable = new Readable({
    read() {
      // Push the user email, access token, and mailing list as a JSON object
      this.push(JSON.stringify({
        userEmail,
        accessToken,
        mailingList: mailingList ? JSON.parse(mailingList) : [] // Parse mailingList if it exists
      }));
      this.push(null); // Signal the end of the stream
    }
  });

  return new Response(readable, {
    headers: { 'Content-Type': 'application/json' }
  });
}
