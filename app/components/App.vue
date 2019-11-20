<template>
    <div v-if="loaded">
        <Navigation />
        <Artists v-if="route === 'artists'" />
        <Artist v-if="route === 'artist'" />
    </div>
</template>

<script>
import Navigation from './partials/Navigation.vue';
import Artists from './pages/Artists.vue';
import Artist from './pages/Artist.vue';

export default {
    name: 'App',
    components: {
        Navigation,
        Artists,
        Artist
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