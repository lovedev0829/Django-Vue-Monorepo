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
            <Button>Save changes</Button>
        </div>             
    </div>
</template>


<script setup>

    import { ref } from "vue";    
    const name = ref('');

</script>