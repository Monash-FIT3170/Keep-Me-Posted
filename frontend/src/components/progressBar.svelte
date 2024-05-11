<!-- Button Component

    Progress Bar

    Author: Zihao Wang
    Last modified: 11/05/2024

-->

<!--  -->

<script>
    import { Progressbar, Button } from 'flowbite-svelte';
    import { sineOut } from 'svelte/easing';
  
    let progress = '0'

    let progressBarWidth = 0
    let progressBarProgress

    $: if (progressBarWidth === 100) {
      clearInterval(progressBarProgress)
    }

    const progression = () => {
      progressBarWidth += 1;
    }

    const makeProgression = () => {
      progressBarWidth = 0;
      progressBarProgress = setInterval(progression, 20)
    }
  </script>
  
<div>
  <Progressbar
    progress={progress}
    animate=true
    precision={0}
    labelInside
    tweenDuration={2000}
    easing={sineOut}
    size="h-6"
    labelInsideClass="bg-blue-600 text-black-100 text-base font-medium text-center p-1 leading-none rounded-full"
  />

  <Button pill outline colour="yellow" on:click={() => (progress = `${Math.round(Math.random() * 100)}`)}>
    Randomize
  </Button>
</div>

<div>
  <div id="myProgress"/>
  <div id="myBar" style="width: {progressBarWidth}%"><b>{progressBarWidth}</b>%</div>
  <button id="progressButton" on:click = {() => (makeProgression())} >Hello</button>
</div>

<style>
  #myProgress {
  width: 100%;
  background-color: grey;
  border-radius: 30px 30px 30px 30px;
  position: absolute;
  margin-top:100px;
}

#myBar {
  width: 0%;
  height: 30px;
  background-color: blue;
  text-align: center;
  border-radius: 30px 30px 30px 30px;
  position: absolute;
  margin-top:100px;
}

#progressButton {
  background-color: blue;
  width: 100px;
  height: 50px;
  text-align: center;
  position: absolute;
  top:0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
  border-radius: 30px 30px 30px 30px;
}
</style>
