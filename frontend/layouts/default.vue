<template>
    <div
        class="min-h-screen bg-slate-100 text-slate-900 dark:bg-slate-900 dark:text-white"
    >
        <div class="container mx-auto max-w-screen-lg px-8">
            <div
                class="rounded-2xl bg-white px-6 py-8 shadow-xl dark:bg-slate-800"
            >
                <slot />
            </div>
        </div>
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