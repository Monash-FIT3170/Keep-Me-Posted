// send email api function. 
// message: String, subject: String, Contacts: [String]
import { emailStatusStore } from "../stores/email-status-store"
import { getAuth } from "../stores/auth-store"  // Import getAuth to retrieve user's email

export let send_email = async (transcript, message, subject, contacts, baseURL) => {
    const postRequestString = baseURL + "/api/sendemail" 

    let data = new FormData()
    data.append('message', message)
    data.append('subject', subject)
    data.append('contacts', contacts)
    
    // Get the logged-in user's email or default to "Guest" if not logged in
    let userEmail = getAuth().email || "Guest";  // Add user's email to form data
    data.append('userEmail', userEmail);  // Pass the user's email along with the request

    if (transcript) {
        data.append('transcript', transcript);
    }

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

        console.log("email sent")
        emailStatusStore.set("Sent")

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
