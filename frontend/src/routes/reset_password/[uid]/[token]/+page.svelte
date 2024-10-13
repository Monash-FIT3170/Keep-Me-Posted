<script>
  import { reset_password } from "../../../../api-functions/reset_password";
  import { backendURL } from "../../../../api-functions/base-URL";
  import { goto } from "$app/navigation";
  import { page } from "$app/stores";
  import LandingPageTitle from "../../../../components/landingPageTitle.svelte";
  import InputFieldWithValidation from "../../../../components/input-field-with-validation.svelte";
  import LoginCardHeader from "../../../../components/loginCardHeader.svelte";
  import Button from "../../../../components/button.svelte";
  import Logo from "../../../../components/logo.svelte";

  $: uid = $page.params.uid;
  $: token = $page.params.token;

  let password1 = "";
  let password2 = "";
  let errorMessage = "";
  let passwordValidationString = "";
  let passwordValidationActive = false;
  let passwordResetSuccess = false;

  let resetPassword = async () => {
    const passwordRegex =
      /^(?=.*[A-Z])(?=.*[!@#$%^&*()_+,\-.;:'"<>=?\/\[\]{}|`~])(?=.{8,})[a-zA-Z0-9!@#$%^&*()_+,\-.;:'"<>=?\/\[\]{}|`~]*$/;

    if (!passwordRegex.test(password1)) {
      errorMessage =
        "Password must contain at least 8 characters, capital letters, and a special character";
      console.log(errorMessage);
      return;
    }

    if (password1 !== password2) {
      errorMessage = "Passwords do not match";
      console.log(errorMessage);
      return;
    }

    let response = await reset_password(uid, token, password1, backendURL);

    if (response.status === 200) {
      errorMessage = "Password successfully reset";
      passwordResetSuccess = true;
      console.log(errorMessage);
    } else {
      errorMessage = "Password reset failed";
      console.log(errorMessage);
    }
  };

  let redirectToLogin = () => {
    goto("/login");
  };
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

    <div class="w-full md:w-1/2 flex justify-center items-center h-full">
      <div
        class="h-full w-full md:w-full lg:w-2/3 flex justify-center items-center"
      >
        <div
          class="py-10 px-16 h-full md:h-3/4 lg:h-3/4 w-full sm:w-3/4 md:w-4/5 rounded-[16px] bg-white md:min-w-full lg:min-w-[450px] md:min-h-[635px] lg:min-h-[635px] ml-0 md:ml-16 mr-0 md:mr-16 max-h-[700px]"
        >
          <!-- Content here -->
          {#if passwordResetSuccess}
            <div class="w-full h-full">
              <LoginCardHeader
                heading="Create New Password"
                subheading="Please enter your new password"
              />

              <div id="password-input">
                <InputFieldWithValidation
                  label="Password"
                  isPasswordType={true}
                  placeholder="••••••••"
                  bind:value={password1}
                  validationMessage={passwordValidationString}
                  validationActive={passwordValidationActive}
                />
              </div>
              <div id="password-input">
                <InputFieldWithValidation
                  label="Password"
                  isPasswordType={true}
                  placeholder="••••••••"
                  bind:value={password2}
                  validationMessage={passwordValidationString}
                  validationActive={passwordValidationActive}
                />
              </div>

              <div id="reset-button" class="w-full h-[45px] mb-4">
                <Button
                  fullWidth={true}
                  fitContainerHeight={true}
                  type="primary"
                  text="Reset Password"
                  handleClick={resetPassword}
                />
              </div>
            </div>
          {:else}
            <LoginCardHeader
              heading="Password Reset Success"
              subheading="You can now go back to the login page and sign in with your new password."
            />
            <div class="h-11">
              <Button
                fullWidth={true}
                fitContainerHeight={false}
                type="primary"
                text="Back To Login"
                handleClick={redirectToLogin}
              />
            </div>
          {/if}
        </div>
      </div>
    </div>
  </div>
</div>
