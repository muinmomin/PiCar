
$(document).ready(function() {

    // makes sure the device is in landscape orientation to ensure best live video feed quality
    function doOnOrientationChange() {
        switch(window.orientation)
        {
            case 0:
            case 180:
                document.getElementById('block_portrait').style.display = "block";
                break;
            default:
                document.getElementById('block_portrait').style.display = "none";
                break;
        }
    }

    $("#flash").click(function() {
        $.ajax({
            type: 'POST',
            url: '/flashled'
        });
    });

    window.addEventListener('orientationchange', doOnOrientationChange);
    doOnOrientationChange();

});













