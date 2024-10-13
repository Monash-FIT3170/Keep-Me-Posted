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
  import { ContactsStore } from "../stores/contacts-store"
  import AddIconBlue from "../assets/add-icon-blue.png"
  import mailIcon from "../assets/mail.png"
  let emailString = "";
  let emailErrorString = "";

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

  function handleKeydown(event) {
    if (event.key === "Enter") {
      addEmail();
    }
  }

</script>

<!-- Input box and the add recipients buttton -->
<div class="flex justify-center gap-2 px-4">
  <!-- Input box div -->
    <div class="relative">
      <!-- Input box -->
      <input
        class="border border-slate-300 pl-9 p-2 rounded-xl w-full sm:w-96 h-full"
        type="email"
        placeholder="johndoe@email.com"
        bind:value={emailString}
        on:keydown={handleKeydown}
      />
      <!-- mail icon in the input box -->
      <button
            class="absolute cursor-default left-3 top-1/2 transform -translate-y-1/2"
            type="button">
          <img src={mailIcon} id="icon" class="h-4 w-4"/>
      </button>
    </div>
  
  <!-- Add recipients button div -->
  <Button
    handleClick={addEmail}
    icon={AddIconBlue}
    text=""
    type="secondary"
  >
  <!--hiding the text in mobile view-->
    <span class="hidden sm:inline sm:ml-2 text-blue-700">Add Recipient</span>
  </Button>
</div>
