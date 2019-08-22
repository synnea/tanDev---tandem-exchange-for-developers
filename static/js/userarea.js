$(document).ready(function () {

    $(".skill-options").hide();

    $(function() {
    $("#python-box").on("click", function () {
        $("#python-options").slideToggle();
    });
});

$(function() {
    $("#sql-box").on("click", function () {
        $("#sql-options").slideToggle();
    });
});
});