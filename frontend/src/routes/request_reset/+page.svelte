<script>
    import { request_reset_password} from '../../api-functions/request_reset_password';
    import { backendURL } from "../../api-functions/base-URL";

    let message = ""
    let email = ""

    let requestPasswordReset = async () => {
        await request_reset_password(email, backendURL)
        message = "If you have an existing account, a reset link will be sent to you."
    }
    
</script>


<div class="flex flex-col">
    <div>Enter your email</div>
    <input type="email" bind:value={ email }/>
    <button on:click={() => requestPasswordReset()}>Request Reset</button>
    
    {#if message}
        <div>{message}</div>
    {/if}
</div>
