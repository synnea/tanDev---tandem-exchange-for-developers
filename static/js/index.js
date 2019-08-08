


document.addEventListener("DOMContentLoaded", function() {
    $('#index-carousel .carousel-item:first').addClass('active');
});


$(function () {
    $(".").on("click", function () {
        $(".main").hide();
        $(".dashboard-container").fadeIn(300);
       $(".content-container").removeClass("background");
    });
});
