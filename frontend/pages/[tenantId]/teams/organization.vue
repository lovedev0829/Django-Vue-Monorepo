<template>
    <main-layout-component>
        <Card class="w-full px-4 h-full">
            <template #title>
                <h3>Organization settings</h3>
                <h5>Manage your organization</h5>
            </template>
            <template #content>
                <SelectButton v-model="menu" :options="menus" optionLabel="label" dataKey="label" />
                <organization-component></organization-component>
            </template>
        </Card>
    </main-layout-component>
</template>

<script setup>

    import MainLayoutComponent from "../layouts/main.vue";
    import OrganizationComponent from '@/components/organization/create.vue'
    

    import { ref } from "vue";
    
    const menu = ref("")
    const action = ref("");

    const menus = ref([
        { label: 'Memeber', value: 'member' },
        { label: 'General', value: 'general' },
        { label: 'Subscription', value: 'subscription' }
    ]);

</script>