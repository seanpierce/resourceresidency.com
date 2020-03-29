<template>
    <div id="events">
        <div v-if="upcomingEvents && upcomingEvents.length > 0">
            <h2>Upcoming</h2>
            <div v-for="event in upcomingEvents" :key="event.id">
                <Event :event="event" />
            </div>
        </div>
        <div v-if="pastEvents && pastEvents.length > 0">
            <h2>Past</h2>
            <div v-for="event in pastEvents" :key="event.id">
                <Event :event="event" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Event from '../partials/Event.vue';

export default {
    components: {
        Event
    },
    data() {
        return {
            upcomingEvents: null,
            pastEvents: null
        }
    },
    methods: {
        getEvents() {
            axios.get('/api/events')
                .then(response => {
                    this.upcomingEvents = response.data.filter(x => x.past === false);
                    this.pastEvents = response.data.filter(x => x.past === true);
                })
                .catch(error => {
                    console.log(error);
                })
        }
    },
    mounted() {
        this.getEvents();
    }
}
</script>