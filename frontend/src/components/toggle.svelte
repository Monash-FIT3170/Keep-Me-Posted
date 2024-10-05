<!-- Toggle Component

    Contains toggle to enable transcript attachment

    Author: Maureen
    Last modified: 15/08/2024

-->

<script>

    import { sendWithTranscriptStore } from "../stores/transcript-store";
    import { get } from "svelte/store";
    
    let isChecked = get(sendWithTranscriptStore);

    $: sendWithTranscriptStore.set(isChecked);
</script>

<div class="flex items-center justify-center p-8">

  <label class="flex items-center space-x-2">
    <input
    type="checkbox"
    value=""
    class="sr-only peer"
    bind:checked={isChecked}
    />
    <div class="cursor-pointer relative w-7 h-4 bg-gray-300
        dark:peer-focus:ring-blue-800 rounded-full peer
        dark:bg-gray-700 peer-checked:after:translate-x-3/4
        rtl:peer-checked:after:-translate-x-3/4
        peer-checked:after:border-blue-600 after:absolute
        after:bg-white after:border-gray-300 after:border
        after:rounded-full after:h-4 after:w-4 after:transition-all
        dark:border-gray-600 peer-checked:bg-blue-600"></div>

    <span class="p-[5px] text-base text-black after:content-['*'] after:text-red-500">
        Attach meeting transcript with email?
    </span>
  </label>
</div>


