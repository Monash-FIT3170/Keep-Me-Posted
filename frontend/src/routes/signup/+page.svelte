<!-- SignUp Page

    Page that is used for user to sign up a new account to the application

    Author: Rohit
    Last Modified: 6/08/2024
-->
<script>
  import { onMount } from "svelte";
  import { goto } from "$app/navigation";
  import Logo from "../../components/logo.svelte";
  import LandingPageTitle from "../../components/landingPageTitle.svelte";
  import InputFieldWithValidation from "../../components/input-field-with-validation.svelte";
  import LoginCardHeader from "../../components/loginCardHeader.svelte";
  import Button from "../../components/button.svelte";
  import LoginPrompt from "../../components/loginPrompt.svelte";
  import { backendURL } from "../../api-functions/base-URL";

  let googleIcon = `<svg
              xmlns="http://www.w3.org/2000/svg"
              x="0px"
              y="0px"
              width="4vw"
              height="3vh"
              viewBox="0 0 48 48"
            >
              <path
                fill="#FFC107"
                d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"
              ></path>
              <path
                fill="#FF3D00"
                d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"
              ></path>
              <path
                fill="#4CAF50"
                d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"
              ></path>
              <path
                fill="#1976D2"
                d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"
              ></path>
            </svg>`;

  let email = "";
  let password = "";
  let verifyPassword = "";
  let emailValidationString = "";
  let passwordValidationString =
    "Password must contain at least 8 characters, capital letters, and a special character";
  let verifyPasswordValidationString = "";
  let emailValidationActive = false;
  let passwordValidationActive = false;
  let verifyPasswordValidationActive = false;

  function handleKeydown(event) {
    if (event.key === "Enter") {
      handleSignUp(); 
    }
  }

  function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  function isValidPassword(password) {
    const passwordRegex =
      /^(?=.*[A-Z])(?=.*[!@#$%^&*()_+,\-.;:'"<>=?\/\[\]{}|`~])(?=.{8,})[a-zA-Z0-9!@#$%^&*()_+,\-.;:'"<>=?\/\[\]{}|`~]*$/;
    return passwordRegex.test(password);
  }

  function emailValidation(email) {
    if (email == "") {
      emailValidationString = "Please Enter Email";
      emailValidationActive = true;
      return false;
    } else if (!isValidEmail(email)) {
      emailValidationString = "Please Enter Valid Email";
      emailValidationActive = true;
      return false;
    } else {
      emailValidationString = "";
      emailValidationActive = false;
      return true;
    }
  }

  function passwordValidation(password) {
    if (password == "" || !isValidPassword(password)) {
      passwordValidationActive = true;
      return false;
    } else {
      passwordValidationActive = false;
      return true;
    }
  }

  function verifyPasswordValidation(password, verifyPassword) {
    if (verifyPassword == "") {
      verifyPasswordValidationString = "Please Enter Password";
      verifyPasswordValidationActive = true;
      return false;
    } else if (verifyPassword != password) {
      verifyPasswordValidationString = "Password does not match";
      verifyPasswordValidationActive = true;
      return false;
    } else {
      verifyPasswordValidationString = "";
      verifyPasswordValidationActive = false;
      return true;
    }
  }

  function handleEmailInUse(response) {
    if ((response.error = "This email address is already in use")) {
      emailValidationString = response["error"];
      emailValidationActive = true;
    }
  }

  async function handleSignUp() {
    console.log("Email:", email);
    console.log("Password:", password);
    console.log("VerifyPassword", verifyPassword);

    if (
      emailValidation(email) &
      passwordValidation(password) &
      verifyPasswordValidation(password, verifyPassword)
    ) {
      const data = { username: email, password: password, email: email };
      const response = await postData(data);
      handleEmailInUse(response);
    }
  }

  // Optional: Fetch initial data or perform other tasks on component mount
  onMount(async () => {
    // Fetch initial data or perform other async tasks here
  });

  async function postData(signUpData) {
    try {
      const url = backendURL + "/signup";
      const data = signUpData;

      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const responseData = await response.json();
      console.log("Response:", responseData);

      if (response.ok) {
        goto("/login");
      }
      return responseData;
    } catch (error) {
      console.error("Error:", error);
    }
  }

  function handleLogInClick() {
    goto("/login");
  }
</script>

<div
  class="m-0 h-screen bg-gradient-to-l from-[#53b1fd] to-[#1570ef] flex justify-center items-center text-white"
>
  <div class="flex flex-col md:flex-row h-screen w-full">
    <!-- Top Row on Mobile / Left Column on Desktop -->
    <div class="flex md:flex-col w-full md:w-1/2">
      <div class="ml-0 sm:ml-24 md:ml-0 w-1/4 md:w-full md:flex-1">
        <div
          class=" ml-4 p-4 sm:p-6 md:p-0 mt-1 md:mt-0 min-w-[100%] md:min-w-[150px] ml-0 md:ml-40 h-full w-1/5 flex flex-col justify-end md:justify-end"
        >
          <Logo class="mt-auto" />
        </div>
      </div>
      <div class="w-3/4 md:w-full md:flex-1 flex items-center md:items-start">
        <div class="ml-4 md:ml-40 mt-2 md:mt-4 mb-0">
          <LandingPageTitle
            title="Keep Me Posted"
            subTitle="Your AI Powered Meeting Companion."
          />
        </div>
      </div>
    </div>
    <!-- Bottom Row on Mobile / Right Column on Desktop -->
    <div class="w-full md:w-1/2 flex justify-center items-center h-full">
      <div
        class="h-full w-full md:w-full lg:w-2/3 flex justify-center items-center"
      >
        <div
          class="py-10 px-16 h-full md:h-3/4 lg:h-3/4 w-full sm:w-3/4 md:w-4/5 rounded-[16px] bg-white md:min-w-full lg:min-w-[450px] md:min-h-[635px] lg:min-h-[635px] ml-0 md:ml-16 mr-0 md:mr-16 max-h-[700px]"
        >
          <!-- Content here -->
          <LoginCardHeader heading="Sign Up" subheading="Create an account!" />

          <InputFieldWithValidation
            label="Email"
            placeholder="name@email.com"
            bind:value={email}
            validationMessage={emailValidationString}
            validationActive={emailValidationActive}
          />

          <InputFieldWithValidation
            label="Password"
            isPasswordType={true}
            placeholder="••••••••"
            bind:value={password}
            validationMessage={passwordValidationString}
            validationActive={passwordValidationActive}
            showValidation={true}
          />

          <InputFieldWithValidation
            label="Verify Password"
            isPasswordType={true}
            placeholder="••••••••"
            bind:value={verifyPassword}
            validationMessage={verifyPasswordValidationString}
            validationActive={verifyPasswordValidationActive}
            onKeydown={handleKeydown}
          />

          <div class="w-full h-[45px] mb-4 mt-8">
            <Button
              fullWidth={true}
              fitContainerHeight={true}
              type="primary"
              text="Sign Up"
              handleClick={handleSignUp}
            />
          </div>

          <div>
            <form class="w-full h-[45px] mb-4" method="post" action="?/OAuth2">
              <Button
                fullWidth={true}
                fitContainerHeight={true}
                type="tertiary"
                text="Sign Up with Google"
                iconSvg={googleIcon}
              />
            </form>
          </div>

          <div class="w-full flex justify-center">
            <LoginPrompt
              text="Already have an account?"
              linkText="Log In"
              isPrimary={false}
              handleClick={handleLogInClick}
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
