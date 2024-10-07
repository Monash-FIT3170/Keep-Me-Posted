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
  import ArrowLeft from "../../assets/arrow-left.png"
  import ArrowRight from "../../assets/arrow-right.png"

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
    goto("/generate_summary")
  };
</script>


<UserEmailEntry></UserEmailEntry>

<div class="{$isOpen ? "opacity-50" : ""}">
  <Topbar></Topbar>

  <div class="flex flex-col text-center">
    <div class="flex flex-col p-12 gap-4">
      <h1>Add Recipients</h1>
      <div class="subheading">
        Add the emails you would like to send the summary to.
      </div>
    </div>

    <EmailEntry></EmailEntry>
    <EmailList></EmailList>
  </div>

  <div class="absolute bottom-8 right-8">
    <Button
      handleClick={nextPage}
      icon={ArrowRight}
      iconPos='right'
      text="Send Email"
      disabled={$ContactsStore.length == 0 && $isCancelled == true}
      type={($ContactsStore.length == 0 && $isCancelled == true) ? "disabled" : "primary"}
    ></Button>
  </div>
</div>

<div class="absolute bottom-8 left-8">
  <Button
    handleClick={previousPage}
    icon={ArrowLeft}
    text="View Summary"
  ></Button>
</div>
