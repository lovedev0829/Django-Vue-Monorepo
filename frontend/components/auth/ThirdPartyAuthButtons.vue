<template>
    <div id="third-party-auth" class="flex items-center justify-center mt-5 flex-wrap">
      <Button
        v-for="provider in providers"
        :key="provider.name"
        @click="$emit('thirdPartyAuth', provider.name)"
        severity="secondary"
        class="hover:scale-105 ease-in-out duration-300 shadow-lg p-2 rounded-lg m-1"
        :icon="provider.icon"
        style="font-size: 1.5em"
      />
    </div>
</template>
  
<script setup>

    const providers =  ref([
            { name: 'google', icon: 'pi pi-google' },
            { name: 'linkedin', icon: 'pi pi-linkedin' },
            { name: 'github', icon: 'pi pi-github' },
            { name: 'facebook', icon: 'pi pi-facebook' },
            { name: 'twitter', icon: 'pi pi-twitter' },
            { name: 'apple', icon: 'pi pi-apple' },
    ])

</script>
  