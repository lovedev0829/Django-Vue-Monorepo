<template>
    <div class="mt-10 flex-col flex gap-4">
        <h5>Update organization</h5>
        <div class="flex flex-row gap-4">
            <div class="flex flex-col gap-2">
                <label for="name">Name</label>
                <InputText id="name" v-model="name" placeholder="Name" class="w-80" />
            </div>
        </div>
        <div class="flex flex-row gap-4">
            
            <Button severity="secondary"  >Cancel</Button> 
            <Button @click="changeTeamHandle">Save changes</Button>
        </div>             
    </div>
</template>


<script setup>

    import { ref } from "vue";    
    import TeamService from "@/services/TeamService";
    import { useTeamStore } from '@/stores/team';

    const toast = useToast();
    const teamStore = useTeamStore();
    const currentTeamId = teamStore.selectedTeam.id;
    const name = ref('');

    onMounted(async() => {
        await TeamService.getTeamByID(currentTeamId).then( res => {
            name.value = res.team.name;
        });
    });

    const changeTeamHandle = async () => {
        
        await TeamService.updateTeam(currentTeamId, name.value).then( res => {
            toast.add({
                severity: 'success',
                detail: res.message,
                life: 3000,
            });
        });

        await teamStore.fetchTeams()
    }

</script>