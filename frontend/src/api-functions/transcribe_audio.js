// transcribe audio api function. 
// audioFile: .mp3 or .wav file, baseURL = String
// output: String

import { transcriptStore } from "../stores/transcript-store";

export let transcribe_audio = async (audioFile, baseURL) => {
    const postRequestString = baseURL + "/api/transcribe"; 

    const formData = new FormData();
    formData.append('audio_file', audioFile);

    try {
        const response = await fetch(postRequestString, { method: "POST", body: formData });

        // Check if error occurred
        if (!response.ok) {
            // Retrieve error
            const errorResponse = await response.json();
            
            // Update the error store with the associated error message
            errorStore.set({
                message: errorResponse.message
            });
            return null;
        };

        const jsonResponse = await response.json();
        transcriptStore.set({
            transcript: jsonResponse.transcription,
            transcriptWithSpeakers: jsonResponse.transcription_with_speakers
        });

        return jsonResponse.transcription; 

    } catch (error) {
        console.error("Error:", error);
        
        // Update the error store with the associated error message
        errorStore.set({
            message: error.message
        });
        return null; 
    }
}
