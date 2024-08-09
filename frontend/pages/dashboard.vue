<template>
    <div>
        Welcome to MonoRepo Dashboard!
    </div>
    <Button>
         Logout
    </Button>
</template>

<script setup>
    const { $userStore } = useNuxtApp();
</script>