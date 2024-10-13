<!-- Summary will be sent after generation page

    The end page when user reaches the end before the summary has generated

    Author: Parul Garg
    Last Modified: 15/08/2024
-->

<script>
  import Button from "../../components/button.svelte";
  import Topbar from "../../components/topbar.svelte";
  import clock from "../../assets/clock.png";
  import green_tick from "../../assets/green-tick.png";
  import { goto } from "$app/navigation";
  import Recipients from "../../components/sendRecipientsList.svelte";
  import { sendWithTranscriptStore } from "../../stores/transcript-store";
  import { resetStores } from "../../stores/reset-store";
  import { emailStatusStore } from "../../stores/email-status-store";
  import { apiStatusStore } from "../../stores/api-status-store";
  import { ContactsStore } from "../../stores/contacts-store";
  import { summaryStore } from "../../stores/summary-store";
  import { transcriptStore } from "../../stores/transcript-store";
  import { send_email } from "../../api-functions/send_email";
  import { backendURL } from "../../api-functions/base-URL";
  import { onDestroy, onMount } from "svelte";
  import { update_meeting_summary } from "../../api-functions/update_meeting_summaries"
  import { authStore } from "../../stores/auth-store";

  let email = ""; // Initialize email as an empty string

  // Subscribe to the authStore to get updates
  const unsubscribe = authStore.subscribe(auth => {
    email = auth.email; // Update email whenever the store changes
  });

  let sending = true;
  onMount(() => {
    trySend()
  });

  let trySend = async () => {
    if (sending) {
      if ($apiStatusStore == "Complete") {
        let summary = $summaryStore.summary 

        console.log(summary)
        
        let subject = $summaryStore.subject;
        let contacts = $ContactsStore
        let transcript = $sendWithTranscriptStore ? $transcriptStore.transcriptWithSpeakers : null;

        let response = await send_email(transcript, summary, subject, contacts, backendURL);
        console.log(response)
        console.log(response == "Emails sent successfully!")

        if(response == "Emails sent successfully!"){
          update_meeting_summary(email, subject, transcript, summary, contacts, "2024-10-05T14:00:00Z", backendURL)
        }

        sending = false;
      } else {
        setTimeout(() => {
          trySend();
        }, 3000);
      }
    }
  };

  onDestroy(() => {
    sending = false
  })

  //the next page in the sequence
  let nextPage = () => {
    resetStores();
    goto("/upload_audio");
  };
</script>

<Topbar></Topbar>

<!-- The div for the content of the page excluding the button -->
<div class="flex flex-col items-center pt-3 pb-10">
  <!-- The div for the headings and the clock icon of the page -->
  <div class="flex flex-col items-center pt-10">
    <!-- styling of the clock icon -->
    <div class="flex justify-center">
      <img
        class="flex flex-row justify-center items-center p-0 flex-none order-none flex-grow-0 w-24 h-24"
        src={$emailStatusStore == "Sent" ? green_tick : clock}
        alt={$emailStatusStore == "Sent" ? "Green Tick" : "Clock"}
      />
    </div>
    <!-- the heading and subheading of the page -->
    <h1 class="pt-3 px-4">
      {$emailStatusStore == "Sent"
        ? "Your Summary Has Been Sent"
        : "Your Summary Will Be Sent"}
    </h1>
    {#if $emailStatusStore == "Sent"}
      <p
        class="subheading pt-4"
      >
        Your summary{$sendWithTranscriptStore ? " and transcript" : ""} has been
        sent to the recipients below.
      </p>
    {:else}
      <p
        class="subheading pt-4"
      >
        After the summary has been completely generated, it will be sent
        automatically{$sendWithTranscriptStore ? " with the transcript" : ""}.
      </p>
    {/if}
  </div>

  <!-- The div for the recipients section of the page -->
  <div class="flex pt-10 gap-3.125">
    <h3 class="text-xl font-bold pr-8">Recipients:</h3>
    <h3 class="font-normal flex flex-wrap">
      <Recipients></Recipients>
    </h3>
  </div>
</div>

<!-- The button for sending another summary -->
<div class="absolute bottom-10 left-1/2 transform -translate-x-1/2">
  <div class="button-holder">
    <Button handleClick={nextPage} type={$emailStatusStore == "Sent" ? "primary" : "disabled"} text="Send Another Summary"></Button>
  </div>
</div>
