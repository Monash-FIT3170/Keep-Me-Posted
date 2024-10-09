<script>
  import { onDestroy } from 'svelte'; // Import onDestroy to unsubscribe
  import kmpIcon from "../assets/kmp-icon.png";
  import profileIcon from "../assets/profile-icon.png";
  import profileHoverIcon from "../assets/profile-icon-dark.png";
  import logOutIcon from "../assets/log-out-icon.png";
  import Button from "../components/button.svelte";
  import { getAuth, authStore, clearAuth } from "../stores/auth-store.js";
  import { goto } from "$app/navigation";
  import { resetStores, resetStoresOnHomeClick } from "../stores/reset-store.js";

  let showDropdown = false;
  let profileIcons = [profileIcon, profileHoverIcon];
  let currentIconIndex = 0;

  let email = ""; // Initialize email as an empty string

  // Subscribe to the authStore to get updates
  const unsubscribe = authStore.subscribe(auth => {
    email = auth.email; // Update email whenever the store changes
  });

  // Ensure to unsubscribe when the component is destroyed
  onDestroy(() => {
    unsubscribe();
  });

  // Function to toggle dropdown
  function toggleDropdown() {
    showDropdown = !showDropdown;
    currentIconIndex = (currentIconIndex + 1) % profileIcons.length;
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
    console.log(email);
    resetStoresOnHomeClick();
    if (email == "") {
      clearAuth();
      goto("/login");
    } else {
      goto("/upload_audio")
    }
  }

  // Function to handle navigating to sign in page
  function handleSignIn() {
    goto("/login");
  }
</script>

<body>
  <div class="flex justify-center items-center justify-between border-b h-20">
    <div class="px-8 m">
      <button on:click={() => handleGoHome()}>
        <img class="h-12" src={kmpIcon} alt="KMP Icon" />
      </button>
    </div>

    <div class="px-8 flex">
      <div>
        {#if (email)} <!-- Check if email is available -->
          <button on:click={() => toggleDropdown()}>
            <div class="flex justify-center items-center px-8">
              <img class="h-6" src={profileIcons[currentIconIndex]} alt="Profile Icon" />
            </div>
          </button>

          {#if showDropdown}
            <div class="w-fit absolute bg-white shadow right-16 py-2 rounded-lg z-50">
              <div class="text-left w-fit py-2 rounded-lg">
                <div class="text-gray-500 text-base px-5 pb-2 w-full">
                  {email} <!-- Show the logged-in user's email -->
                </div>
                <div class="w-full border-t border-gray-100"></div>
                <div class="flex w-full float-start items-start justify-start pt-3 pb-1 px-3">
                  <button class="hover:bg-gray-100 rounded-lg font-sans justify-center items-center flex w-full h-8" on:click={() => handleLogout()}>
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
