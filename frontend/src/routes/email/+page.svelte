<script>
    let postRequestString = "http://localhost:8000/emailer/"  // yours may be different, see what link pops up when you run django server, then add /emailer on the end
    let contacts = []
    let contents = ""
    let emailField = ""

    let buttonPressed = () => {
        let data = new FormData()
        data.append('contents', contents)
        data.append('contacts', contacts)
            
        fetch(postRequestString, {method: 'POST', data: data}).then(response => {
            console.log(response)
        })
    }
    /**
     * This function is used to remove the email from the array and display when the user clicks the delete
     * @param index
     */
    let remove_email= (index)=> {
        contacts.splice(index, 1)
        contacts = contacts
    }

    /**
     * add_email function is for displaying the user emails in the display field and for adding the user to the contact array
     */
    let add_email = () =>{
        contacts.push(emailField)
        emailField = ""
        contacts = contacts
    }

    
</script>


<!-- This link is currently used for using google material icons-->
<link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">

      <!-- this style heading class is for making the "Add Recepients" heading centered in the page-->
<style>
    .heading{
        text-align: center;
    }

    ul {
        list-style-type: none;
    }   

    .email {
        display: flex;
        justify-content: center;
    }

</style>

<br>

<div class="heading">Add Receipents<br><br><br><br><br><br>
<!-- Below is HTML code for the input field and add button-->
<label for = "email">Enter User Email Address:</label>
<input placeholder = "test@example.com" bind:value={emailField}>

<!-- on click the add button calls the add_email function-->
<button on:click={add_email}>Add +</button><br><br><br><br><br>

<!-- loops through each contact and prints -->
<ul>
    {#each contacts as email, index (index)}
    <div class="email"><li>{email}</li> <button on:click={remove_email(index)}>-</button></div>
    {/each}
</ul>



<div id="display" >

</div>
</div>