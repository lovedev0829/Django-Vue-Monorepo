<template>
    <div>
      <sidebar-component></sidebar-component>
      <div class="relative md:ml-64 bg-blueGray-100">
        <navbar-component></navbar-component>
        <div class="relative md:pt-32 pb-32 pt-12">
            <div class="px-4 md:px-10 mx-auto w-full">
                <div class="flex flex-wrap">
                    <div class="w-full px-4 h-full">
                        <slot></slot>
                    </div>
                </div>
            </div>
          </div>
      </div>
    </div>
  </template>

  <script>
      import NavbarComponent from "../components/Navbar.vue";
      import SidebarComponent from "../components/Sidebar.vue";
      
      export default {
            name: "dashboard-page",
            components: {
            NavbarComponent,
            SidebarComponent,
            },
            data() {
                return {
                    date: new Date().getFullYear()
                }
            }
      };
  </script>