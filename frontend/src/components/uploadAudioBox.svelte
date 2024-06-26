<!--

    Upload Audio Box Component

    Authors: Parul Garg (pgar0011)
    Editied by: Benjamin Cherian, Zihao Wang, Angelina Leung
    Last Modified: 13/05/24

-->
<!-- JavaScript -->
<script>
  import micIcon from "../assets/mic-icon.png";
  import uploadIcon from "../assets/upload-icon.png";
  import radioIcon from "../assets/radio-icon.png";
  import fileIcon from "../assets/file-icon.png";
  import Dropzone from "svelte-file-dropzone";
  import { simple_pathway } from "../api-functions/simple_pathway";
  import { api_status } from "../stores/simple-pathway-store";
  import { goto } from "$app/navigation";
  export let simple = false;

  const unsubscribe = api_status.subscribe((value) => {
    console.log(value.status); // Log the status value
    updateLoadingBar(value.status);
  });

  function updateLoadingBar(api_status) {
    if (api_status == "Transcribe") {
      updateUploadBoxContents("Transcribing audio", false);
      currentProgress = 0.4;
      makeProgression();

      setTimeout(() => {
        currentProgress = 0.55;
        makeProgression();
      }, 8000);

    } else if (api_status == "Summary") {
      updateUploadBoxContents("Generating summary", true);
      currentProgress = 0.7;
      makeProgression();

    } else if (api_status == "Email") {
      updateUploadBoxContents("Sending email", true);
      currentProgress = 0.9;
      makeProgression();

    } else if (api_status == "Complete") {
      currentProgress = 0.99;
      makeProgression();
      setTimeout(() => {
        goto("/sent");
      }, 2500);
      
    }
  }

  // ------------------------------------------ Progress Bar
  let progressBarWidth = 0;
  let progressBarProgress;
  let progressBarDisplay = 0;
  let loadingBarWidth;
  let progressBarMax = 1;
  let currentProgress = 0;

  $: switch (progressBarWidth) {
    case Math.round(loadingBarWidth * progressBarMax):
      clearInterval(progressBarProgress);
  }

  const progression = () => {
    if (progressBarWidth < currentProgress * loadingBarWidth) {
      progressBarWidth += 1;
      progressBarDisplay = Math.round(
        (progressBarWidth / loadingBarWidth) * 100,
      );
    }
  };

  const makeProgression = () => {
    loadingBarWidth = document.getElementById("loadingBar").clientWidth;
    document.getElementById("loadingBar").style.visibility = "visible";
    document.getElementById("progressNumber").style.visibility = "visible";
    progressBarProgress = setInterval(progression, 10);

    return true;
  };
  const MAX_DURATION_SECONDS = 7200; // 7200 seconds = 120 minutes

  var ICON_DICT = {
    "Uploading meeting audio": uploadIcon,
    "Transcribing audio": radioIcon,
    "Generating summary": fileIcon,
    "Sending email": fileIcon,
  };

  // ------------------------------------------ File Handling
  let file;
  let errorMessage = "";

  async function handleFilesSelect(e) {
    const { acceptedFiles } = e.detail;
    file = null; // Reset the file each time new files are selected

    if (acceptedFiles.length > 0) {
      const selectedFile = acceptedFiles[0];

      // Initial file type check before loading it as an audio source
      if (
        !selectedFile.name.endsWith(".mp3") &&
        !selectedFile.name.endsWith(".wav")
      ) {
        errorMessage =
          "Invalid audio format! \n Your meeting audio must be in MP3 or WAV format.";
        return; // Exit the function early if file type is incorrect
      }

      const audio = new Audio(URL.createObjectURL(selectedFile)); // Create new Audio HTML object, create URL used as source for audio element

      audio.addEventListener("loadedmetadata", async () => {
        if (audio.duration <= MAX_DURATION_SECONDS) {
          file = selectedFile;
          errorMessage = "";
          console.log("mao");
          const response = await simple_pathway(file, "http://127.0.0.1:8000");
        } else {
          errorMessage =
            "Meeting duration exceeded! \n Your meeting audio should be less than 120 minutes.";
          file = null;
          //TODO: Replace with error message pop-up
        }
      });
    } else {
      errorMessage =
        "Invalid audio format! Your meeting audio must be in MP3 or WAV format";
    }
  }

  // ------------------------------------------ Box Contents
  // changes the contents of the audio box
  function updateUploadBoxContents(newText, isProgression) {
    var firstLine = document.querySelector(".first-line");
    // changeClass('.first-line', '.loading-line')
    firstLine.textContent = newText + "...";

    if (isProgression) {
      // Change icon source
      var icon = document.getElementById("icon");
      icon.src = ICON_DICT[newText];
    } else {
      var secondLine = document.querySelector(".second-line");
      changeClass(".second-line", "loading-line");
      secondLine.textContent = "";

      // Change icon source
      var icon = document.querySelector(".large-icon");
      icon.src = ICON_DICT[newText];
      changeClass(".large-icon", ".small-icon");
    }

    // when a file is dragged in show the loading bar and 'Uploading meeting audio'
    // when file is sent to assemblyai; show 'Transcribing audio'
    // when file is sent to gemini; show 'Generating Summary'
    // when file is sent to assemblyai; show 'transcribing audio'
  }

  function changeClass(elemId, newClassName) {
    // Get the span element by its ID
    const spanElement = document.querySelector(elemId);

    // Remove any existing class from the span element
    if (spanElement != null) {
      spanElement.className = "";

      // Add the new class to the span element
      spanElement.classList.add(newClassName);
    }
  }
