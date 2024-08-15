<template>
    <main-layout-component>
        <div id="dashboard-componenet">
            hello world
        </div>
    </main-layout-component>
</template>

  <script>
      import MainLayoutComponent from "../layouts/main.vue";
      
      export default {
            name: "dashboard-page",
            components: {
              MainLayoutComponent,
            },
      };
  </script>