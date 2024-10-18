import { defineConfig } from "cypress";

export default defineConfig({
  projectId: '2ciyzj',
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    baseUrl: 'http://localhost:5173',
    supportFile: false, // else need a separate file
  },
  retries: {
    runMode: 3,
    openMode: 1,
  },
});
