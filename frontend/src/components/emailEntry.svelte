<script>
  import Button from "../components/button.svelte";
  import { ContactsStore } from "../stores/contacts-store"
  import AddIconBlue from "../assets/add-icon-blue.png"
  import mailIcon from "../assets/mail.png"
  let emailString = "";
  let emailErrorString = "";

  let addEmail = () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailRegex.test(emailString)) {
      ContactsStore.update((prev) => {
        if (prev.includes(emailString)) {
          return prev;
        } else {
          return [...prev, emailString];
        }
      });
      emailString = "";
    } else {
      emailErrorString = "Please enter a valid email address.";
      setTimeout(() => {
        emailErrorString = "";
      }, 3000);
    }
  };
</script>

<div class="flex justify-center gap-2 px-4">
    <div class="relative">
      <input
        class="border border-slate-300 pl-9 p-2 rounded-xl w-full sm:w-96 h-full"
        type="email"
        placeholder="johndoe@email.com"
        bind:value={emailString}
      />
      <button
            class="absolute cursor-default left-3 top-1/2 transform -translate-y-1/2"
            type="button">
          <img src={mailIcon} id="icon" class="h-4 w-4"/>
      </button>
    </div>
  <Button
    handleClick={addEmail}
    icon={AddIconBlue}
    text=""
    type="secondary"
  >
    <span class="hidden sm:inline sm:ml-2 text-blue-700">Add Recipient</span>
  </Button>
</div>
