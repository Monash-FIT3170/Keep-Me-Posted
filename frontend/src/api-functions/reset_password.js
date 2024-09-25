
export let reset_password = async (email, baseURL) => {
    const postRequestString = baseURL + "/send_password_reset" 

    const verficationCode = Math.floor(100000 + Math.random() * 900000)

    const response = await fetch(postRequestString, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            email: email,
            subject: "KMP Password Reset",
            contacts: [email],
            message: "You're one time code is " + verficationCode
        }),
    });

    return response;
}