import { writable } from 'svelte/store';

// Define the key for session storage
const STORAGE_KEY = 'authStore';

// Function to get the initial state from session storage or use default
function getInitialState() {
  if (typeof window !== 'undefined' && window.sessionStorage) {
    const storedState = sessionStorage.getItem(STORAGE_KEY);
    return storedState ? JSON.parse(storedState) : {
      email: "",
      loggedIn: false,
      accessToken: "", // Add accessToken to the initial state
      mailing_list: [] // Add mailing_list to the initial state
    };
  }
  // Fallback state for non-browser environments
  return {
    email: "",
    loggedIn: false,
    accessToken: "", // Add accessToken to the initial state
    mailing_list: [] // Add mailing_list to the initial state
  };
}

// Create a writable store with initial state
const initialState = getInitialState();
export const authStore = writable(initialState);

// Subscribe to store changes and save to session storage
if (typeof window !== 'undefined' && window.sessionStorage) {
  authStore.subscribe(value => {
    sessionStorage.setItem(STORAGE_KEY, JSON.stringify(value));
  });
}

// Function to update the authStore
export function updateAuth(email, loggedIn, accessToken = "", mailing_list = []) {
  authStore.update(state => ({
    ...state,
    email,
    loggedIn,
    accessToken, // Update the accessToken in the store
    mailing_list // Update the mailing_list in the store
  }));
}

// Function to get the current authStore value
export function getAuth() {
  let currentValue;

  // Subscribe to the store to get the current value
  const unsubscribe = authStore.subscribe(value => {
    currentValue = value;
  });

  // Immediately unsubscribe after getting the value
  unsubscribe();

  return currentValue;
}

// Function to clear the session storage and reset the store
export function clearAuth() {
  sessionStorage.removeItem(STORAGE_KEY);
  
  authStore.set({
    email: "",
    loggedIn: false,
    accessToken: "", // Clear accessToken as well
    mailing_list: [] // Clear mailing_list as well
  });
}
