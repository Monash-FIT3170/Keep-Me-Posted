<script>
  export let emailSubject = "";   // This will hold the email subject
  export let summaryGenerated = ""; // This will hold the summary (transcript)
  
  // Remove internal scrolling in textarea and expand outer div instead
  function autoResize(event) {
    const textarea = event.target;
    textarea.style.height = `${textarea.scrollHeight}px`;
  }
</script>

<div class="rounded-lg p-4 w-11/12 sm:w-9/12 mx-auto" style="background-color: #F5FAFF;">
  <div class="flex flex-col gap-0 mb-4">
    <label class="block text-dark font-semibold pl-2 text-lg mb-2" style="color:#667085" for="emailSubject">
      Email Subject
    </label>
    <input
      class="w-full p-2 rounded border-[#D1E3F0] bg-[#F5FAFF]"
      type="text"
      id="emailSubject"
      bind:value={emailSubject}
    />
  </div>

  <div class="flex flex-col gap-0 mb-4">
    <label class="block text-dark font-semibold pl-2 text-lg mb-2" style="color:#667085" for="summaryGenerated">
      Summary
    </label>
    <textarea
      class="w-full p-2 rounded text-base border border-[#D1E3F0] bg-[#F5FAFF] focus-within:border-blue-500 focus-within:border-2 focus-within:p-1.5 outline-none"
      id="summaryGenerated"
      bind:value={summaryGenerated}
      on:input={autoResize}
      rows="4"
    ></textarea>
  </div>
</div>
