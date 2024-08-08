// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['nuxt-primevue', '@nuxtjs/i18n', '@pinia/nuxt'],

  components: [
      {
          path: '~/components',
          pathPrefix: false
      }
  ],

  primevue: {
      options: {
          unstyled: true
      },
      importPT: { as: 'Lara', from: '~/presets/lara' }  },

  imports: {
      dirs: ["./locales"],
  },

  css: [
      '@/assets/styles/style.css',
      '/node_modules/primeicons/primeicons.css',
      '@/assets/styles/layout/layout.scss'
  ],

  postcss: {
      plugins: {
          tailwindcss: {},
          autoprefixer: {}
      }
  },
  runtimeConfig: {
    public: {
        API_BASE_URL: process.env.NODE_ENV === "development" ? 'http://192.168.147.193:8000/api/v1' : process.env.API_BASE_URL,
    },
  },

  i18n: {
      vueI18n: './i18n.config.ts'
  },
});