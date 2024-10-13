<!-- Summary generation page

    Page that shows the summary generated

    Author: Brenda Dang, Diya Ramesh
    Last Modified: 1/08/2024
-->

<script>
  import TopBar from "../../components/topbar.svelte";
  import Button from "../../components/button.svelte";
  import SummaryBox from "../../components/summary-box.svelte";
  import { goto } from "$app/navigation";
  import { summaryStore } from "../../stores/summary-store";
  import ArrowLeft from "../../assets/arrow-left.png"
  import ArrowRight from "../../assets/arrow-right.png"
  import PopUpModal from "../../components/popUpModal.svelte";

  export let title = "Your Summary is Being Generated...";
  export let subTitle = "We are still generating your summary...";
  let summaryBoxRef;

  let backBtn = () => {
    goto("/upload_audio");
  };

  let forwardBtn = () => {
    if (summaryBoxRef && summaryBoxRef.saveSummaryToStore) {
      summaryBoxRef.saveSummaryToStore();
    }
    goto("/email");
  };

  let dots = "";
  setInterval(() => {
    if (dots.length < 3) {
      dots += ".";
    } else {
      dots = "";
    }
  }, 500);

  $: hasSummaryGenerated = $summaryStore["summary"] && $summaryStore["subject"];
  $: {
    if (hasSummaryGenerated) {
      title = "Summary Generated!";
      subTitle = "Your summary is ready to be sent.";
    } else {
      title = "Your Summary is Being Generated...";
      subTitle = "We are still generating your summary...";
    }
  }
  
</script>

<body>
  <TopBar />
  <div class="flex flex-col justify-center items-center pt-12">
    <h1>
      {hasSummaryGenerated
        ? "Summary Generated!"
        : "Your Summary is Being Generated"}
    </h1>
    <div class="subheading mt-4">
      {hasSummaryGenerated
        ? "Your summary is ready to be sent."
        : "We are still generating your summary" + dots}
    </div>
  </div>

  <div class="mt-10 mb-8">
    <SummaryBox bind:this={summaryBoxRef} />
  </div>

  {#if $summaryStore.summary}
    <div class="absolute bottom-8 left-8">
      <Button
        class="primary"
        text="Re-Upload Audio"
        icon={ArrowLeft}
        handleClick={backBtn}
      />
    </div>
    <div class="absolute bottom-8 right-8">
      <Button
        class="primary"
        text="Add Recipients"
        icon={ArrowRight}
        iconPos="right"
        handleClick={forwardBtn}
      />
    </div>
  {:else}
    <div class="absolute bottom-8 left-8">
      <Button
        class="primary"
        text="Re-Upload Audio"
        icon={ArrowLeft}
        handleClick={backBtn}
      />
    </div>

    <div class="absolute bottom-8 right-8">
      <Button
        class="primary"
        text="Add Recipients"
        icon={ArrowRight}
        iconPos="right"
        handleClick={forwardBtn}
      />
    </div>
  {/if}
</body>
