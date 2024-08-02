// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  devServer: {
    host: '0.0.0.0',
    port: '3000'
  },

  modules: ['nuxt-primevue', '@nuxtjs/tailwindcss', '@nuxtjs/eslint-module'],

  primevue: {
    usePrimeVue: true,
    options: {
      unstyled: false,
      ripple: true
    },
    cssLayerOrder: 'tailwind-base,primevue, tailwind-utilities',
    components: {
      include: '*',
      exclude: ['Galleria', 'Carousel', 'Chart', 'Editor']
    },
    directives: {
      include: ['Ripple', 'Tooltip']
    }
  },

  css: [
    '~/assets/scss/main.scss',
    '~/assets/css/tailwind.css',
    '~/assets/css/theme.css'
  ],

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {}
    }
  },

  compatibilityDate: '2024-08-02'
})