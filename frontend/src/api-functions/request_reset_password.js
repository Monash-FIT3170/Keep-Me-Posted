import { ResetPasswordStore } from "../stores/reset-password-store"

export let request_reset_password = async (email, baseURL) => {
    const postRequestString = baseURL + "/send_password_reset" 

    const verficationCode = Math.floor(100000 + Math.random() * 900000).toString()
    const message = "Hello, \n\nA password reset has been requested for your Keep Me Posted account. You're one time verification code is: \n\n**" + verficationCode + "**\n\nPlease ignore this message if you did not request a reset." 

    ResetPasswordStore.set({email: email, code: btoa(verficationCode)})

    let data = new FormData()
    data.append('message', message)
    data.append('subject', "KMP Password Reset")
    data.append('contacts', [email])
    data.append('email', email)

    const response = await fetch(postRequestString, {
        method: "POST",
        body: data
    });

    return response;
}