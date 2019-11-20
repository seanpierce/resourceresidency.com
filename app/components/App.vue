<template>
    <div v-if="loaded">
        <Navigation />
        <Artists v-if="route === 'artists'" />
        <Artist v-if="route === 'artist'" />
        <Residencies v-if="route === 'residencies'" />
        <Residency v-if="route === 'residency'" />
        <About v-if="route === 'about'" />
    </div>
</template>

<script>
import Navigation from './partials/Navigation.vue';
import Artists from './pages/Artists.vue';
import Artist from './pages/Artist.vue';
import Residencies from './pages/Residencies.vue';
import Residency from './pages/Residency.vue';
import About from './pages/About.vue';

export default {
    name: 'App',
    components: {
        Navigation,
        Artists,
        Artist,
        Residencies,
        Residency,
        About
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