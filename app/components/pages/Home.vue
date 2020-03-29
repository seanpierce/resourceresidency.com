<template>
    <div id="home">
        <div id="twitch-stream"></div>
        <img src="/assets/images/somekindofshow.jpg" alt="" style="width:100%">
        <div id="temp-logos">
            <img src="/assets/images/calexo_logo.png" alt="" style="transform:translateY(-100%)" onclick="window.location.href='https://calexo.co'">
            <img src="/assets/images/s1_logo.png" alt="" style="width:20%" onclick="window.location.href='https://s1portland.com/'">
        </div>
    </div>
</template>

<script>

export default {
    mounted() {
        new Twitch.Embed("twitch-stream", {
            width: '100%',
            height: 500,
            channel: "resourceresidency",
            layout: "video",
            autoplay: false,
            setFullscreen: true
        });
    }
}
</script>