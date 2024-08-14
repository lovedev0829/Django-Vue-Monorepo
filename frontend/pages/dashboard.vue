<template>
    <div>
      <sidebar-component></sidebar-component>
      <div class="relative md:ml-64 bg-blueGray-100">
        <navbar-component></navbar-component>
      
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