import { ResetPasswordStore } from "../stores/reset-password-store"

export let reset_password = async (email, password, baseURL) => {
    const postRequestString = baseURL + "/reset_password" 

    let data = new FormData()
    data.append('email', email)
    data.append('password', password)

    const response = await fetch(postRequestString, {
        method: "POST",
        body: data
    });

    return response
}