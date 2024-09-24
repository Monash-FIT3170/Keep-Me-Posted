
export let reset_password_confirm = async (uid, token, new_password1, new_password2, baseURL) => {

    const postRequestString = baseURL + "/password_reset_confirm/" 

    const response = await fetch(postRequestString, {
        method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                uid: uid,
                token: token,
                new_password1: new_password1,
                new_password2: new_password2,
            }),
        });

    const jsonResponse = await response.json();

    return jsonResponse;
}