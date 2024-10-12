<script>
  import { Card } from 'flowbite-svelte';
  import Regenerate from "../assets/regenerate-icon.png";
  import { goto } from "$app/navigation";

  export let subject = "Summary History";
  export let transcript = "Default summary text goes here.";
  export let date = "dd/mm/yyyy";

  // Function to handle navigating to the specified page
  function handleResend() {
    goto("/resend_summary"); 
  }
</script>

<Card>
  <h5 class="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white overflow-hidden whitespace-nowrap text-ellipsis">
    {subject}
  </h5>
  
  <p class="mb-3 font-normal text-gray-700 dark:text-gray-500 overflow-hidden text-ellipsis line-clamp-3">
    {transcript}
  </p>

  <div class="flex items-center justify-between text-primary-600">
    <span class="text-gray-500 dark:text-gray-400">
      {date}
    </span>
    <button 
      class="ml-4 min-w-[120px] font-bold px-4 py-2 bg-blue-100 text-blue-600 hover:bg-blue-200 hover:text-blue-700 rounded-md transition-all duration-300 ease-in-out flex items-center"
      on:click={handleResend}
    >
      <img class="h-5 mr-3" src={Regenerate} alt="Regenerate Icon" />
      <span class="text-blue-600">Resend</span>
    </button>
  </div>
</Card>



