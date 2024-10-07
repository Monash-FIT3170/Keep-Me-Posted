<!-- 

    The page where user uploads the audio file for Send Summary ASAP pathway.

    Author: Parul Garg (pgar0011)
    Edited By: Angelina Leung (aleu0007), Maureen Pham (mpha0039), Danny Leung (dleu0007), Rohit Valanki (rval0008)
    Last Modified: 1/10/2024 by Alex Ung

-->

<script>
  //required imports
  import Button from "../../components/button.svelte";
  import Topbar from "../../components/topbar.svelte";
  import Toggle from "../../components/toggle.svelte";
  import GoogleDriveButton from "../../components/googleDriveButton.svelte";
  import UploadBox from "../../components/uploadAudioBox.svelte";
  import { goto } from "$app/navigation";
  import { apiStatusStore } from "../../stores/api-status-store";
  import { navStatusStore } from "../../stores/nav-status-store";
  import { resetStores } from "../../stores/reset-store";
  import RightArrow from "../../assets/arrow-right.png";
  import { onMount, onDestroy } from "svelte";
  import { updateAuth, authStore } from "../../stores/auth-store.js";
  import PopUpModal from "../../components/popUpModal.svelte";

  let loggedIn;
  let googleAuth = false;
  let userEmail = null;
  let accessToken = null;
  let mailingList = []; // Add variable to hold mailing list

  // Subscribe to the store to get the current value of `loggedIn`
  const unsubscribe = authStore.subscribe((value) => {
    loggedIn = value.loggedIn;
  });
  // Clean up the subscription when the component is destroyed
  onDestroy(() => {
    unsubscribe();
  });

  onMount(async () => {
    const queryParams = new URLSearchParams(window.location.search);
    googleAuth = queryParams.get("google_auth") === "true";
    console.log("Google Auth:", googleAuth);

    if (!loggedIn && googleAuth) {
      try {
        const response = await fetch("/sse");

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        // Read the response body as a stream
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let result = "";

        // Read the stream
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          result += decoder.decode(value, { stream: true });
        }

        // Parse the JSON data
        const data = JSON.parse(result);
        userEmail = data.userEmail;
        accessToken = data.accessToken;
        mailingList = data.mailingList || []; // Handle mailing list

        // Update the store with the fetched data
        if (userEmail && accessToken) {
          updateAuth(userEmail, true, accessToken, mailingList); // Pass mailing list to updateAuth
        }

        console.log("Fetched user email:", userEmail);
        console.log("Fetched access token:", accessToken);
        console.log("Fetched mailing list:", mailingList);
      } catch (error) {
        console.error(
          "Error fetching user email, access token, and mailing list:",
          error,
        );
      }
    }
  });

  // Function to navigate to the summary page and update the status to "Viewed"
  let nextPage = () => {
    goto("/generate_summary");
    navStatusStore.set("Skipped");
  };

  // Function to handle re-upload action and reset the status
  function handleReUpload() {
    apiStatusStore.set("");
    resetStores();
  }

  let popUpModalComponent;
  let errorMessage = "Something went wrong, please try again!";

  function openPopUp() {
    if (popUpModalComponent) {
      popUpModalComponent.togglePopUp();
    }
  }
</script>

<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Upload Meeting Audio</title>
  </head>
  <body>
    <Topbar />
    <h1 class="mt-12">Upload Meeting Audio</h1>
    <div class="subheading mb-16 mt-4 px-2">
      Upload your meeting audio for us to summarise.
    </div>

    <UploadBox popUpModal = {popUpModalComponent}/>

    <GoogleDriveButton />

    <Toggle />

    {#if $apiStatusStore == "Complete"}
      <div class="flex justify-center items-center p-3">
        <Button
          type="secondary"
          text="Re-Upload Audio"
          handleClick={handleReUpload}
        />
      </div>
    {/if}

    <div class="absolute bottom-8 right-8">
      <Button
        handleClick={nextPage}
        icon={RightArrow}
        text="View Summary"
        disabled={$apiStatusStore == ""}
        type={$apiStatusStore == "" ? "disabled" : "primary"}
      ></Button>
    </div>
      <PopUpModal 
      bind:this={popUpModalComponent}
      header="Oops..."
      mainText={errorMessage}
      type='error'
      iconPath='../src/assets/error-icon.svg'
      firstButtonText="Close"
      firstHandleClick={openPopUp}
    />
  </body>
</html>
