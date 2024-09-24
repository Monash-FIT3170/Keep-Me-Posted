<script>
    import reset_password from '../../api-functions/reset_password';
    import { backendURL } from "../../api-functions/base-URL";


    let email = "";
    let message;

    let requestPasswordReset = async () => {
        let response = await reset_password(email, backendURL);
        message = "A password reset link will be sent to your email if you have an account."
    }
    
</script>

<div>
    <h1>Request Password Reset</h1>
    <form on:submit|preventDefault={requestPasswordReset}>
        <label for="email">Enter your email:</label>
        <input type="email" bind:value={email} required />

        <button type="submit">Reset Password</button>
    </form>

    {#if message}
        <p>{message}</p>
    {/if}
</div>
