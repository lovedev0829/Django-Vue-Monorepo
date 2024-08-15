<template>
    <!-- Navbar -->
    <nav
      class="absolute top-0 left-0 w-full z-10 bg-transparent md:flex-row md:flex-nowrap md:justify-start flex items-center p-4 bg-white"
    >
      <div
        class="w-full mx-autp items-center flex justify-between md:flex-nowrap flex-wrap md:px-10 px-4"
      >
        <!-- Brand -->
       
        
        <!-- Form -->
        <form
          class="md:flex hidden flex-row flex-wrap items-center lg:ml-auto mr-3"
        >
          <div class="relative flex w-full flex-wrap items-stretch">
            <span class="relative">
              <i class="pi pi-search absolute top-2/4 -mt-2 left-3 text-surface-400 dark:text-surface-600" />
                <InputText v-model="value1" placeholder="Search" class="pl-10" />
              </span>
          </div>
        </form>
        <!-- User -->
        <ul
          class="flex-col md:flex-row list-none items-center hidden md:flex"
        >
          <user-dropdown-component></user-dropdown-component>
        </ul>
      </div>
    </nav>
  
    <!-- End Navbar -->
  </template>
  
  <script setup>

  import UserDropdownComponent from "./UserDropdown.vue";
  
  </script>