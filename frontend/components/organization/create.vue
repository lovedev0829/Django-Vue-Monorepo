<template>
    <div class="mt-10 flex-col flex gap-4">
        <h5>Manage organization</h5>
        <div class="flex flex-row gap-4">
            <div class="flex flex-col gap-2">
                <InputText id="name" v-model="name" placeholder="Name" class="w-80" />
            </div>
            <div class="flex flex-col gap-2">
                <Button @click="createHandle">+ Create new Team</Button>
            </div>
        </div>
    </div>
</template>


<script setup>

    import { ref } from "vue";
    import { useTeamStore } from '@/stores/team'; // Import the team store

    const toast = useToast();
    const name = ref('');
    const teamStore = useTeamStore();

    const createHandle = async () => {
        if(name.value === "")     {
            toast.add({
                severity: 'error',
                summary: 'Invalid Team Name',
                detail: "Please provide correct team name!",
                life: 3000,
            });  
            return
        }

        await teamStore.createTeam(name.value).then(res => {
            toast.add({
                severity: 'success',
                detail: "Team created successfully!",
                life: 3000,
            });  
        })
    }


</script>