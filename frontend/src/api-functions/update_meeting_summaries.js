// send email api function. 
// message: String, subject: String, Contacts: [String]
import { emailStatusStore } from "../stores/email-status-store"


export let update_meeting_summary = async (user_email, meeting_subject, meeting_transcript, meeting_summary, meeting_recipients, meeting_date, baseURL) => {
    const postRequestString = baseURL + "/meetings/" 

    let data = new FormData()
    data.append('user_email', user_email)
    data.append('meeting_subject', meeting_subject)
    data.append('meeting_transcript', meeting_transcript)
    data.append('meeting_summary', meeting_summary)
    data.append('meeting_recipients', JSON.stringify(meeting_recipients))
    data.append('meeting_date', meeting_date)

    try {
        const response = await fetch(postRequestString, { method: "POST", body: data})

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

        const jsonResponse = await response.json()

        console.log("meeting summary updated")

        return jsonResponse.details;
    } catch (error) {
        console.error("Error:", error)

        // Update the error store with the associated error message
        errorStore.set({
            message: error.message
        });
        return null
    }
}
