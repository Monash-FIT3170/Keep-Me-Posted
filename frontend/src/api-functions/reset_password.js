
export let reset_password = async (email, baseURL) => {
    const postRequestString = baseURL + "/password_reset" 

    const response = await fetch(postRequestString, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            email: email,
        }),
    });

    const jsonResponse = await response.json();

    return jsonResponse;
}