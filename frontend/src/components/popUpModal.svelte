<!-- Pop-Up Modal Component

    Contains pop-up modal

    Author: Brenda Dang
    Modified by: Bowen Dong, Diya Ramesh
    Last modified: 9/08/2024

-->

<script>
  import Button from "./button.svelte";
  import errorIcon from "../assets/error-icon.png";
  import { Progressbar } from "flowbite-svelte";
  import { apiStatusStore } from "../stores/api-status-store";

  export let type = "primary"; // Default type is primary (blue with 1 button)
  export let firstHandleClick = () => {}; // Click function for primary button (dark blue, or red)
  export let secondHandleClick = () => {}; // Click function for secondary button (light blue)
  export let header = "Pop-Up Modal"; // Header of popup modal
  export let mainText = "This is a pop-up modal."; // Main text of popup modal
  export let firstButtonText = "Button"; // Text for primary button (dark blue, or red)
  export let secondButtonText = "Button"; // Text for secondary button (light blue)
  export let iconPath = ""; // path for image icon
  export let width = "64"; // default width of pop up
  export let visible = false; // Default state of popup is not visible

  const widthClasses = {
  '96': 'w-96',     // 24rem
  '80': 'w-80',     // 20rem
  '64': 'w-64',     // 16rem
  '48': 'w-48',     // 12rem
  'full': 'w-full', // 100%
  };

  export function togglePopUp() {
    visible = !visible;
  }

  export function getVisible() {
    return visible
  }

  let progress = 0
  let targetProgress = 100
  export function animateProgress() {
    const speed = 1; // Speed of animation
    if (progress < targetProgress) {
      if ($apiStatusStore == 'Cancel') {
        console.log("Progress reset");
        resetProgress();
        return;
      };
      progress += speed;
      if (progress >= targetProgress) {
        progress = targetProgress;
        return;
      }
      setTimeout(() => {
        animateProgress();
      }, 50);
    }
  }

  export function resetProgress() {
    progress = 0
  }
</script>

<body>
  {#if visible}
    <div
      class="justify-center items-center font-sans h-fulltransition ease-in-out duration-300 z-50"
    >
      <div
        class="fixed inset-0 flex items-center justify-center w-full h-full bg-black bg-opacity-50 backdrop-filter backdrop-blur-md"
      >
        <div class={`bg-white rounded-lg p-4 ${widthClasses[width]}`}>
          {#if iconPath}
            <div class="flex items-center justify-center pb-2">
              <img class="h-12" src={iconPath} alt="pop up icon" />
            </div>
          {:else if type === "error"}
            <div class="flex items-center justify-center pb-2">
              <img class="h-12" src={errorIcon} alt="error pop up icon" />
            </div>
          {/if}
          <div
            class="flex items-center justify-center text-gray-900 text-lg font-bold"
          >
            {header}
          </div>
          <div
            class="flex items-center justify-center text-gray-500 text-sm pt-2"
          >
            {mainText}
          </div>
          {#if type === "loading"}
            <div class="justify-center pb-1 pt-4 items-center w-full">
              <div class="pb-4">
                <Progressbar progress={progress} color="blue" />
              </div>
              <Button
                type="primary"
                text={firstButtonText}
                fullWidth={true}
                handleClick={firstHandleClick}
              />
            </div>
          {:else if type === "secondary"}
            <div
              class="flex shrink justify-evenly object-cover pb-1 pt-8 items-center"
            >
              <div class="w-5/12">
                <Button
                  type="secondary"
                  text={secondButtonText}
                  fullWidth={true}
                  handleClick={secondHandleClick}
                />
              </div>
              <div class="w-5/12">
                <Button
                  type="primary"
                  text={firstButtonText}
                  fullWidth={true}
                  handleClick={firstHandleClick}
                />
              </div>
            </div>
          {:else}
            <div class="justify-center pb-1 pt-8 items-center w-full">
              <Button
                type={type === "error" ? "error" : "primary"}
                text={firstButtonText}
                fullWidth={true}
                handleClick={firstHandleClick}
              />
            </div>
          {/if}
        </div>
      </div>
    </div>
  {/if}
</body>

<!--
    EXAMPLE USAGE FOR ERROR POP UP
<script>
    import TopBar from "../../components/topbar.svelte"
    import PopUpModal from "../../components/popUpModal.svelte";

    let popUpModalComponent;

    function togglePop() {
        popUpModalComponent.togglePopUp();
    }

</script>

<div>
    <TopBar />
    <button on:click={togglePop}>click to cause error</button>

</div>

<PopUpModal
  bind:this={popUpModalComponent}
  header="Regenerating..."
  mainText=""
  type="loading"
  firstHandleClick={togglePop}
/>
-->