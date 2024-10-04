// send summary api function.
// transcript: String, baseURL = String
// output: String
import { summaryStore } from "../stores/summary-store";
import { errorStore } from "../stores/error-store";

export let send_summary = async (transcript, baseURL) => {
    const postRequestString = baseURL + "/api/summariser"; 
    let data = new FormData()
    transcript = transcript
    data.append('transcript', transcript);

    try {
        const response = await fetch(postRequestString, { method: "POST", body: data });

        // Check if error occurred
        if (!response.ok) {
            console.log(response.status);
            // Retrieve error
            const errorResponse = await response.json();

            console.log(errorResponse.message);
            
            // Update the error store with the associated error message
            errorStore.set({
                message: errorResponse.message
            });
            return null;
        };

        const jsonResponse = await response.json();

        summaryStore.set({
            summary: jsonResponse.summary,
            subject: jsonResponse.title
        })

        return jsonResponse.summary, jsonResponse.title; 

    } catch (error) {
        console.error("Error:", error);
            
        // Update the error store with the associated error message
        errorStore.set({
            message: error.message
        });
        return null; 
    }
}