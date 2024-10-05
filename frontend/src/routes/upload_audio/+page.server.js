import { redirect } from '@sveltejs/kit';
import { OAuth2Client } from 'google-auth-library';
import { SECRET_CLIENT_ID, SECRET_CLIENT_SECRET } from '$env/static/private';
import { frontendURL } from '../../api-functions/base-URL';

export const actions = {
    OAuth2: async({}) => {
        const redirectURL = `${frontendURL}oauth`; // Use the dynamic frontend URL

        console.log('id', SECRET_CLIENT_ID);

        const oAuth2Client = new OAuth2Client(
            SECRET_CLIENT_ID,
            SECRET_CLIENT_SECRET,
            redirectURL
        );

        // Generate the URL that will be used for the consent dialog.
        const authorizeUrl = oAuth2Client.generateAuthUrl({
            access_type: 'offline',
            scope: [
                'https://www.googleapis.com/auth/userinfo.email', // Access user's email
                'https://www.googleapis.com/auth/drive.readonly', // Access user's Google Drive metadata
                'https://www.googleapis.com/auth/userinfo.profile', // Access user's profile info
                'https://www.googleapis.com/auth/contacts.readonly', // Access user's contacts
                'https://www.googleapis.com/auth/contacts', // Manage user's contacts
                'openid' // OpenID Connect for authentication
            ],
            prompt: 'select_account'
        });

        throw redirect(302, authorizeUrl);
    }
};
