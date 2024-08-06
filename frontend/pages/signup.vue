<!-- /pages/signup.vue -->
<template>
    <div class="h-screen w-screen flex justify-center items-center dark:bg-gray-900">
      <div class="grid gap-8">
        <div id="back-div" class="bg-gradient-to-r from-blue-500 to-purple-500 rounded-[25px] m-4">
          <div class="border-[20px] border-transparent rounded-[20px] dark:bg-gray-900 bg-white shadow-lg xl:p-10 2xl:p-10 lg:p-10 md:p-10 sm:p-2 m-2">
            <h1 class="pb-6 font-bold dark:text-gray-400 text-5xl text-center cursor-default">
              Sign Up
            </h1>
            <Form @submit.prevent="register" class="space-y-4">
                <InputField
                    id="firstName"
                    label="First Name"
                    type="text"
                    :modelValue="firstName"
                    placeholder="First Name"
                    required
                />
                <InputField
                    id="lastName"
                    label="Last Name"
                    type="text"
                    :modelValue="lastName"
                    placeholder="Last Name"
                    required
                />
                <InputField
                    id="email"
                    label="Email"
                    type="email"
                    :modelValue="email"
                    placeholder="Email"
                    required
                />
                <div>
                    <label for="password" class="mb-2 dark:text-gray-400">Password</label>
                    <Password
                        id="password"
                        v-model="password"
                        class="w-full placeholder:text-base"
                        placeholder="Password"
                        feedback="false"
                        toggleMask
                        required
                    />
                </div>
                <div>
                    <label for="password" class="mb-2 dark:text-gray-400">Confirm Password</label>
                    <Password 
                        :invalid="password !== confirmPassword"
                        id="confirmPassword"
                        v-model="confirmPassword"
                        class="w-full placeholder:text-base"
                        placeholder="Confirm Password"
                        feedback="false"
                        toggleMask
                        required
                    />
                </div>
              <Button
                class="bg-gradient-to-r dark:text-gray-300 from-blue-500 to-purple-500 shadow-lg mt-6 p-2 text-white rounded-lg w-full hover:scale-105 hover:from-purple-500 hover:to-blue-500 transition duration-300 ease-in-out"
                type="submit"
                label="SIGN UP"
              />
            </Form>
            <div class="flex flex-col mt-4 items-center justify-center text-sm">
              <h3 class="dark:text-gray-300">
                Already have an account?
                <NuxtLink to="/login" class="group text-blue-400 transition-all duration-100 ease-in-out">
                    <span class="bg-left-bottom bg-gradient-to-r from-blue-400 to-blue-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out">
                        Log In
                    </span>
                </NuxtLink>
              </h3>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
    
    import InputField from '~/components/InputField.vue';

    const { $userStore, $router } = useNuxtApp();
    
    const firstName = ref('');
    const lastName = ref('');
    const email = ref('');
    const password = ref('');
    const confirmPassword = ref('');
    
    const register = async () => {
        if (password.value !== confirmPassword.value) {
        console.error('Passwords do not match');
        return;
        }
    
        try {
        await $userStore.register({
            firstName: firstName.value,
            lastName: lastName.value,
            email: email.value,
            password: password.value,
        });
        $router.push('/login');
        } catch (error) {
        console.log('error', error);
        }
    };
  </script>