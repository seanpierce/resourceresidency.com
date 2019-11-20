<template>
    <div v-if="loaded">
        <Navigation />
        <Artists v-if="route === 'artists'" />
        <Artist v-if="route === 'artist'" />
        <Residencies v-if="route === 'residencies'" />
        <Residency v-if="route === 'residency'" />
    </div>
</template>

<script>
import Navigation from './partials/Navigation.vue';
import Artists from './pages/Artists.vue';
import Artist from './pages/Artist.vue';
import Residencies from './pages/Residencies.vue';
import Residency from './pages/Residency.vue';

export default {
    name: 'App',
    components: {
        Navigation,
        Artists,
        Artist,
        Residencies,
        Residency
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