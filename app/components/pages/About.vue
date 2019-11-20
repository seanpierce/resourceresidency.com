<template>
    <div v-if="content" v-html="content.info"></div>
</template>

<script>
export default {
    name: 'About',
    computed: {
        content() {
            return this.$root.data;
        }
    }
}
</script>