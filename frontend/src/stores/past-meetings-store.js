// src/stores/meetingsStore.js

import { writable } from 'svelte/store';

// Create a writable store to hold the meetings
export const meetings = writable([]);

// Function to fetch meetings from the API
export const fetchMeetings = async (userEmail) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/meetings/${userEmail}/`);
        if (!response.ok) {
            throw new Error('Failed to fetch meetings');
        }
        const data = await response.json();
        meetings.set(data);  // Update the store with the fetched meetings
    } catch (error) {
        console.error('Error fetching meetings:', error);
    }
};

// Function to add a new meeting
export const addMeeting = (newMeeting) => {
    meetings.update(currentMeetings => {
        return [...currentMeetings, newMeeting];
    });
};

// Function to update a specific meeting
export const updateMeeting = (updatedMeeting) => {
    meetings.update(currentMeetings => {
        return currentMeetings.map(meeting => 
            meeting.id === updatedMeeting.id ? updatedMeeting : meeting
        );
    });
};

// Function to delete a meeting
export const deleteMeeting = (meetingId) => {
    meetings.update(currentMeetings => {
        return currentMeetings.filter(meeting => meeting.id !== meetingId);
    });
};
