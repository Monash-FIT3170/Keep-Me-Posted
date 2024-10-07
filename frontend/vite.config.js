import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig, loadEnv } from 'vite';

const requiredEnvVars = ['VITE_SECRET_CLIENT_ID', 'VITE_SECRET_CLIENT_SECRET'];

export default defineConfig(({ mode }) => {
	const env = loadEnv(mode, process.cwd());

    requiredEnvVars.forEach((varName) => {
        const envValue = env[varName];
    
        // check if environment variable is missing
        if (!envValue) {
            console.error(`Missing required frontend environment variable: ${varName}`)
        }
    
        if (envValue === "REPLACE_WITH_API_KEY") {
            console.error(`Environment variable ${varName} is still set to "REPLACE_WITH_API_KEY"`);
        }
    });

    return {
        plugins: [sveltekit()],
        server: {
            fs: {
                allow: ['/src/']
            }
        },
    };
});
