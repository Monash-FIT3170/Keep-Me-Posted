<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<script>
	let email = '';
</script>

<input bind:value={email} placeholder="enter your email address" />
<p>Hello {name || 'stranger'}!</p>
