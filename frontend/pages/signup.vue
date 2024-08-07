<script setup>
    import { useForm } from 'vee-validate';
    import * as yup from 'yup';
    import InputField from '~/components/InputField.vue';

    const { $userStore, $router } = useNuxtApp();

    const schema = yup.object({
        email: yup.string().required().email().label('Email address'),
        firstName: yup.string().required().label('First Name'),
        lastName: yup.string().required().label('Last Name'),
        password: yup.string().required().min(6).label('Password'),
        passwordConfirm: yup
            .string()
            .oneOf([yup.ref('password')], 'Passwords must match')
            .required()
            .label('Password confirmation'),
        terms: yup
            .boolean(false)
            .required()
            .oneOf([true], 'You must agree to the terms and conditions')
            .label('Terms agreement'),
    });

    const { defineField, handleSubmit, errors } = useForm({
        validationSchema: schema
    });

    const [firstName, firstNameProps] = defineField('firstName');
    const [lastName, lastNameProps] = defineField('lastName');
    const [email, emailProps] = defineField('email');
    const [password, passwordProps] = defineField('password');
    const [passwordConfirm, passwordConfirmProps] = defineField('passwordConfirm');
    const [terms, termsProps] = defineField('terms');

    const onSubmit = handleSubmit(async (values) => {
    
        try {

            await $userStore.register({
                    firstName: values.firstName,
                    lastName: values.lastName,
                    email: values.email,
                    password: values.password,
            });
        
            $router.push('/login');

        } catch (error) {
            console.log('error', error);
        }
    });
</script>

<template>
    <div class="h-screen w-screen flex justify-center items-center dark:bg-gray-900">
      <div class="grid gap-8">
        <div id="back-div" class="bg-gradient-to-r from-blue-500 to-purple-500 rounded-[25px] m-4">
          <div class="border-[20px] border-transparent rounded-[20px] dark:bg-gray-900 bg-white shadow-lg xl:p-10 2xl:p-10 lg:p-10 md:p-10 sm:p-2 m-2">
            <h1 class="pb-6 font-bold dark:text-gray-400 text-5xl text-center cursor-default">
              Sign Up
            </h1>
            <Form @submit.prevent="onSubmit" class="space-y-4">
              <InputField
                id="firstName"
                label="First Name"
                type="text"
                v-model="firstName"
                v-bind="firstNameProps"
                placeholder="First Name"
              />
              <small id="firstName-help" class="p-error">
                {{ errors.firstName }}
              </small>
              <InputField
                id="lastName"
                label="Last Name"
                type="text"
                v-model="lastName"
                v-bind="lastNameProps"
                placeholder="Last Name"
              />
              <small id="lastName-help" class="p-error">
                {{ errors.lastName }}
              </small>
              <InputField
                id="email"
                label="Email"
                type="email"
                v-model="email"
                v-bind="emailProps"
                placeholder="Email"
              />
              <small id="email-help" class="p-error">
                {{ errors.email }}
              </small>
              <div class="flex flex-col">
                <label for="password" class="mb-2 dark:text-gray-400">Password</label>
                <Password
                  id="password"
                  v-model="password"
                  v-bind="passwordProps"
                  class="w-full placeholder:text-base"
                  placeholder="Password"
                  feedback="false"
                  toggleMask
                />
                <small id="password-help" class="p-error">
                  {{ errors.password }}
                </small>
              </div>
              <div class="flex flex-col">
                <label for="passwordConfirm" class="mb-2 dark:text-gray-400">Confirm Password</label>
                <Password
                  id="passwordConfirm"
                  v-model="passwordConfirm"
                  v-bind="passwordConfirmProps"
                  class="w-full placeholder:text-base"
                  placeholder="Confirm Password"
                  feedback="false"
                  toggleMask
                />
                <small id="passwordConfirm-help" class="p-error">
                  {{ errors.passwordConfirm }}
                </small>
              </div>
              <div class="flex items-start">
                <Checkbox
                  id="terms"
                  v-model="terms"
                  v-bind="termsProps"
                  :binary="true"
                  class="mr-2"
                />
                <label for="terms" class="dark:text-gray-400">
                  I agree to the
                  <NuxtLink to="/terms" class="text-blue-400">terms and conditions</NuxtLink>
                </label>
              </div>
              <small id="terms-help" class="p-error">
                {{ errors.terms }}
              </small>
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
  
  <style>
  .p-error {
    display: block;
    color: red;
  }
  </style>
  