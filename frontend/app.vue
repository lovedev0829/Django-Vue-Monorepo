<template>
    <NuxtLayout>
        <NuxtPage />
    </NuxtLayout>
</template>

<script setup>

    const { $userStore } = useNuxtApp();
    const router = useRouter()

    if($userStore.access_token) {
        router.push('/dashboard')
    } else {
        router.push('/login')
    }

</script>