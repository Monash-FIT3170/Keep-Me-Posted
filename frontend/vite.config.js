import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig, loadEnv } from 'vite';

const requiredEnvVars = ['VITE_SECRET_CLIENT_ID', 'VITE_SECRET_CLIENT_SECRET'];

requiredEnvVars.forEach((varName) => {
    const envValue = import.meta.env[varName];
    console.log(envValue);

    // check if environment variable is missing
    if (!envValue || envValue === undefined) {
        console.error('Missing required frontend environment variable: ${varName}')
    }

    if (envValue === "REPLACE_WITH_API_KEY") {
        console.error('Environment variable ${varName} is still set to "REPLACE_WITH_API_KEY"');
    }
});

export default defineConfig(({ mode }) => {
	const env = loadEnv(mode, process.cwd());
    return {
        plugins: [sveltekit()],
        server: {
            fs: {
                allow: ['/src/']
            }
        },
    };
});
