$(document).ready(function () {

    // Activate sidebar toggle functionality

    if ($(window).width() > 800) {
        $('sidebar').removeClass('active');
    }

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

});
