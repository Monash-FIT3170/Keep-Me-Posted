<!-- Input Field with Validation Component

    Contains Input Field with title and built in validation

    Author: Rohit Valanki
    Last modified: 30/07/2024

-->
<script>
  export let label = "";
  export let value = "";
  export let placeholder = "";
  export let validationMessage = "";
  export let showValidation = false; // Default false state
  export let validationActive = false; // Default false state
  export let isPasswordType = false;
  export let onInput;
  export let isWithIcon = false; // allows for icon padding
  export let onKeydown; 

  function handleInput(event) {
    value = event.target.value;
    if (onInput) {
      onInput(value);
    }
  }

  function handleKeydown(event) {
    if (onKeydown) {
      onKeydown(event); 
    }
  }

</script>

<div id="login-form-container" class="mb-4">
  <label class="block text-gray-700 text-sm mb-1">{label}</label>
  {#if isPasswordType}
    <input
      type="password"
      bind:value
      {placeholder}
      on:input={handleInput}
      on:keydown={handleKeydown}
      class="border-gray-300 rounded-lg w-full py-3 px-3 text-gray-700 text-sm placeholder:text-sm leading-tight focus:outline-none focus:shadow-outline"
      style="border-radius: 8px; border-width: 1px;"
    />
  {:else if isWithIcon}
    <input
      type="text"
      bind:value
      {placeholder}
      on:input={handleInput}
      on:keydown={handleKeydown}
      class="pl-10 border-gray-300 rounded-lg w-full py-3 px-3 text-gray-700 text-sm placeholder:text-sm leading-tight focus:outline-none focus:shadow-outline"
      style="border-radius: 8px; border-width: 1px;"
    />
  {:else}
    <input
      type="text"
      bind:value
      {placeholder}
      on:input={handleInput}
      on:keydown={handleKeydown}
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
