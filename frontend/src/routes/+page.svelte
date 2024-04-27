<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<script>
	let email = '';

    function handleInput(event) {
    userEmail = event.target.value;
  }
</script>

<input type="email" placeholder="Enter your email" bind:value={email} on:input={handleInput} />
<p>Your email is: {email}</p>