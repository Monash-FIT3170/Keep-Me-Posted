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
            class="absolute cursor-default h-5 w-5 left-3 top-3 py-2 flex items-center bg-white"
            type="button">
          <!-- <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.9" stroke="#667085" class="size-12">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75" />
          </svg> -->
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
