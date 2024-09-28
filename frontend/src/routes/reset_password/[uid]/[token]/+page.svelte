<script>
    import { reset_password} from '../../../../api-functions/reset_password';
    import { backendURL } from "../../../../api-functions/base-URL";
    import { goto } from "$app/navigation";
    import { page } from '$app/stores';

    $: uid = $page.params.uid;
    $: token = $page.params.token;
    
    let password1 = ""
    let password2 = ""
    let errorMessage = ""

    let resetPassword = async () => {
        const passwordRegex = /^(?=.*[A-Z])(?=.*[!@#$%^&*()_+,\-.;:'"<>=?\/\[\]{}|`~])(?=.{8,})[a-zA-Z0-9!@#$%^&*()_+,\-.;:'"<>=?\/\[\]{}|`~]*$/;

        if (!passwordRegex.test(password1)) {
            errorMessage = "Password must contain at least 8 characters, capital letters, and a special character";
            return
        }

        if (password1 !== password2) {
            errorMessage = "Passwords do not match"
            return
        }

        let response = await reset_password(uid, token, password1, backendURL);
        
        if (response.status === 200) {
            errorMessage = "Password successfully reset"
            setTimeout(() => {
                goto("/login")
            }, 1500)
        } else {
            errorMessage = "Password reset failed"
        }
    }

</script>

<!--
TODO:
Make this pretty :)
-->

<div class="flex flex-col">
    <div>Enter your new password</div>
    <input type="password" placeholder="••••••••" bind:value={ password1 }/>
    <div>Re-enter your new password</div>
    <input type="password" placeholder="••••••••" bind:value={ password2 }/>

    <button on:click={() => resetPassword()}>Reset password</button>
    {#if errorMessage}
        <div>{errorMessage}</div>
    {/if}
</div>