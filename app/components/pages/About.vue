<template>
    <div class="content">
        <h2>About</h2>
        <div v-if="content" v-html="content.info"></div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            content: null
        }
    },
    methods: {
        getContent() {
            axios.get('/api/content/about')
                .then(response => {
                    this.content = response.data;
                })
                .catch(error => {
                    console.oog(error);
                })
        }
    },
    mounted() {
        this.getContent();
    }
}
</script>