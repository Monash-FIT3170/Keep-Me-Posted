<script>
    import { reset_password } from '../../api-functions/reset_password';
    import { backendURL } from "../../api-functions/base-URL";
    import { goto } from "$app/navigation";
    import { ResetPasswordStore } from "../../stores/reset-password-store"

    let message = ""

    let requestPasswordReset = async () => {
        let response = await reset_password($ResetPasswordStore.email, backendURL);
        
        if (response.status === 200) {
            goto("/reset_password")
        } else {
            message = "There is no account matching that email"
        }
    }
    
</script>

<div>
    <h3>Enter your email</h3>
    <input type="email" bind:value={ $ResetPasswordStore.email}/>
    <button on:click={() => requestPasswordReset()}>Reset password</button>
    {#if message}
        <h3>message</h3>
    {/if}
</div>
