<template>
    <div class="mt-10 flex-col flex gap-4">
        <h5>Invite new member</h5>
        <div class="flex flex-row gap-4">
            <div class="flex flex-col gap-2">
                <label for="email">Email</label>
                <InputText id="email" v-model="email" placeholder="Email" aria-describedby="username-help" class="w-80" />
            </div>
            <div class="flex flex-col gap-2">
                <label for="role">Role</label>
                <Select v-model="role" :options="roles" optionLabel="role" placeholder="Select a City"  class="w-80 p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-blue-300">
                    <option v-for="role in roles" :value="role.value">{{ role.name }}</option>
                </Select>
            </div>
        </div>
        <div>
            <Button>Invite</Button>
        </div>
        <Divider class="w-1/2" />
        <DataTable :value="users" tableStyle="max-width: 50rem" class="bg-white" >
            <template #empty> No members found. </template>
            <template #loading> Loading members data. Please wait. </template>
            <Column field="email" header="Username" ></Column>
            <Column field="role" header="Role" ></Column>
            <Column field="invitation"  header="Invitation accepted" >
                <template #body="{ data }">
                    <div class="flex items-center gap-2">
                        <span class="pi pi-check-circle" v-if="data.invitation == 'Yes'"></span>
                        <span class="pi pi-clock" v-if="data.invitation == 'No'"></span>
                        <span>{{ data.invitation }}</span>
                    </div>
                </template>
            </Column>
            <Column field="action" header="Actions" >
                <template #body="{ data }">
                    <Button type="button" icon="pi pi-ellipsis-v" @click="toggle" aria-haspopup="true" aria-controls="overlay_menu" text  rounded  severity="secondary"  size="small" />
                    <TieredMenu  ref="action" id="overlay_menu" :model="actions" :popup="true" />
                </template>
            </Column>
        </DataTable>                
    </div>
</template>


<script setup>

    import { ref } from "vue";
    
    const email = ref('');
    const role = ref();
    const menu = ref("")
    const action = ref("");

    const menus = ref([
        { label: 'Memeber', value: 'member' },
        { label: 'General', value: 'general' },
        { label: 'Subscription', value: 'subscription' }
    ]);


    const roles = ref([
        { name: 'Memeber', value: 'memeber' },
        { name: 'Admin', value: 'admin' },
        { name: 'Owner', value: 'owner' },
    ]);

    const users = [
        {
            email: "lovedev0829@gmail.com",
            role: "Admin",
            invitation: "Yes"
        },
        {
            email: "tlegen@gmail.com",
            role: "Owner",
            invitation: "Yes"
        },
        {
            email: "vlady@gmail.com",
            role: "Memeber",
            invitation: "No"
        }
    ]

    
    const actions = ref([
        {
            label: 'Actions',
            class: 'font-bold pointer-events-none',
            
        },
        {
            label: 'Change Role',
            items: [
                { label: 'Admin' },
                { label: 'Memeber' },
            ]

        },
        {
            label: 'Delete',
        }
    ]);

    const toggle = (event) => {
        action.value.toggle(event);
    };
</script>