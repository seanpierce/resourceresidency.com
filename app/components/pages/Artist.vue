<template>
    <div>
        <h2>Artist</h2>
        <h3>{{ artist.name }}</h3>
        <div v-html="artist.info"></div>
        <div v-if="artist.residencies.length > 0">
            <h3>Residencies</h3>
            <ul>
                <li v-for="residency in artist.residencies" :key="residency.id">
                    <a :href="'/residencies/' + residency.id">{{ residency.name }}</a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Artist',
    computed: {
        artist() {
            return this.$root.data;
        }
    }
}
</script>