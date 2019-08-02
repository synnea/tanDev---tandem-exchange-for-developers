// Changes the color of the navbar once the user has scrolled down for 100 pixels.

$(document).ready(function () {

    if ($(window).width() < 800) {
        $("#navbar").removeClass("fixed-top").addClass("static-top");
    } else {
        $(window).scroll(function () {
            $("nav").toggleClass('scrolled', $(this).scrollTop() > 100);
            $(".nav-link").toggleClass('scrolled', $(this).scrollTop() > 100);
        });
    }

    $(window).on('resize', function () {

        if ($(window).width() <= 800) {
            $("#navbar").removeClass("fixed-top").addClass("static-top");
        } else {
            $("#navbar").removeClass("static-top").addClass("fixed-top");

            $(window).scroll(function () {
                $("nav").toggleClass('scrolled', $(this).scrollTop() > 100);
                $(".nav-link").toggleClass('scrolled', $(this).scrollTop() > 100);
            });
        }
    });

});
