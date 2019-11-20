<template>
    <div>
        <h2>Artist</h2>
        <h3>{{ artist.name }}</h3>
        <div v-html="artist.info"></div>
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