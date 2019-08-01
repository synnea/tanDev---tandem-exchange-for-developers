
// Changes the color of the navbar once the user has scrolled down for 100 pixels.

$(document).ready(function () {

$( window ).scroll(function() {
    $("nav").toggleClass('scrolled', $(this).scrollTop() > 100);
    $(".nav-link").toggleClass('scrolled', $(this).scrollTop() > 100);
});

});