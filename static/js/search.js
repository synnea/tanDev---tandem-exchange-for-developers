$(document).ready(function () {

    // Activate sidebar toggle functionality

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active', 500);
    });

    // Change navbar class to static-top.

    $(function () {
        $("#navbar").removeClass("fixed-top").addClass("static-top");
    });


    // Activate the custom multiple select dropdown picker.

    $(function () {
        $('select').selectpicker();
    });



    $(function () {
        $('select').selectpicker();
    });

    // Clear the selected items in the dropdown menus on the search page.

    $(function () {



        $('#districtRefresh').on("click", function () {
            var itemSelectorOption = $('#districtSelect.selectpicker option:selected');
            itemSelectorOption.remove();
            $('#districtSelect').selectpicker('refresh');
        })

    });


});