</script>

<!-- COMPONENT -->
<div class="upload-box">
  <label for="uploadAudioBox" class="custom-input">
    <Dropzone on:drop={handleFilesSelect} accept=".mp3, .wav">
      <!-- The dropzone is on top of custom-input so the grey is covering the lightblue-->
      <img id="icon" class="large-icon" src={micIcon} alt="Icon" />
      <span class="first-line">Upload meeting audio</span>
      <span class="second-line"
        >Must be under 120 minutes. MP3 or WAV formats accepted.</span
      >

      <div id="loadingBar">
        <div id="progressBar" style="width: {progressBarWidth}px"></div>
      </div>
      <div id="progressNumber"><b>{progressBarDisplay}</b>%</div>
    </Dropzone>
  </label>
</div>

<div class="status-message">
  {#if file}
    <p>File ready: {file.name}</p>
  {:else}
    <p>{errorMessage}</p>
  {/if}
</div>

<!-- Styling -->
<style>
  .upload-box {
    display: flex;
    justify-content: center;
  }

  .large-icon {
    /* large icon */

    width: 3.5vw;
    height: calc(2 * width);

    max-width: 46px;
    max-height: 52px;

    /* Inside auto layout */
    flex: none;
    order: 0;
    flex-grow: 0;
  }

  /* Not on inital load in */
  .small-icon {
    /* small icon */

    width: 30px;
    height: 30px;

    /* Inside auto layout */
    flex: none;
    order: 0;
    flex-grow: 0;
  }

  .custom-input {
    /* Upload Audio Box */

    box-sizing: border-box;

    /* Auto layout */
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 0px 0px;
    gap: 16px;

    width: 55vw;
    height: 27vh;
    max-width: 700px;
    max-height: 233px;

    /* Blue/25 */
    background: #f5faff;
    /* Blue/300 */
    border: 3px solid #84caff;
    border-radius: 5px;

    /* Inside auto layout */
    flex: none;
    order: 0;
    flex-grow: 0;
  }

  .first-line {
    /* Upload meeting audio */
    width: 25vw;
    height: 5vh;

    /* Text xl/Medium */
    font-style: normal;
    font-family: "Inter";
    font-weight: 500;
    font-size: 1.45vw;
    line-height: 5vh;
    /* identical to box height, or 150% */
    text-align: center;

    /* Blue/800 */
    color: #1849a9;

    /* Inside auto layout */
    flex: none;
    order: 0;
    flex-grow: 0;
  }

  .second-line {
    /* Must be under 120 minutes. MP3 or WAV formats accepted. */

    width: 16.5vw;
    height: 5vh;

    /* Text md/Regular */
    font-style: normal;
    font-weight: 400;
    font-size: 1.1vw;
    line-height: 4vh;
    /* or 150% */
    text-align: center;

    /* Gray/400 */
    color: #98a2b3;

    /* Inside auto layout */
    flex: none;
    order: 1;
    flex-grow: 0;
  }

  /* Not on inital load in */
  .loading-line {
    /* 
  /* Auto layout */
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0px;
    gap: 4px;

    width: 256px;
    height: 30px;

    /* Inside auto layout */
    flex: none;
    order: 1;
    flex-grow: 0;
  }

  .status-message {
    text-align: center;
    padding: 10px;
    color: #333;
    font-size: 16px;
    margin-top: 100px;
  }

  #loadingBar {
    top: 57%;
    visibility: hidden;
    border: 1px solid;
    position: absolute;
    margin-top: 67px;
    width: 35vw;
    height: 10px;
    background-color: #e9eaec;
    border-radius: 30px 30px 30px 30px;
    border-color: #e9eaec;
  }

  #progressBar {
    position: relative;
    height: 10px;
    background-color: #1570ef;
    border-radius: 30px 30px 30px 30px;
  }

  #progressNumber {
    color: rgb(105, 104, 104);
    visibility: hidden;
    font-size: 14px;
    left: 19vw;
    top: 2.8vh;
    position: relative;
  }
</style>
