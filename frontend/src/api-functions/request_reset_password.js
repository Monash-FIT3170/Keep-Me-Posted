import { ResetPasswordStore } from "../stores/reset-password-store"

export let request_reset_password = async (email, baseURL) => {
    const postRequestString = baseURL + "/send_password_reset" 

    let data = new FormData()
    data.append('email', email)

    const response = await fetch(postRequestString, {
        method: "POST",
        body: data
    });

    return response;
}