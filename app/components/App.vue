<template>
    <div>
        <div id="container">
            <Navigation />
            <Home v-if="route === 'home'" />
            <About v-if="route === 'about'" />
            <Events v-if="route === 'events'" />
        </div>
    </div>
</template>

<script>
import Home from './pages/Home.vue';
import Navigation from './partials/Navigation.vue';
import Artists from './pages/Artists.vue';
import Artist from './pages/Artist.vue';
import Residencies from './pages/Residencies.vue';
import Residency from './pages/Residency.vue';
import About from './pages/About.vue';
import Events from './pages/Events.vue';

export default {
    name: 'App',
    components: {
        Home,
        Navigation,
        Artists,
        Artist,
        Residencies,
        Residency,
        About,
        Events
    },
    computed: {
        route() {
            return this.$root.page;
        },
        loaded() {
            return this.$root.loaded;
        }
    },
}
</script>