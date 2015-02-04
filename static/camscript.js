//
//camera settings
//
function init_camsettings() {
    $.ajax({
        type: "GET",
        url: "http://192.168.1.199/cmd_pipe.php?cmd=px 1296 976 25 25 2592 1944"
    });
    $.ajax({
        type: "GET",
        url: "http://192.168.1.199/cmd_pipe.php?cmd=an %20"
    });
}



//
// MJPEG
//
var mjpeg_img;
function reload_img () {
    mjpeg_img.src = "http://192.168.1.199/cam_pic.php?time=" + new Date().getTime();
}
function error_img () {
    setTimeout("mjpeg_img.src = 'http://192.168.1.199/cam_pic.php?time=' + new Date().getTime();", 100);
}



//
//reboot, shutdown, camera off
//just for personal use; aware of security flaw
$(document).keydown(function (event) {
    if (event.keyCode == 38) {
        $.ajax({
            type: "GET",
            url: "http://192.168.1.199/cmd_func.php?cmd=reboot"
        });
    }
    else if (event.keyCode == 39) {
        $.ajax({
            type: "GET",
            url: "http://192.168.1.199/cmd_pipe.php?cmd=ru 0"
        });
    }
});



//
// init
//
init_camsettings();
function init() {
    mjpeg_img = document.getElementById("mjpeg_dest");
    mjpeg_img.onload = reload_img;
    mjpeg_img.onerror = error_img;
    reload_img();

}



//todo: instead of pressing keys, have buttons for controls
//todo: make a camera settings page (maybe)