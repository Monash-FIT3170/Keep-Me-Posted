<!-- Input Field with Validation Component

    Contains Input Field with title and built in validation

    Author: Rohit Valanki
    Modified by: Bowen Dong
    Last modified: 30/09/2024

-->
<script>
  import eyeClosed from "../assets/eye-closed.svg";
  import eyeOpen from "../assets/eye-open.svg";
  export let label = "";
  export let value = "";
  export let placeholder = "";
  export let validationMessage = "";
  export let showValidation = false; // Default false state
  export let validationActive = false; // Default false state
  export let isPasswordType = false;
  export let onInput;
  export let isWithIcon = false; // allows for icon padding
  let showPassword = false;

  function handleInput(event) {
    value = event.target.value;
    if (onInput) {
      onInput(value);
    }
  }
</script>

<div id="login-form-container" class="mb-4">
  <label class="block text-gray-700 text-sm mb-1">{label}</label>
  {#if isPasswordType}
    <div class="relative">
      {#if showPassword}
        <!-- Show password -->
        <input
          type="text"
          bind:value
          {placeholder}
          on:input={handleInput}
          class="border-gray-300 rounded-lg w-full py-3 px-3 text-gray-700 text-sm placeholder:text-sm leading-tight focus:outline-none focus:shadow-outline"
          style="border-radius: 8px; border-width: 1px;"
        />
      {:else}
        <!-- Hide password  -->
        <input
          type="password"
          bind:value
          {placeholder}
          on:input={handleInput}
          class="border-gray-300 rounded-lg w-full py-3 px-3 text-gray-700 text-sm placeholder:text-sm leading-tight focus:outline-none focus:shadow-outline"
          style="border-radius: 8px; border-width: 1px;"
        />
      {/if}
      <!-- Toggle button for showing/hiding password -->
      <button
        type="button"
        class="absolute inset-y-0 right-0 px-3 text-gray-400"
        on:click={() => (showPassword = !showPassword)}
        aria-label={showPassword ? "Hide password" : "Show password"}
      >
        {#if showPassword}
          <img src={eyeOpen} alt="Show password" class="h-5 w-5" />
        {:else}
          <img src={eyeClosed} alt="Hide password" class="h-5 w-5" />
        {/if}
      </button>
    </div>
  {:else if isWithIcon}
    <input
      type="text"
      bind:value
      {placeholder}
      on:input={handleInput}
      class="pl-10 border-gray-300 rounded-lg w-full py-3 px-3 text-gray-700 text-sm placeholder:text-sm leading-tight focus:outline-none focus:shadow-outline"
      style="border-radius: 8px; border-width: 1px;"
    />
  {:else}
    <input
      type="text"
      bind:value
      {placeholder}
      on:input={handleInput}
      class="border-gray-300 rounded-lg w-full py-3 px-3 text-gray-700 text-sm placeholder:text-sm leading-tight focus:outline-none focus:shadow-outline"
      style="border-radius: 8px; border-width: 1px;"
    />
  {/if}
  {#if showValidation || validationActive || validationMessage}
    <p
      id="validation-message"
      class={validationActive
        ? "text-red-500 text-xs m-1"
        : "text-[#959595] text-xs m-1"}
    >
      {validationMessage}
    </p>
  {/if}
</div>
