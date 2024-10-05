<!-- Profile Page 

    Page that shows previously sent summaries 

    Author: Jeremy Wang, Afia Farzana
    Last Modified: 05/10/2024
-->

<script>
    import Card from "../../components/summaryCard.svelte";
    import Topbar from "../../components/topbar.svelte";
</script>
  
  <body class="p-4 sm:p-8">
    <Topbar />
    <h1 class="class=text-3xl sm:text-4xl font-bold text-center mt-6 mb-4 text-gray-900 dark:text-white"> 
      Summary History
    </h1>
    <h2 class="text-lg sm:text-xl font-normal text-center mt-4 mb-6 text-gray-700 dark:text-gray-400">
      View your previously generated summaries here
  </h2>
    <!-- Card Container Section -->
  <div class="flex flex-col sm:flex-row gap-4 flex-wrap justify-center">
    <!-- First Card -->
    <Card class="w-full sm:max-w-sm bg-white shadow-lg rounded-lg p-6" />
    
    <!-- Add more cards here -->
    <Card class="w-full sm:max-w-sm bg-white shadow-lg rounded-lg p-6" />
    <Card class="w-full sm:max-w-sm bg-white shadow-lg rounded-lg p-6" />
  </div>
  </body>
  