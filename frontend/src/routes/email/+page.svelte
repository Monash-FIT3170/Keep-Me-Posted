<script>
    let postRequestString = "http://localhost:8000/emailer/"  // yours may be different, see what link pops up when you run django server, then add /emailer on the end
    let contacts = []
    let contents = ""

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
     * @param emailsList
     * @param id
     */
    let remove_email= (emailsList, id)=> {
        emailsList.splice(id, 1)
        console.log(emailsList)
    }

    /**
     * add_email function is for displaying the user emails in the display field and for adding the user to the contact array
     */
    let add_email = () =>{
        //retreiving the email from the input field
        let emailInputField = document.getElementById("inputEmail");
        let email_to_display = ""
        contacts.push(emailInputField.value);
        
        let displayField = document.getElementById("display");
        if (contacts.length>0){

            let htmlDisplay = ``;

            htmlDisplay += `<div style='display: flex; flex-direction: column; align-items: center;'>`;
            for (let contact_index = 0; contact_index<contacts.length; contact_index++){
                htmlDisplay += `<div class='row' style="margin:10px;width:250px; height:25px; border:2px solid lightgrey; border-radius:60px; display: flex; justify-content: space-between;">`;
                email_to_display = contacts[contact_index]
                htmlDisplay += `<div class='contact'>` + email_to_display + `</div>`;
                htmlDisplay += `<button on:click={remove_email(contacts, '${contact_index}')} style = "border-radius:100px; cursor:pointer;"><i class = "material-icons" style = "font-size:15px;">remove</i></button>`
                htmlDisplay +=`</div>`;
            }
            htmlDisplay += `</div>`;
            displayField.innerHTML = htmlDisplay;
        }
        else{
            displayField.innerHTML = `No users added.`;
            
        }
        console.log(contacts)

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

</style>

<br>

<div class="heading">Add Receipents<br><br><br><br><br><br>
<!-- Below is HTML code for the input field and add button-->
<label for = "email">Enter User Email Address:</label>
<input id="inputEmail" placeholder = "test@example.com">
<!-- on click the add button calls the add_email function-->
<button on:click={add_email}>Add +</button><br><br><br><br><br>


<div id="display" >

</div>
</div>




