<!-- Top Bar Navigation Component

    Enables settings and profile on-click

    Author: mpha0039
    Edited by: dleu0007
    Last modified: 9/05/2024

 -->

<script>
  import TopBar from "../components/topbar.svelte";
  import { goto } from "$app/navigation";
  
</script>
<button on:click = {goto("/login")}></button>
<TopBar />

