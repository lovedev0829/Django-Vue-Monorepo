<template>
    <div class="min-h-screen bg-slate-100 text-slate-900 dark:bg-slate-900 dark:text-white">
        <slot />
    </div>
    <Toast />
</template>

<script setup lang="ts">
    useLocaleHead({
        addDirAttribute: true,
        identifierAttribute: 'id',
        addSeoAttributes: true
    });
</script>