<!-- Login Prompt Component

    Contains Login Prompt component with hyperlink

    Author: Rohit Valanki
    Last modified: 31/07/2024

-->
<script>
  export let handleClick;
  export let isPrimary = true; // Default to primary color
  export let text = "The main text";
  export let linkText = "Linktext";
</script>

<div class="flex flex-row items-center space-x-1">
  <div class="text-gray-500 text-xs">
    {text}
  </div>
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div
    class="text-xs font-inter font-semibold cursor-pointer"
    on:click={handleClick}
    class:text-[#6941C6]={isPrimary}
    class:text-[#175cd3]={!isPrimary}
  >
    {linkText}
  </div>
</div>
