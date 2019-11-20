<template>
    <div>
        <h2>Artists</h2>
        <ul>
            <li v-for="artist in artists" :key="artist.id">
                <a :href="'/artists/' + artist.id">{{ artist.name }}</a>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'Artists',
    computed: {
        artists() {
            return this.$root.data;
        }
    }
}
</script>