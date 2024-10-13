<script>
  import { goto } from "$app/navigation";
  import { request_reset_password } from "../../api-functions/request_reset_password";

  import Logo from "../../components/logo.svelte";
  import LandingPageTitle from "../../components/landingPageTitle.svelte";
  import InputFieldWithValidation from "../../components/input-field-with-validation.svelte";
  import LoginCardHeader from "../../components/loginCardHeader.svelte";
  import Button from "../../components/button.svelte";
  import { backendURL, frontendURL } from "../../api-functions/base-URL";

  let message = "";
  let email = "";

  let requestPasswordReset = async () => {
    if (email == "") {
      emailValidationString = "Please Enter Email";
      emailValidationActive = true;
      return false;
    } 
    else if (!isValidEmail(email)) {
      emailValidationString = "Please Enter Valid Email";
      emailValidationActive = true;
      return false;
    }
    else
    {
      message ="If you have an existing account, a reset link will be sent to you.";
      await request_reset_password(email, backendURL, frontendURL);
    }
  };

  let emailValidationString = "";

  let emailValidationActive = false;

  function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
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
          class="p-4 sm:p-6 md:p-0 mt-1 md:mt-0 min-w-[100%] md:min-w-[150px] ml-0 md:ml-40 h-full w-1/5 flex flex-col justify-end md:justify-end"
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
    <div
      class="w-full md:w-1/2 flex flex-col justify-center items-center h-full"
    >
      <div
        class="h-full w-full md:w-full lg:w-2/3 flex justify-center items-center"
      >
        <div
          class="py-10 px-16 h-full md:h-3/4 lg:h-3/4 w-full sm:w-3/4 md:w-4/5 rounded-[16px] bg-white md:min-w-full lg:min-w-[450px] md:min-h-[635px] lg:min-h-[635px] ml-0 md:ml-16 mr-0 md:mr-16 max-h-[700px]"
        >
          <!-- Content here -->
          <div class="w-full h-full">
            <LoginCardHeader
              heading="Forgot Password"
              subheading="Please enter your email to receive link for resetting password"
            />
            <div id="email-input">
              <InputFieldWithValidation
                label="Email"
                placeholder="name@email.com"
                bind:value={email}
                validationMessage={emailValidationString}
                validationActive={emailValidationActive}
              />
            </div>

            <div id="forgot-button" class="w-full h-[45px] mb-4">
              <Button
                fullWidth={true}
                fitContainerHeight={true}
                type="primary"
                text="Send Link"
                handleClick={requestPasswordReset}
              />
            </div>
            <div class="text-[#667085] text-sm font-inter font-[350] mb-6">
              {message}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
