<template>
    <nav
      class="md:left-0 md:block md:fixed md:top-0 md:bottom-0 md:overflow-y-auto md:flex-row md:flex-nowrap md:overflow-hidden shadow-xl bg-white  z-10 py-4 px-6"
    >
      <div
        class="md:flex-col md:items-stretch md:min-h-full md:flex-nowrap px-0 flex flex-wrap items-center justify-between w-full mx-auto"
      >
        <!-- Toggler -->
        <button
          class="cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent"
          type="button"
          v-on:click="toggleCollapseShow('bg-white m-2 py-3 px-6')"
        >
          <i class="fas fa-bars"></i>
        </button>
        <!-- Brand -->
        <a
          class="md:block text-left md:pb-2 text-blueGray-600 mr-0 inline-block whitespace-nowrap text-sm uppercase font-bold p-4 px-0"
          href="javascript:void(0)"
        >
        MonoRepo SaaS
        </a>
        <!-- User -->
        <ul class="md:hidden items-center flex flex-wrap list-none">
          <li class="inline-block relative">
            <notification-dropdown-component></notification-dropdown-component>
          </li>
          <li class="inline-block relative">
            <user-dropdown-component></user-dropdown-component>
          </li>
        </ul>
        <!-- Collapse -->
        <div
          class="md:flex md:flex-col md:items-stretch md:opacity-100 md:relative md:mt-4 md:shadow-none shadow absolute top-0 left-0 right-0 z-40 overflow-y-auto overflow-x-hidden h-auto items-center flex-1"
          v-bind:class="collapseShow"
        >
          <!-- Collapse header -->
          <div
            class="md:min-w-full md:hidden block pb-4 mb-4 border-b border-solid border-blueGray-200"
          >
            <div class="flex flex-wrap">
              <div class="w-6/12">
                <a
                  class="md:block text-left md:pb-2 text-blueGray-600 mr-0 inline-block whitespace-nowrap text-sm uppercase font-bold p-4 px-0"
                  href="javascript:void(0)"
                >
                  MonoRepo SaaS
                </a>
              </div>
              <div class="w-6/12 flex justify-end">
                <button
                  type="button"
                  class="cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent"
                  v-on:click="toggleCollapseShow('hidden')"
                >
                  <i class="fas fa-times"></i>
                </button>
              </div>
            </div>
          </div>
          <Menu :model="items" class="border-0 w-full">
            <template #item="{ item, props }">
                <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
                    <a :href="href" v-bind="props.action" @click="navigate">
                        <span :class="item.icon" />
                        <span class="ml-2">{{ item.label }}</span>
                    </a>
                </router-link>
                <a v-else :href="item.url" :target="item.target" v-bind="props.action">
                    <span :class="item.icon" />
                    <span class="ml-2">{{ item.label }}</span>
                </a>
            </template>
        </Menu>
        </div>
      </div>
    </nav>
  </template>

  <script setup>
  
  import NotificationDropdownComponent from "./NotificationDropdown.vue";
  import UserDropdownComponent from "./UserDropdown.vue";

    const collapseShow = "hidden";
    const router = useRouter()
    const toggleCollapseShow = function(classes) {
        this.collapseShow = classes;
    }

    const items = ref([
            {
                label: 'Dashboard',
                icon: 'pi pi-home',
                route: '/dashboard'
            },
            {
                label: 'Payment',
                icon: 'pi pi-money-bill',
            },
            {
                label: 'External',
                icon: 'pi pi-home',
            },
            {
                label: 'Subscription',
                icon: 'pi pi-home',
            },
            {
                label: 'Organization settings',
                icon: 'pi pi-building',
                route: 'organization'
            },
            {
            label: 'Statis pages',
            items: [
                {
                    label: 'Privacy policy',
                },
                {
                    label: 'Terms and conditions',
                }
            ]
        }

        ])
  </script>