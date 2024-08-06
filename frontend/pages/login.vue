<template>
    <div class="h-screen w-screen flex justify-center items-center dark:bg-gray-900">
      <div class="grid gap-8">
        <div id="back-div" class="bg-gradient-to-r from-blue-500 to-purple-500 rounded-[25px] m-4">
          <div class="border-[20px] border-transparent rounded-[20px] dark:bg-gray-900 bg-white shadow-lg xl:p-10 2xl:p-10 lg:p-10 md:p-10 sm:p-2 m-2">
            <h1 class="pt-8 pb-6 font-bold dark:text-gray-400 text-5xl text-center cursor-default">
              Log in
            </h1>
            <Form @submit.prevent="login" class="space-y-4">
              <div>
                <label for="email" class="mb-2 dark:text-gray-400">Email</label>
                <InputText
                  id="email"
                  v-model="email"
                  class="w-full placeholder:text-base "
                  type="email"
                  placeholder="Email"
                  required
                />
              </div>
              <div>
                <label for="password" class="mb-2 dark:text-gray-400">Password</label>
                <Password
                  id="password"
                  v-model="password"
                  class="w-full placeholder:text-base"
                  placeholder="Password"
                  feedback="false"
                  toggleMask
                />
              </div>
              <a class="group text-blue-400 transition-all duration-100 ease-in-out" href="#">
                <span class="bg-left-bottom bg-gradient-to-r text-sm from-blue-400 to-blue-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out">
                  Forget your password?
                </span>
              </a>
              <Button
                class="bg-gradient-to-r dark:text-gray-300 from-blue-500 to-purple-500 shadow-lg mt-6 p-2 text-white rounded-lg w-full hover:scale-105 hover:from-purple-500 hover:to-blue-500 transition duration-300 ease-in-out"
                type="submit"
                label="LOG IN"
              />
            </Form>
            <div class="flex flex-col mt-4 items-center justify-center text-sm">
              <h3 class="dark:text-gray-300">
                Don't have an account?
                <NuxtLink to="/signup" class="group text-blue-400 transition-all duration-100 ease-in-out">
                    <span class="bg-left-bottom bg-gradient-to-r from-blue-400 to-blue-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out">
                        Sign Up
                    </span>
                </NuxtLink>
              </h3>
            </div>
            <!-- Third Party Authentication Options -->
            <ThirdPartyAuthButtons @thirdPartyAuth="thirdPartyAuth" />
            <div class="text-gray-500 flex text-center flex-col mt-4 items-center text-sm">
              <p class="cursor-default">
                By signing in, you agree to our
                <a class="group text-blue-400 transition-all duration-100 ease-in-out" href="#">
                  <span class="cursor-pointer bg-left-bottom bg-gradient-to-r from-blue-400 to-blue-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out">
                    Terms
                  </span>
                </a>
                and
                <a class="group text-blue-400 transition-all duration-100 ease-in-out" href="#">
                  <span class="cursor-pointer bg-left-bottom bg-gradient-to-r from-blue-400 to-blue-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out">
                    Privacy Policy
                  </span>
                </a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
<script setup>

import ThirdPartyAuthButtons from '@/components/auth/ThirdPartyAuthButtons.vue';

const { $userStore } = useNuxtApp();

const email = ref(null);
const password = ref(null);


const login = async () => {
  try {
    await $userStore.login(email.value, password.value);
    await $userStore.getUser();
  } catch (error) {
    console.log('error', error);
  }
};

const thirdPartyAuth = (provider) => {
    
  console.log(`Third-party auth with ${provider}`);
  // Add third-party auth logic here
};

</script>
