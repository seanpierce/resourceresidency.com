import App from './components/App.vue';

export const app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    components: {
        'App': App
    },
    data: {
        page: null,
        data: null,
        debug: null,
        loaded: false
    },
    computed: {
    },
    mounted() {
        // Fetch the initial page data MVC style
        var elem = document.getElementById('data');

        if (elem) {
            if (elem.attributes.page.value)
                this.page = elem.attributes.page.value;

            if (elem.attributes.data.value)
                this.data = JSON.parse(elem.attributes.data.value);

            if (elem.attributes.debug.value)
                this.debug = elem.attributes.debug.value === 'true';
        }

        this.loaded = true;
    },
    template: `
        <App />
    `
  })