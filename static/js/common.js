
$(document).ready(function () {


    // Upon the document loading, assign two different navbar styles  to width below and above 800.
    // Below 800, assign a static top class. Above 800, assign a transparent background that picks up color after the user has scrolled for 20 pixels.

    if ($(window).width() < 800) {
        $("#navbar").removeClass("fixed-top").addClass("static-top");
    } else {
        $(window).scroll(function () {
            $("nav").toggleClass('scrolled', $(this).scrollTop() > 20);
            $(".nav-link").toggleClass('scrolled', $(this).scrollTop() > 20);
        });
    }

    // Call the same functions upon window resize.

    $(window).on('resize', function () {

        if ($(window).width() <= 800) {
            $("#navbar").removeClass("fixed-top").addClass("static-top");
        } else {
            $("#navbar").removeClass("static-top").addClass("fixed-top");

            $(window).scroll(function () {
                $("nav").toggleClass('scrolled', $(this).scrollTop() > 50);
                $(".nav-link").toggleClass('scrolled', $(this).scrollTop() > 50);
            });
        }
    });

});