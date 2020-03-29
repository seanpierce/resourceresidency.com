<template>
    <div class="event">
        <h3>{{ event.name }}</h3>
        <h4>{{ event.date }}</h4>
        <div v-if="event.files">
            <div v-for="file in event.files" :key="file.id">
                <EventFile :file="file.event_file" />
            </div>
        </div>
        <div v-html="event.info"></div>
    </div>
</template>

<script>
import EventFile from '../partials/EventFile.vue';

export default {
    components: {
        EventFile
    },
    props: ['event']
}
</script>