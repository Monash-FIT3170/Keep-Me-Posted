<script>
    import { reset_password} from '../../api-functions/reset_password';
    import { backendURL } from "../../api-functions/base-URL";
    import { ResetPasswordStore } from "../../stores/reset-password-store"
    import { goto } from "$app/navigation";
    
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

        let response = await reset_password($ResetPasswordStore.email, password1, backendURL);
        
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

<div>
    <h3>Enter your new password</h3>
    <input type="password" placeholder="••••••••" bind:value={ password1 }/>
    <h3>Re-enter your new password</h3>
    <input type="password" placeholder="••••••••" bind:value={ password2 }/>

    <button on:click={() => resetPassword()}>Reset password</button>
    {#if errorMessage}
        <h3>{errorMessage}</h3>
    {/if}
</div>