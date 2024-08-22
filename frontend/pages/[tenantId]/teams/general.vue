<template>
    <main-layout-component>
        <Card class="w-full px-4 h-full">
            <template #title>
                <h3>Organization settings</h3>
                <h5>Manage your organization</h5>
            </template>
            <template #content>
                <SelectButton v-model="menu" :options="menus" optionLabel="label" dataKey="value" />
                <personal-memeber-component v-if="currenTeamType == TeamType.PERSONAL"></personal-memeber-component>
                <organization-member-component v-else-if="currenTeamType == TeamType.ORGANIZATION"></organization-member-component>
            </template>
        </Card>
    </main-layout-component>
</template>

<script setup>

    import MainLayoutComponent from "../layouts/main.vue";
    import PersonalMemeberComponent from '@/components/organization/update.vue';
    import OrganizationMemberComponent from '@/components/members/update.vue';
    import { TeamType } from "@/constants/team.global.ts"
    import { useTeamStore } from '@/stores/team';
    import { generateTeamPath } from "@/helper/team.global"

    import { ref, watch } from "vue";
    const { $router } = useNuxtApp();
    
    const menu = ref("member");
    const teamStore = useTeamStore();
    const currenTeamType = teamStore.selectedTeam.type
    const menus = ref([
        { label: 'Member', value: 'member' },
        { label: 'General', value: 'general' },
        { label: 'Subscription', value: 'subscription' }
    ]);

    // Watch the menu ref and navigate to the corresponding route when it changes
    watch(menu, (newValue) => {
        if (newValue?.value === 'member') {
            $router.push(generateTeamPath('teams/member'));
        } else if (newValue?.value === 'subscription') {
            $router.push(generateTeamPath('subscriptions'));
        }
    });
</script>
