<!-- Input Field Component

    Contains modifiable input field

    Author: Alex Ung
    Last modified: 12/05/2024

-->

<!--  -->
<script>
    export let input = '';

    export let width = '100%'// Default width set to 100%, but it can be overridden when the component is used.
  </script>
  
  <input type="text" bind:value={input} placeholder="Enter text here" class="input-field" style="width: {width};"/>
  
  <style>
    .input-field {
      width: 100%; /* Adjust width as needed */
      padding: 8px 12px;
      font-size: 16px;
      border: 1px solid #cccccc; /* Light grey border */
      border-radius: 5px; /* Rounded corners */
      box-shadow: none; /* No shadow for a flat design */
      outline: none; /* Removes the default focus outline */
    }
  
    .input-field:focus {
      border-color: #888; /* Darker border when focused */
    }
  </style>
  