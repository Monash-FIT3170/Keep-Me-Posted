<!-- Summary generation page

    Page that shows the summary generated

    Author: Brenda Dang, Diya Ramesh
    Last Modified: 1/08/2024
-->

<script>
    import Card from "../../components/summaryCard.svelte";
    import Topbar from "../../components/topbar.svelte";
</script>
  
  <body>
    <Topbar />
    <h1 class="text-4xl font-bold text-center mt-6 mb-4 text-gray-900 dark:text-white">
      Summary History
    </h1>
    <h2 class="text-lg font-normal text-center mt-4 mb-6 text-gray-700 dark:text-gray-400">
      View your previously generated summaries here
  </h2>
    <!-- Card Container Section -->
  <div class="flex flex-row gap-4 flex-wrap justify-center">
    <!-- First Card -->
    <Card class="max-w-sm bg-white shadow-lg rounded-lg p-6" />
    
    <!-- Add more cards here -->
    <Card class="max-w-sm bg-white shadow-lg rounded-lg p-6" />
    <Card class="max-w-sm bg-white shadow-lg rounded-lg p-6" />
  </div>
  </body>
  