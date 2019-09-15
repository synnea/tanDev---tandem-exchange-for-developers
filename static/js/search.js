$(document).ready(function () {

    // Activate sidebar toggle functionality


    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active', 500);
    });

    if ($(window).width() <= 800) {
        $(".search-card").addClass("d-none");
    }

    // Call the same functions upon window resize.

    $(window).on('resize', function () {

        if ($(window).width() <= 800) {

            $(".search-card").addClass("d-none");
        }
    });


});