<!-- /components/InputField.vue -->
<template>
    <div class="flex flex-col">
      <label :for="id" class="mb-2 dark:text-gray-400">{{ label }}</label>
      <InputText
        :id="id"
        v-model="localValue"
        :type="type"
        :placeholder="placeholder"
        :required="required"
        class="w-full placeholder:text-base"
      />
    </div>
  </template>
  
  <script setup>
  import { ref, watch, computed } from 'vue';
  
  const props = defineProps({
    id: String,
    label: String,
    type: {
      type: String,
      default: 'text',
    },
    modelValue: [String, Number],
    placeholder: String,
    required: {
      type: Boolean,
      default: false,
    },
  });
  
  const emit = defineEmits(['update:modelValue']);
  
  const localValue = computed({
    get() {
      return props.modelValue;
    },
    set(value) {
      emit('update:modelValue', value);
    },
  });
  </script>
  