<script>
  import { onDestroy } from 'svelte'; // Import onDestroy to unsubscribe
  import kmpIcon from "../assets/kmp-icon.png";
  import profileIcon from "../assets/profile-icon.png";
  import profileHoverIcon from "../assets/profile-icon-dark.png";
  import logOutIcon from "../assets/log-out-icon.png";
  import Button from "../components/button.svelte";
  import { getAuth, authStore, clearAuth } from "../stores/auth-store.js";
  import { goto } from "$app/navigation";
  import { resetStores } from "../stores/reset-store.js";
  import PopUpModal from '../components/popUpModal.svelte';

  let showDropdown = false;
  let isHovered = false;
  let profileIcons = [profileIcon, profileHoverIcon];
  let popUpModalComponent;  

  let email = ""; // Initialize email as an empty string

  // Subscribe to the authStore to get updates
  const unsubscribe = authStore.subscribe(auth => {
    email = auth.email; // Update email whenever the store changes
  });

  // Ensure to unsubscribe when the component is destroyed
  onDestroy(() => {
    unsubscribe(); 
  });

  // Hover handling
  function hover() {
    isHovered = true;
    showDropdown = true; // Open dropdown on hover
  }

  // When non-hovering
  function antiHover() {
    isHovered = false;
    showDropdown = false; // Close dropdown on hover end
  }

  // Function to handle logging out
  function handleLogout() {
    clearAuth();
    resetStores();
    goto("/login");
    console.log("todo - handle logout");
  }

  // Function to handle going to main page (NOT sign in if they are signed in already)
  function handleGoHome() {
    console.log("todo - handle go to home");
  }

  // Function to handle navigating to sign in page
  function handleSignIn() {
    goto("/login");
  }

  // Function to handle toggling the pop up
  function toggleLogOut() {
    popUpModalComponent.togglePopUp();
    toggleDropdown();
  }
</script>

<body>
  <div class="z-50 fixed">
    <PopUpModal
    bind:this={popUpModalComponent}
    type="secondary"
    header="Are you sure you want to log out?"
    mainText="Your session will not be saved."
    firstButtonText="Log Out"
    secondButtonText="Cancel"
    firstHandleClick={handleLogout}
    secondHandleClick={toggleLogOut}
    width="96"
    />
  </div>
  <div class="flex justify-center items-center justify-between border-b h-20">
    <div class="px-8 m">
      <button on:click={() => handleGoHome()}>
        <img class="h-12" src={kmpIcon} alt="KMP Icon" />
      </button>
    </div>

    <div class="px-8 flex">
      <div>
        {#if (email)} <!-- Check if email is available -->
          <button 
            on:click={() => goto("/profile")} 
            on:mouseenter={hover} 
            on:mouseleave={antiHover}
            class="relative"
          >
            <div class="flex justify-center items-center px-8">
              <img class="h-6" src={isHovered ? profileHoverIcon : profileIcon} alt="Profile Icon" />
            </div>
          </button>

          {#if showDropdown}
            <div class="w-fit absolute bg-white shadow right-16 py-2 rounded-lg z-40">
              <div class="text-left w-fit py-2 rounded-lg">
                <div class="text-gray-500 text-base px-5 pb-2 w-full">
                  {email} <!-- Show the logged-in user's email -->
                </div>
                <div class="w-full border-t border-gray-100"></div>
                <div class="flex w-full float-start items-start justify-start pt-3 pb-1 px-3">
                  <button class="hover:bg-gray-100 rounded-lg font-sans justify-center items-center flex w-full h-8" on:click={popUpModalComponent.togglePopUp()}>
                    <div class="justify-start items-center flex flex-row w-full ms-1 px-1">
                      <img class="h-4" src={logOutIcon} alt="Log Out Icon" />
                      <div class="text-gray-700 text-base px-3">Log Out</div>
                    </div>
                  </button>
                </div>
              </div>
            </div>
          {/if}
        {:else} 
         <Button type="secondary" text="Sign In" handleClick={handleSignIn}/>
        {/if}
      </div>
    </div>
  </div>
</body>
