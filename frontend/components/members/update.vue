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
        <div class="flex items-baseline gap-2 mt-10">
            <i class="pi pi-exclamation-triangle" style="font-size: 1.5rem; color: red"></i>
            <span style="font-size: 1.5rem; color: red">Danger Zone</span>
        </div>
        <div class="flex items-baseline justify-between w-1/2 mt-12 border-2 border-red-500 p-5 rounded-md">
            <span style="font-size: 1.5rem; color: red">Delete this organization</span>
            <Button  severity="danger" @click="deleteTeamHandle">Remove organization</Button>
        </div>
        <ConfirmDialog group="templating" class="w-2/12">
            <template #message="slotProps">
                <div class="flex flex-col items-center w-full gap-4 border-b border-surface-200 dark:border-surface-700">
                    <i :class="slotProps.message.icon" class="!text-6xl text-primary-500"></i>
                    <p>{{ slotProps.message.message }}</p>
                </div>
            </template>
        </ConfirmDialog>
    </div>
</template>


<script setup>

    import { ref } from "vue";    
    import TeamService from "@/services/TeamService";
    import { useTeamStore } from '@/stores/team';
    import { useConfirm } from "primevue/useconfirm";

    const toast = useToast();
    const teamStore = useTeamStore();
    const currentTeamId = teamStore.selectedTeam.id;
    const name = ref('');
    const router = useRouter()
    const confirm = useConfirm();

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

    const deleteTeamHandle = () => {
        confirm.require({
            group: 'templating',
            header: 'Confirmation',
            message: 'Please confirm to proceed moving forward.',
            icon: 'pi pi-exclamation-circle',
            rejectProps: {
                label: 'Cancel',
                icon: 'pi pi-times',
                outlined: true,
                size: 'small'
            },
            acceptProps: {
                label: 'Delete',
                icon: 'pi pi-check',
                size: 'small'
            },
            accept: async () => {
                await TeamService.deleteTeam(currentTeamId).then( res => {
                    toast.add({
                        severity: 'success',
                        detail: res.message,
                        life: 3000,
                    });
                });

                teamStore.resetTeamStorage()
                router.push('/dashboard')
            }
        });
      
    }

</script>