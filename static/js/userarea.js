$('no-rate').click(function () {
    if ($("input:radio[class='no-rate']").is(":checked")) {
        $(this).css("background-color", "yellow")
    }
});