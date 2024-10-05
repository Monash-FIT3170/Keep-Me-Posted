<script>
  import { Card } from 'flowbite-svelte';
  import Regenerate from "../assets/regenerate-icon.png";
</script>

<Card>
  <a href="/">
    <h5 class="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white">Summary History</h5>
  </a>
  
  <!-- Text box for summary, truncated to 3 lines (edit the line clamp for more) -->
  <p class="mb-3 font-normal text-gray-700 dark:text-gray-500 overflow-hidden text-ellipsis line-clamp-3">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis scelerisque semper massa ut placerat. Sed ligula purus, interdum ut metus vitae, suscipit congue massa. Pellentesque vel mauris finibus, suscipit massa non, dignissim sem. Quisque vel ullamcorper eros. Nulla malesuada mi et facilisis egestas. Curabitur eget erat sit amet ligula egestas convallis. Nulla facilisi. Fusce nisl arcu, lacinia et libero quis, bibendum ultricies justo. Praesent dapibus blandit finibus. Maecenas semper ante nec neque pulvinar, vitae eleifend diam consectetur. Suspendisse viverra nisi a mi ullamcorper mattis.
  </p>

  <!-- Container for summary date and resent button -->
  <div class="flex items-center justify-between text-primary-600">
    <a href="/" class="inline-flex items-center text-gray-500 dark:text-gray-400 hover:underline">
      Sent dd/mm/yy
    </a>
    <button class="ml-4 min-w-[120px] font-bold px-4 py-2 bg-blue-100 text-blue-600 hover:bg-blue-200 hover:text-blue-700 rounded-md transition-all duration-300 ease-in-out flex items-center">
      <img class="h-5 mr-3" src={Regenerate} alt="Regenerate Icon" />
      <span class="text-blue-600">Resend</span>
    </button>
  </div>
</Card>