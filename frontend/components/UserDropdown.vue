<template>
    <div>
      <a
        class="text-blueGray-500 block"
        @click="toggle" 
      >
        <div class="items-center flex">
          <span
            class="w-12 h-12 text-sm text-white bg-blueGray-200 inline-flex items-center justify-center rounded-full"
          >
            <img
              alt="..."
              class="w-full rounded-full align-middle border-none shadow-lg"
              src="../assets/images/avatar.png"
            />
          </span>
        </div>
      </a>
      <TieredMenu ref="menu" id="overlay_tmenu" :model="items" popup >
        <template #item="{ item, props, hasSubmenu }">
            <a class="flex items-center" v-bind="props.action">
                <span :class="item.icon" />
                <span class="ml-2">{{ item.label }}</span>
                <Badge v-if="item.badge" class="ml-auto" :value="item.badge" />
                <span v-if="item.shortcut" class="ml-auto border border-surface rounded bg-emphasis text-muted-color text-xs p-1">{{ item.shortcut }}</span>
                <i v-if="hasSubmenu" class="pi pi-angle-right ml-auto"></i>
            </a>
        </template>
    </TieredMenu>
  
    </div>
  </template>

<script setup>
    import { ref } from "vue";
    const { $userStore } = useNuxtApp();
    const router = useRouter()
    const menu = ref();
    const items = ref([
        {
            label: 'Proile',
            icon: 'pi pi-user',
            command: () => {
                // Callback to run
            }
        },
        
        {
            separator: true
        },
        {
            label: 'Log out',
            icon: 'pi pi-sign-out',
            command: async () => {
                await $userStore.logout();
                router.push('/login')

            }
        }
    ]);
    
    const toggle = (event) => {
        menu.value.toggle(event);
    };

</script>