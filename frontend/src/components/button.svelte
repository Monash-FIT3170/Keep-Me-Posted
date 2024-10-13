<!-- Button Component

    Contains modifiable button

    Author: Diya Ramesh, Brenda Dang, Benjamin Cherian
    Last modified: 13/10/2024

-->

<script>
    export let type = 'primary';
    export let handleClick = () => {};
    export let icon = ''; // Default empty string for icon URL
    export let iconSvg = ''; // Default empty string for inline SVG
    export let iconPos = 'left'; // Default icon position is on left of the button
    export let text = 'Button';
    export let altText = '';
    export let fullWidth = false; // Default to false for not full width
    export let minHeight = 11;
    export let fitContainerHeight = false; // New prop to fit container height
    export let disabled = false;
    let originalType = type;
    export let loading = false;


    // Internal handleClick function that calls the passed handleClick prop
    function internalHandleClick() {
        handleClick();
    }

    export function toggleDisabled() {
        if (type == 'disabled') {
            type = originalType;
        } else {
            type = 'disabled';
        }
    }

    export function replaceIcon(newIconPath) {
        icon = newIconPath;
    }

</script>

<div class="flex justify-center sm:justify-start h-full">
    <button 
        class="flex items-center justify-center font-sans rounded-lg px-3 py-2.5 md:px-4 md:py-2.5 lg:px-5 lg:py-2.5 transition ease-in-out duration-300 min-h-{minHeight}
        {type === 'primary' ? 'bg-blue-600 text-white hover:bg-blue-800 border-none' : ''}
        {type === 'secondary' ? 'bg-blue-50 text-blue-700 hover:bg-blue-100 border-none' : ''}
        {type === 'secondary-with-border' ? 'bg-blue-50 text-blue-700 hover:bg-blue-100 border-blue-600 border-2' : ''}
        {type === 'tertiary' ? 'bg-white text-gray-800 border-[1px] border-gray-300 hover:bg-gray-300' : ''}
        {type === 'disabled' ? 'bg-gray-200 text-white cursor-not-allowed border-none' : ''}
        {type === 'error' ? 'bg-red-600 text-white border-none' : ''}
        {type === 'no-bg' ? '' : ''}
        {fullWidth ? 'w-full text-center' : ''}
        {fitContainerHeight ? 'h-full' : ''}"
        on:click={internalHandleClick}
        disabled={disabled}>

        {#if loading}
            <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="#7d7d7d" stroke-width="4"></circle>
                <path class="opacity-35" fill="#6a6a6a" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            {text}
        {:else}
            {#if iconPos === 'right'}
                {text}
            {/if}

            {#if icon}

                {#if text === ''}
                    <!-- svelte-ignore a11y-missing-attribute -->
                    <img src="{icon}" class="max-w-4 md:max-w-5 lg:max-w-6"> <!-- no margin if only icon-->
                {:else}
                    <img src="{icon}" alt='icon' class="max-w-4 md:max-w-5 lg:max-w-6
                    {iconPos === 'left' ? "mr-2" : ""}
                    {iconPos === 'right' ? "ml-2" : ""}">
                {/if}
            {:else if iconSvg}
                <!-- svelte-ignore a11y-missing-attribute -->
                <div src="{icon}" class="sm:mr-2 lg:mr-6 2xl:mr-[2vw] max-w-6
                {iconPos === 'left' ? "mr-2" : ""}
                {iconPos === 'right' ? "ml-2" : ""}">
                    {@html iconSvg}
                </div>
            {/if}

            {#if iconPos === 'left'}
                {text}
            {/if}
        {/if}
        <slot>{altText}</slot> <!-- alternative text for if the button needs to be resized-->
    </button>
</div>