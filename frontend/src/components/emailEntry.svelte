
<!--

	Email Input Box and Add Recipients Button Component

	consists of parts
	1. the email input field along with the icon
	2. the add recipients button

	Authors: Harrison Lane
	Editied by: Parul Garg, Angelina Leung, Maureen Pham
	Last Modified: 9/10/24 by Parul Garg

-->

<script>
  // necessary imports
  import Button from "../components/button.svelte";
  import { ContactsStore } from "../stores/contacts-store";
  import { authStore } from "../stores/auth-store";
  import AddIconBlue from "../assets/add-icon-blue.png";
  import { onMount } from "svelte";
  import mailIcon from "../assets/mail.png"
  let emailString = "";
  let emailErrorString = "";
  let searchResults = [];
  let inputFocused = false;

  onMount(() => {
    // $authStore.mailing_list = [
    //   "fgh6a@abc.com",
    //   "jklb7p@xyz.net",
    //   "mn234@def.org",
    //   "zxcvbnm@ghi.co",
    //   "qw56er@jkl.org",
    //   "ty8uio@xyz.com",
    //   "as9df@pqr.co",
    //   "gh1jk@stu.com",
    //   "qazwsx@vbn.com",
    //   "edc45rf@poi.net",
    // ]; 
    // uncomment this to see dummy email data
  });

  //logic to check and add the entered email
  let addEmail = () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    // checking if entered email string is valid
    if (emailRegex.test(emailString)) {
      // if valid, add the email to the contacts store
      ContactsStore.update((prev) => {
        // handling duplicate email entries
        if (prev.includes(emailString)) {
          return prev;
        } else {
          return [...prev, emailString];
        }
      });
      emailString = "";
    } 
    // if email string is not valid
    else {
      emailErrorString = "Please enter a valid email address.";
      setTimeout(() => {
        emailErrorString = "";
      }, 3000);
    }
  };

  let searchEmails = () => {
    searchResults = $authStore.mailing_list.filter((email) =>
      email.toLowerCase().includes(emailString.toLowerCase())
    );
  };

  let handleFocus = () => {
    inputFocused = true;
    searchEmails();
  };

  let handleBlur = () => {
    setTimeout(() => {
      inputFocused = false; // Delay to allow click on search results
    }, 100);
  };
  
  function handleKeydown(event) {
    if (event.key === "Enter") {
      addEmail();
    }
  }

</script>

<!-- Input box and the add recipients buttton -->
<div class="flex justify-center gap-2 px-4">
  <div class="relative">
    <input
      class="border border-slate-300 pl-9 p-2 rounded-xl w-full sm:w-96 h-full"
      type="email"
      placeholder="johndoe@email.com"
      bind:value={emailString}
      on:input={searchEmails}
      on:focus={handleFocus}
      on:blur={handleBlur}
    />
    <button
      class="absolute cursor-default left-3 top-1/2 transform -translate-y-1/2"
      type="button"
    >
    <img src={mailIcon} id="icon" class="h-4 w-4" alt="mail icon"/>
    </button>

    {#if inputFocused && searchResults.length > 0}
      <div
        class="absolute bg-white shadow-sm border border-gray-300 rounded-lg w-full z-10 max-h-48 overflow-y-scroll my-1"
      >
        <ul class="py-2 space-y-2">
          {#each searchResults as result}
            <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <li class="px-4 py-2 hover:bg-gray-200 rounded-xl cursor-pointer flex" on:click={() => {
                emailString = result;
                addEmail();
              }}>
              {result}
            </li>
          {/each}
        </ul>
      </div>
    {/if}
  </div>

  <Button handleClick={addEmail} icon={AddIconBlue} text="" type="secondary">
    <span class="hidden sm:inline sm:ml-2 text-blue-700">Add Recipient</span>
  </Button>
</div>

{#if emailErrorString}
  <div class="text-red-500 absolute bottom-8 left-1/2 transform -translate-x-1/2">{emailErrorString}</div>
{/if}
