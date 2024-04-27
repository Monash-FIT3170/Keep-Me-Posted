<script>

    let postRequestString = "http://localhost:8000/emailer/"  // yours may be different, see what link pops up when you run django server, then add /emailer on the end
    let contacts = []
    let contents = ""
    let emailField = ""
    let errorMessage = ""

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
        if(!emailField.trim()){
            //This is to display error message when inputfield is empty
            errorMessage = 'Please enter email address.';
            // Clear error message after 2 seconds
            setTimeout(() => {
                errorMessage = '';
            }, 2000);
        }
        else{
            //if input field is not empty then it will be pushed to the contacts list
            contacts.push(emailField)
            emailField = ""
            contacts = contacts
        }
        
    }

    
</script>


<!-- This link is currently used for using google material icons-->
<link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">

      <!-- this styling secton contains styles for many components used throughout the page-->
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
    
    .error {
        color: red;
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
    }

</style>

<br>
<!--If an error message is triggered the error message is displayed-->
{#if errorMessage}
<p class="error">{errorMessage}</p>
{/if}


<div class="heading">Add Receipents<br><br><br><br><br><br>
<!-- Below is HTML code for the input field and add button-->
<label for = "email">Enter User Email Address:</label>
<input placeholder = "test@example.com" bind:value={emailField}>


<!-- on click the add button calls the add_email function-->
<button on:click={add_email}>Add +</button><br><br><br><br><br>

<!-- loops through each contact and prints -->
<ul>
    {#each contacts as email, index (index)}
    <div class="email" style="margin-top:10px;"><li>{email}</li><button style="border-radius:50px; border:3px lightGrey; cursor:pointer;background-color:lightblue;" on:click={remove_email(index)}>-</button></div>
    {/each}
</ul>


<div id="display" >

</div>
</div>