$(document).ready(function () {


    // Hides the skill level checkboxes upon load.


    $(function () {
        $(".skill-options").hide();
    });

    // Function that toggles the next set of skill level checkboxes 
    // after a skill box has been selected.

    $(function () {
        $(".skill-field").on("click", function () {
            $(this).next(".skill-options").slideToggle("slow");
            return false;
        });
    
    });

});