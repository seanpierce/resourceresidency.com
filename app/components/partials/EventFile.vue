<template>
    <div class="event-file">
        <div v-if="type === 'video'">
            <video controls :src="'media/' + file" />
        </div>
        <div v-if="type === 'image'">
            <img :src="'media/' + file" />
        </div>
    </div>
</template>

<script>
export default {
    props: ['file'],
    data() {
        return {
            extension: null,
        }
    },
    computed: {
        type() {
            if (this.isImage(this.extension))
                return 'image';

            if (this.isVideo(this.extension))
                return 'video';

            return null;
        }
    },
    methods: {
        getFileType(path) {
            var splitPath = path.split('.');
            this.extension =  splitPath[splitPath.length - 1];
        },
        isImage(extension) {
            var imageTypes = ['png', 'jpg', 'jpeg', 'gif']
            return imageTypes.indexOf(extension) > -1;
        },
        isVideo(extension) {
            var videoTypes = ['mov', 'mp4']
            return videoTypes.indexOf(extension) > -1;
        }
    },
    mounted() {
        this.getFileType(this.file);
    }
}
</script>