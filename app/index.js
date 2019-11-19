import App from './components/App.vue';

export const app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    components: {
        'App': App
    },
    data: {
    },
    computed: {
    },
    mounted() {
    },
    template: `
        <App />
    `
  })