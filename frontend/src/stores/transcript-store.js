import { writable } from 'svelte/store';

export const transcriptStore = writable({
    transcript: "",
    transcriptWithSpeakers: ""
});

export const sendWithTranscriptStore = writable(true);
