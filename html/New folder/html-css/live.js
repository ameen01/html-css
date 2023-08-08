// create a variable for the video player element
var player = document.getElementById("video-player");

// check if the browser supports the video element
if (player.canPlayType) {
    // set the source of the video
    player.src = "http://example.com/livestream.mp4";
    // load the video
    player.load();
    // play the video
    player.play();
}
