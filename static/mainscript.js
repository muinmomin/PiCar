var allowed = true;

$(document).ready(function(){

    $(document).keydown(function(event) {
        if(event.charCode == 0 && event.keyCode==0) {
            return false;
        }
        //moving forward
        if(event.keyCode == 87) {
            if(allowed) {
                $.ajax({
                    type: "POST",
                    url: "/motorforward"
                });
                allowed = false;
            }
        }
        //reversing
        else if(event.keyCode == 83) {
            if(allowed) {
                $.ajax({
                    type: "POST",
                    url: "/motorreverse"
                });
                allowed = false;
            }
        }
        //showing distance
        else if(event.keyCode == 32) {
            if (allowed) {
                $.getJSON("/distance", function(jd) {
                    $("#distance").text(jd.dist);
                });
                allowed = false;
            }
        }
        else if(event.keyCode == 65 || event.keyCode == 68) {
            if (allowed) {
                $.ajax({
                   type: "POST",
                    url: "/turnleft"
                });
            }
        }
    });


    $(document).keyup(function(event) {
        if(event.charCode == 0 && event.keyCode==0) {
            return false;
        }
        if(event.keyCode == 87)
        {
            $.ajax({
                type: "POST",
                url: "/motorforwardstop"
            });
        }
        else if(event.keyCode == 83)
        {
            $.ajax({
                type: "POST",
                url: "/motorreversestop"
            });
        }
        else if(event.keyCode == 65 || event.keyCode == 68) {
            $.ajax({
                type: "POST",
                url: "/stopleft"
            });
        }
        allowed = true;
    });


});