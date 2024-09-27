<script>
    import { request_reset_password} from '../../api-functions/request_reset_password';
    import { backendURL } from "../../api-functions/base-URL";
    import { goto } from "$app/navigation";
    import { ResetPasswordStore } from "../../stores/reset-password-store"

    let message = ""
    let codeSent = false
    let code =  ""

    let requestPasswordReset = async () => {
        let response = await request_reset_password($ResetPasswordStore.email, backendURL);
        
        if (response.status === 200) {
            codeSent = true
            message = "A code has been sent to your email"
        } else {
            message = "There is no account matching that email"
        }
    }

    let checkCode = () => {
        if (code === atob($ResetPasswordStore.code)) {
            goto("/reset_password")
        } else {
            message = "The code provided is not correct. Please try again."
        }
    }
    
</script>

<!-- TODO
Make this look pretty
Make sure the enter email text box binds to the store - bind:value={ $ResetPasswordStore.email}
Make sure the reset password button binds to the function - on:click={() => requestPasswordReset()}
Make sure that the different boxes are rendered based on if the code has been sent - codeSent
Make sure that the code is binded to the variable - bind:value={ code }
-->

<div>
    {#if !codeSent}
    <h3>Enter your email</h3>
    <input type="email" bind:value={ $ResetPasswordStore.email}/>
    <button on:click={() => requestPasswordReset()}>Request Reset</button>
    {:else} 
    <h3>Enter the validation code sent to your email</h3>
    <input bind:value={ code }/>
    <button on:click={() => checkCode()}>Reset password</button>
    {/if}
    {#if message}
        <h3>{message}</h3>
    {/if}
</div>
