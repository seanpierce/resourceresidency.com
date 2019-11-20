<template>
    <div>
        <h2>Residency</h2>
        <h3>{{ residency.name }}</h3>
        <div v-html="residency.info"></div>
        <div v-if="residency.artists.length > 0">
            <h3>Artists</h3>
            <ul>
                <li v-for="artist in residency.artists" :key="artist.id">
                    <a :href="'/artists/' + artist.id">{{ artist.name }}</a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Residency',
    computed: {
        residency() {
            return this.$root.data;
        }
    }
}
</script>