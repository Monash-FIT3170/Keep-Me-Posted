import { writable, get } from 'svelte/store';

import { backendURL } from '../api-functions/base-URL';

// Key to retrieve the auth store from sessionStorage
const AUTH_STORAGE_KEY = 'authStore';

// Helper function to load meetings from session storage
function loadFromSessionStorage() {
    if (typeof window !== 'undefined' && window.sessionStorage) {
        const storedMeetings = sessionStorage.getItem('meetings');
        return storedMeetings ? JSON.parse(storedMeetings) : [];
    }
    return [];
}

// Helper function to save meetings to session storage
function saveToSessionStorage(meetings) {
    if (typeof window !== 'undefined' && window.sessionStorage) {
        sessionStorage.setItem('meetings', JSON.stringify(meetings));
    }
}

// Helper function to get the user email from authStore in session storage
function getUserEmailFromAuthStore() {
    if (typeof window !== 'undefined' && window.sessionStorage) {
        const authStore = sessionStorage.getItem(AUTH_STORAGE_KEY);
        if (authStore) {
            const parsedAuthStore = JSON.parse(authStore);
            return parsedAuthStore.email || null; // Return email if available
        }
    }
    return null; // Return null if no email found
}

// Create a writable store to hold the meetings, initialized from session storage if available
export const meetings = writable(loadFromSessionStorage());

// Subscribe to changes in the store and save to session storage whenever the store is updated
meetings.subscribe((value) => {
    saveToSessionStorage(value);
});

// Function to fetch meetings from the API using email from session storage
export const fetchMeetings = async () => {
    const userEmail = getUserEmailFromAuthStore();
    if (!userEmail) {
        console.log('No user email found in session storage.');
        return;
    }

    try {
        const response = await fetch(`${backendURL}/meetings/${userEmail}/`);
        if (!response.ok) {
            throw new Error('Failed to fetch meetings');
        }
        const data = await response.json();
        meetings.set(data);  // Update the store and session storage with the fetched meetings
    } catch (error) {
        console.error('Error fetching meetings:', error);
    }
};

// Function to add a new meeting
export const addMeeting = (newMeeting) => {
    meetings.update(currentMeetings => {
        const updatedMeetings = [...currentMeetings, newMeeting];
        saveToSessionStorage(updatedMeetings); // Save to session storage
        return updatedMeetings;
    });
};

// Function to update a specific meeting
export const updateMeeting = (updatedMeeting) => {
    meetings.update(currentMeetings => {
        const updatedMeetings = currentMeetings.map(meeting => 
            meeting.id === updatedMeeting.id ? updatedMeeting : meeting
        );
        saveToSessionStorage(updatedMeetings); // Save to session storage
        return updatedMeetings;
    });
};

// Function to delete a meeting
export const deleteMeeting = (meetingId) => {
    meetings.update(currentMeetings => {
        const updatedMeetings = currentMeetings.filter(meeting => meeting.id !== meetingId);
        saveToSessionStorage(updatedMeetings); // Save to session storage
        return updatedMeetings;
    });
};

// Helper function to get meetings from the store itself
export function getMeetingsFromStore() {
    return get(meetings); // Retrieve the current meetings from the store
}




// import { getMeetingsFromStore } from '../../stores/past-meetings-store';

//     // Get the current meetings from the store
// let currentMeetings = getMeetingsFromStore();

// console.log('Current meetings:', currentMeetings);
