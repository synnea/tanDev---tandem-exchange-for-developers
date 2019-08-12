$(document).ready(function () {

    // Activate sidebar toggle functionality

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

    // Change navbar class to static-top.

    $(function() {
    $("#navbar").removeClass("fixed-top").addClass("static-top");
    })


});