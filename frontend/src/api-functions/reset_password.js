import { ResetPasswordStore } from "../stores/reset-password-store"

export let reset_password = async (uid, token, password, baseURL) => {
    const postRequestString = baseURL + "/reset_password" 

    let data = new FormData()
    data.append('uid', uid)
    data.append('token', token)
    data.append('password', password)

    const response = await fetch(postRequestString, {
        method: "POST",
        body: data
    });

    return response
}