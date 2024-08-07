<template>
    <div>
        Welcome to MonoRepo Dashboard!
    </div>
</template>

<script setup>
    const { $userStore } = useNuxtApp();
    console.log($userStore.access_token)
</script>