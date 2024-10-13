<!-- Email Popup Modal Component

    A pop up that shows when continuing without sign in
    Prompts user to enter their email address

    Author: Harry Lane, Maureen Pham
    Last modified: 9/08/2024

-->

<script>
  import Button from "./button.svelte";
  import { ContactsStore } from "../stores/contacts-store";
  import { isOpen, isCancelled } from "../stores/user-email-popup-store";
  import InputFieldWithValidation from "./input-field-with-validation.svelte";

  let emailString = "";
  let emailErrorString = "";
  let showEmailError = false;

  let handleCancel = () => {
    isCancelled.set(true);
    isOpen.set(false);
  };

  let handleAddEmail = () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailRegex.test(emailString)) {
      ContactsStore.update((prev) => [...prev, emailString]);
      emailString = "";
      isOpen.set(false);
      isCancelled.set(true);
    } else {
      emailErrorString = "Please enter a valid email address.";
      showEmailError = true;
    }
  };

  function handleKeydown(event) {
    if (event.key === "Enter") {
      handleAddEmail();
    }
  }

</script>

{#if $isOpen}
    <!-- Overlay -->
    <div class="fixed inset-0 bg-black bg-opacity-50 z-40"></div>

    <!-- Popup Content -->
     <div class="fixed inset-0 flex items-center justify-center z-50">
        <div class="p-4 w-full max-w-md bg-white border rounded-xl">
            <div class="h2 text-center text-gray-900 font-semibold p-2">Would you like to receive a copy of the summary?</div>

      <div class="h3 text-center text-gray-500 text-base p-1">
        Add your email to receive the summary.
      </div>

      <div class = "w-full px-4 py-2">
        <div class="relative">
            <InputFieldWithValidation
                isWithIcon={true}
                label="Email Address"
                placeholder="you@kmp.com"
                bind:value={emailString}
                validationMessage={emailErrorString}
                validationActive={showEmailError}
                onKeydown={handleKeydown}
                />
                <button
                    class="absolute cursor-default h-5 w-5 left-3 top-9 py-2 flex items-center bg-white"
                    type="button">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="#667085" class="size-12">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75" />
                  </svg>
                </button>
        </div>
      </div>



      <div class="flex shrink justify-between pb-1 pt-0 items-center">
        <div class = "w-5/12 pl-4">
            <Button
              type="secondary"
              text="No, thanks"
              fullWidth={true}
              handleClick={handleCancel}
            ></Button>
        </div>
        <div class = "w-5/12 pr-4">
        <Button
          type="primary"
          text="Add myself"
          fullWidth={true}
          handleClick={handleAddEmail}
        ></Button>
        </div>
      </div>
    </div>
    </div>
{/if}