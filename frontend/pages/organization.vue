<template>
    <main-layout-component>
        <Card class="w-full px-4 h-full">
            <template #title>
                <h3>Organization settings</h3>
                <h5>Manage your organization</h5>
            </template>
            <template #content>
                <Menubar :model="items"  class="bg-white border-0" />
                <div>
                    
                </div>
            </template>
        </Card>
    </main-layout-component>
</template>

<script setup>

    import MainLayoutComponent from "../layouts/main.vue";
    import { ref } from "vue";

    const items = ref([
        {
            label: 'Memeber',
            icon: 'pi pi-users',
            command: () => { /* Your command logic here */ },
            active: true,
            focused: true,

        },
        {
            label: 'General',
            icon: 'pi pi-star',
            active: false
        },
        {
            label: 'Subscription',
            icon: 'pi pi-calendar',
            active: false
        },
       
    ]);
</script>