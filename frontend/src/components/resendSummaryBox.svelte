<script>
  import Button from "./button.svelte";
  import { summaryStore } from "../stores/summary-store";
  import { onMount } from "svelte";
  import regenerateIcon from "../assets/regenerate-icon.png";
  import regenerateIconDisabled from "../assets/regenerate-icon-disabled.png";
  import PopUpModal from "./popUpModal.svelte";
  import { marked } from "marked";
  import TurndownService from "turndown";
  import { transcriptStore } from "../stores/transcript-store";
  import { send_summary } from "../api-functions/send_summary";
  import { backendURL } from "../api-functions/base-URL";
  import { apiStatusStore } from "../stores/api-status-store";

  export let emailSubject = "";
  export let summaryGenerated = "";
  let dots = "";

  setInterval(() => {
    if (dots.length < 3) {
      dots += ".";
    } else {
      dots = "";
    }
  }, 500);

  function autoResize(event) {
    const textarea = event.target;
    textarea.style.height = `${textarea.scrollHeight}px`;
  }

  function loadSummaryContent() {
    const unsubscribe = summaryStore.subscribe((value) => {
      if (!summaryGenerated) {
        summaryGenerated = marked(value.summary);
      }
      if (!emailSubject) {
        emailSubject = value.subject;
      }
    });
    if (summaryGenerated && emailSubject) {
      unsubscribe();
    }
  }

  onMount(() => {
    loadSummaryContent();
  });

  export const saveSummaryToStore = () => {
    if (emailSubject) {
      const updatedSubject = document.getElementById("emailSubject").value;
      if (updatedSubject) {
        summaryStore.update((current) => {
          return {
            ...current,
            subject: updatedSubject,
          };
        });
      }
    }
    if (summaryGenerated) {
      const updatedSummary =
        document.getElementById("summaryGenerated").innerHTML;
      const turndownService = new TurndownService();
      let markdownContent = turndownService.turndown(updatedSummary);
      if (updatedSummary) {
        summaryStore.update((current) => {
          return {
            ...current,
            summary: markdownContent,
          };
        });
      }
    }
  };

  let regenerateBtn;
  let popUpModalComponent;

  function cancelRegenerate() {
    apiStatusStore.set("Cancel");
    popUpModalComponent.togglePopUp();
    regenerateBtn.toggleDisabled();
    regenerateBtn.replaceIcon(regenerateIconDisabled);
  }

  function openRegeneratePopUp() {
    popUpModalComponent.resetProgress();
    popUpModalComponent.togglePopUp();
    popUpModalComponent.animateProgress();

    let currentSubject = emailSubject;
    let currentSummary = summaryGenerated;

    send_summary($transcriptStore.transcript, backendURL)
      .then((response) => {
        emailSubject = $summaryStore.subject;
        summaryGenerated = $summaryStore.summary;
        if ($apiStatusStore == 'Cancel') {
          console.log("Regenerate cancelled");
          emailSubject = currentSubject;
          summaryGenerated = currentSummary;
          saveSummaryToStore();
          apiStatusStore.set('');
          regenerateBtn.toggleDisabled();
          regenerateBtn.replaceIcon(regenerateIcon);
          return;
        };
        console.log("Summary and subject successfully updated from backend.");
        if (popUpModalComponent.getVisible() == true) {
          popUpModalComponent.togglePopUp();
          popUpModalComponent.resetProgress();
        }
      })
      .catch((error) => {
        console.error("Failed to regenerate summary and subject:", error);
        if (popUpModalComponent.getVisible() == true) {
          popUpModalComponent.togglePopUp();
          popUpModalComponent.resetProgress();
        }
      });
  }
</script>


<style>
  input:focus {
    outline: none;
    box-shadow: none;
  }
  
  input {
    outline: none;
  }

  input:focus {
    outline: none;
    border-color: inherit; /* This ensures the border doesn't change color on focus */
    box-shadow: none; /* Remove shadow */
  }
</style>

<div>
  <div class="z-50 fixed">
    <PopUpModal
      bind:this={popUpModalComponent}
      header="Regenerating..."
      mainText=""
      type="loading"
      firstButtonText="Cancel"
      firstHandleClick={cancelRegenerate}
      width="96"
    />
  </div>
  <div class="rounded-lg p-4 w-11/12 sm:w-9/12 mx-auto" style="background-color: #F5FAFF;">
    {#if summaryGenerated && emailSubject}
      <div class="flex justify-end ml-auto"></div>
    {/if}
    <div class="flex flex-col gap-0 mb-4">
      <label
        class="block text-dark font-semibold pl-2 text-lg mb-2"
        style="color:#667085"
        for="emailSubject"
      >
        Email Subject
      </label>
      {#if emailSubject}
        <input
          class="w-full p-2 rounded border-[#D1E3F0] bg-[#F5FAFF]"
          type="text"
          id="emailSubject"
          readonly
          bind:value={emailSubject}
          placeholder="Your subject will be generated here..."
        />
      {:else}
        <div class="w-full p-2 rounded text-slate-400 font-bold">
          Your subject will be generated here{dots}
        </div>
      {/if}
    </div>
    <div class="flex flex-col gap-0 mb-4">
      <label
        class="lock text-dark font-semibold pl-2 text-lg mb-2"
        style="color:#667085"
        for="summaryGenerated"
      >
        Summary
      </label>
      {#if summaryGenerated}
        <div
          class="w-full p-2 rounded text-base border border-[#D1E3F0] bg-[#F5FAFF] focus-within:border-blue-500 focus-within:border-2 focus-within:p-1.5 outline-none"
          style=""
          id="summaryGenerated"
          placeholder="Your summary will be generated here..."
          readonly
        >
          {@html marked(summaryGenerated)}
        </div>
      {:else}
        <div class="w-full p-2 rounded text-slate-400 text-base">
          Your subject will be generated here{dots}
        </div>
      {/if}
    </div>
  </div>
</div>
