
export let request_reset_password = async (email, baseURL, frontendURL) => {
    const postRequestString = baseURL + "/send_password_reset" 

    let data = new FormData()
    data.append('email', email)
    data.append('frontendURL', frontendURL)

    const response = await fetch(postRequestString, {
        method: "POST",
        body: data
    });

    return response;
}