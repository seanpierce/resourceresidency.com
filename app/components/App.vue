<template>
    <div>
        <div id="twitch-stream"></div>
        <img src="/assets/images/somekindofshow.jpg" alt="" style="width:100%">
        <div id="temp-logos">
            <img src="/assets/images/calexo_logo.png" alt="" style="transform:translateY(-100%)" onclick="window.location.href='https://calexo.co'">
            <img src="/assets/images/s1_logo.png" alt="" style="width:20%" onclick="window.location.href='https://https://s1portland.com/'">
        </div>
    </div>
    <!-- <div v-if="loaded">
        <Navigation />
        <Artists v-if="route === 'artists'" />
        <Artist v-if="route === 'artist'" />
        <Residencies v-if="route === 'residencies'" />
        <Residency v-if="route === 'residency'" />
        <About v-if="route === 'about'" />
    </div> -->
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
    mounted() {
        new Twitch.Embed("twitch-stream", {
            width: '100%',
            height: 500,
            channel: "resourceresidency",
            layout: "video",
            autoplay: false,
            setFullscreen: true
            // only needed if your site is also embedded on embed.example.com and othersite.example.com 
            // parent: ["embed.example.com", "othersite.example.com"]
        });
    }
}
</script>