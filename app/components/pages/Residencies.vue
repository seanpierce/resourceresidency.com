<template>
    <div>
        <h2>Residencies</h2>
        <ul>
            <li v-for="residency in residencies" :key="residency.id">
                <a :href="'/residencies/' + residency.id">{{ residency.name }}</a>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'Residencies',
    computed: {
        residencies() {
            return this.$root.data;
        }
    }
}
</script>