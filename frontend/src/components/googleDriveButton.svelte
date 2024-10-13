<!-- Google Drive Button Component

    Contains google file picker to allow users to upload files from their google drive

    Author: Ahmed Almasry, Maureen Pham
    Last modified: 14/09/2024

-->
<script>
    import { onMount } from "svelte";
    import Button from "./button.svelte";
    import { getAuth } from "../stores/auth-store";
    import DriveIcon from "../assets/google-drive.png";
    
    let pickerInited = false;
    let accessToken = null;
    let googleAuth = false;

    const API_KEY = "AIzaSyClx-X-RcNSLj88cdn7Mnnn60KVhnq5hvI";
    const APP_ID = "342252136789";

    function gapiLoaded() {
        console.log("Google API loaded");
        gapi.load("client:picker", initializePicker);
    }

    async function initializePicker() {
        await gapi.client.load(
            "https://www.googleapis.com/discovery/v1/apis/drive/v3/rest",
        );
        pickerInited = true;
    }

    onMount(async () => {
        const queryParams = new URLSearchParams(window.location.search);
        googleAuth = queryParams.get("google_auth") === "true";
        console.log("Google Auth:", googleAuth);

        if (googleAuth) {
            accessToken = getAuth().accessToken;
            console.log("Access Token:", accessToken);
        }

        const gapiScript = document.createElement("script");
        gapiScript.src = "https://apis.google.com/js/api.js";
        gapiScript.async = true;
        gapiScript.defer = true;
        gapiScript.onload = gapiLoaded;
        document.body.appendChild(gapiScript);

    });

    async function handleAuthClick() {
        accessToken = getAuth().accessToken; // pull token from store to prevent forbidden error message
        await createPicker();
    }

    /**
     *  Create and render a Picker object for searching images.
     */
    function createPicker() {
        console.log("Creating picker");
        const view = new google.picker.View(google.picker.ViewId.DOCS);
        view.setMimeTypes("audio/mpeg,video/mp4,audio/wav"); //displays the files shown in google picker
        const picker = new google.picker.PickerBuilder()
            .enableFeature(google.picker.Feature.NAV_HIDDEN)
            .enableFeature(google.picker.Feature.MULTISELECT_ENABLED)
            .setDeveloperKey(API_KEY)
            .setAppId(APP_ID)
            .setOAuthToken(accessToken)
            .addView(view)
            .addView(new google.picker.DocsUploadView())
            .setCallback(pickerCallback)
            .build();
        picker.setVisible(true);
    }

    /**
     * Displays the file details of the user's selection.
     * @param {object} data - Containers the user selection from the picker
     */
    async function pickerCallback(data) {
        console.log(data)
        if (data.action === google.picker.Action.PICKED) {
            let text = `Picker response: \n${JSON.stringify(data, null, 2)}\n`;
            const document = data[google.picker.Response.DOCUMENTS][0];
            const fileId = document[google.picker.Document.ID];
            const response = await fetch(`https://www.googleapis.com/drive/v3/files/${fileId}?alt=media`, {
                headers: new Headers({
                    Authorization: `Bearer ${accessToken}`, // pass in the token as an authorization header to access its google files
                }),
            });
            // storing the http request data(mp3/mp4) as a blob
            const blob = await response.blob();
            //converting blob to an actual file
            const file = new File([blob], document[google.picker.Document.NAME], { type: blob.type });

            // create event which will trigger the file handling in upload audio box
            const event = new CustomEvent("fileSelected", {
                detail: {acceptedFiles: [file] },
            }); 
            window.dispatchEvent(event);                
        }
    }


</script>


<div class="flex justify-center items-center h-[50px] mb-4">
    {#if googleAuth}
        <Button
            fullWidth={true} 
            fitContainerHeight={true}
            type="secondary" 
            text="Upload from Google Drive"
            icon = {DriveIcon}
            handleClick={handleAuthClick} />
    {:else}
        <form id="google-form" method="post" action="?/OAuth2">
            <Button
                fullWidth={true} 
                fitContainerHeight={true}
                type="secondary" 
                text="Upload from Google Drive"
                icon = {DriveIcon}
                handleClick={handleAuthClick} />
        </form>
    {/if}

    <p id="content" class="text-center"> </p>
</div>