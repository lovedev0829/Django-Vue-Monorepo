<template>
    <!-- Navbar -->
    <nav class="absolute top-0 left-0 w-full z-10 bg-transparent md:flex-row md:flex-nowrap md:justify-start flex items-center p-4 bg-white">
      <div class="w-full mx-auto items-center flex justify-between md:flex-nowrap flex-wrap md:px-10 px-4">
        <div class="gap-4 flex flex-row">
          <Dropdown
            v-model="selectedTeam"
            :options="groupedTeams"
            optionLabel="label"
            optionGroupLabel="label"
            optionGroupChildren="items"
            class="custom-dropdown w-64"
            @change="handleChangeOrg"
            optionValue="id"
          >
            <template #optiongroup="slotProps">
              <div class="flex align-items-center">
                <div>{{ slotProps.option.label }}</div>
              </div>
            </template>
          </Dropdown>
          <Button icon="pi pi-cog" text rounded size="large" />
        </div>
  
        <form class="md:flex hidden flex-row flex-wrap items-center lg:ml-auto mr-3">
          <div class="relative flex w-full flex-wrap items-stretch">
            <span class="relative">
              <i class="pi pi-search absolute top-2/4 -mt-2 left-3 text-surface-400 dark:text-surface-600" />
              <InputText v-model="value1" placeholder="Search" class="pl-10" />
            </span>
          </div>
        </form>
        <ul class="flex-col md:flex-row list-none items-center hidden md:flex">
          <user-dropdown-component></user-dropdown-component>
        </ul>
      </div>
    </nav>
    <!-- End Navbar -->
  </template>
  
  <script setup>

  import { ref, onMounted, computed, watch } from 'vue';
  import UserDropdownComponent from './UserDropdown.vue';
  import { useTeamStore } from '@/stores/team';
  import { TeamType } from "@/constants/team.global.ts"
  import { generateTeamPath } from "@/helper/team.global.ts"
  const { $router } = useNuxtApp();

  const selectedTeam = ref(null);
  const teamStore = useTeamStore();
  
  const groupedTeams = computed(() => {
    
    const personalAccount = {
      label: 'Personal Account',
      items: [],
    };
  
    const organizations = {
      label: 'Organization',
      items: [],
    };
  
    teamStore.teams.forEach((team) => {
      const displayName = team.name;
      const item = { label: displayName, id: team.id };
      if (team.type === TeamType.PERSONAL) {
            personalAccount.items.push(item);
      } else {
            organizations.items.push(item);
      }
    });
  
    return [personalAccount, organizations];

  });
  
  watch(teamStore.selectedTeam, (currentTeam) => {
      console.log("currentTeam", currentTeam)
        selectedTeam.value = currentTeam.id
  }, { immediate: true });
  
  const handleChangeOrg = () => {
      teamStore.changeCurrentTeam(selectedTeam.value)
      const path = generateTeamPath("")
      $router.push(path)
  };
  
  onMounted(() => {
    teamStore.fetchTeams();
  });
  </script>
  
  <style scoped>
  .custom-dropdown .p-dropdown-panel {
    max-height: none !important; /* Remove max height limit */
    overflow: hidden !important;  /* Disable scroll and hide overflow */
  }
  </style>
  