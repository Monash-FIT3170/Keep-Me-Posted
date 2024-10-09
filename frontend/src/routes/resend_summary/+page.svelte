<script>
    import Button from "../../components/button.svelte";
    import Topbar from "../../components/topbar.svelte";
    import EmailEntry from "../../components/emailEntry.svelte";
    import EmailList from "../../components/emailList.svelte";
    import { goto } from "$app/navigation";
    import { ContactsStore } from "../../stores/contacts-store";
    import { authStore } from "../../stores/auth-store"
    import { isOpen, isCancelled} from "../../stores/user-email-popup-store";
    import UserEmailEntry from "../../components/userEmailEntry.svelte";
    import { onMount } from "svelte";
    import ArrowRight from "../../assets/arrow-right.png"
    import SummaryBox from "../../components/summary-box.svelte";
    import SendRecipients from "../../components/sendRecipientsList.svelte";
    import Toggle from "../../components/toggle.svelte"; 

    let summaryBoxRef;
    let sendRecipientsRef;
    let toggleRef; 
  
    onMount(() => {
      if ($authStore["loggedIn"] == true) {
        ContactsStore.update((prev) => {
          if (prev.includes($authStore["email"])) {
            return prev;
          } else {
            return [...prev, $authStore["email"]];
          }
        })
      }
    })
  
    
    let nextPage = () => {
      if ($authStore.email.length == 0 && !($isCancelled)) {
        isOpen.set(true)
      } else {
        goto("/send_summary")
      }
    };
  
    let previousPage = () => {
      goto("/profile")
    };
  </script>
  
  
  
  
  <div class="{$isOpen ? "opacity-50" : ""}">
    <Topbar></Topbar>
    <div class="flex flex-col text-center">
      <div class="flex flex-col p-12 gap-4">
        <h1>Resend Summary</h1>
        <div class="subheading">
          You can add or remove your previous recipients and resend your summary. 
        </div>
        <EmailEntry></EmailEntry>
      </div>
    </div>

    <div class="flex flex-col text-center">
      <div class="flex flex-col text-center">
        <h6 style="color: grey">Previously sent to: </h6>
        <EmailList></EmailList>
      </div>
      <Toggle></Toggle>
    </div>

    <div>
      <SummaryBox bind:this={summaryBoxRef} />
    </div>
  
    <div style="margin-left: 1100px; margin-top:10px">
      <Button
        handleClick={nextPage}
        icon={ArrowRight}
        iconPos='right'
        text="Resend Email"
        disabled={$ContactsStore.length == 0 && $isCancelled == true}
        type={($ContactsStore.length == 0 && $isCancelled == true) ? "disabled" : "primary"}
      ></Button>

    </div>

    

    
  </div>
  
  