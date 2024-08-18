<template>
    <div class="mt-10 flex-col flex gap-4">
        <h5>Manage organization</h5>
        <div class="flex flex-row gap-4">
            <div class="flex flex-col gap-2">
                <InputText id="name" v-model="name" placeholder="Name" class="w-80" />
            </div>
            <div class="flex flex-col gap-2">
                <Button @click="createHandle">+ Create new tenant</Button>
            </div>
        </div>
    </div>
</template>


<script setup>

    import { ref } from "vue";
    import TeamService from "@/services/TeamService.ts"
    
    const toast = useToast();
    const name = ref('');

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

        await TeamService.createTeam(name.value).then(res => {
            console.log(res)
        })
    }


</script>