<script>
    import { onMount } from "svelte";
    import { reset_password_confirm } from '../../api-functions/reset_password_confirm';
    import { backendURL } from "../../api-functions/base-URL";

    let uid = "";
    let token = "";
    let newPassword = "";
    let confirmPassword = "";
    let errorMessage = "";
    let successMessage = "";

    onMount(() => {
        const params = new URLSearchParams(window.location.search);
        uid = params.get("uid");
        token = params.get("token");
    });

    async function resetPassword() {
        if (newPassword !== confirmPassword) {
            errorMessage = "Passwords do not match";
            return;
        }

        let response = await reset_password_confirm(uid, token, newPassword, confirmPassword, backendURL);

        const data = await response.json();
        if (response.ok) {
            successMessage = "Password reset successful!";
        } else {
            errorMessage = data.detail || "An error occurred.";
        }
    }
</script>

<div>
    <h1>Reset Password</h1>
    {#if errorMessage}
        <p style="color: red;">{errorMessage}</p>
    {/if}
    {#if successMessage}
        <p style="color: green;">{successMessage}</p>
    {/if}
    <form on:submit|preventDefault={resetPassword}>
        <label>
            New Password:
            <input type="password" bind:value={newPassword} required />
        </label>
        <label>
            Confirm Password:
            <input type="password" bind:value={confirmPassword} required />
        </label>
        <button type="submit">Reset Password</button>
    </form>
</div>
