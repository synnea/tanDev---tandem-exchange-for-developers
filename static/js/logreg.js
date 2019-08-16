$(document).ready(function () {


    // Change navbar class to static-top.


    $(function () {
        $("#navbar").removeClass("fixed-top").addClass("static-top");
    });

    // Saves the current tab into local storage so that the same tab is displayed after refreshing the page.
    // Used to prevent the browser to re-attach the 'active' class to the login tab after refreshing from the register tab.
    // Code taken from https://stackoverflow.com/questions/50423148/keep-active-tab-on-page-refresh-in-bootstrap-4-using-local-storage.

    $(function() {
        $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
            localStorage.setItem('activeTab', $(e.target).attr('href'));
        });
        
        var activeTab = localStorage.getItem('activeTab');
        if(activeTab){
            $('.nav-tabs a[href="' + activeTab + '"]').tab('show');
        }
    });

    // The following two functions hide the flash messages when the login/register tabs are being switched.

    $(function() {
        $('#register-tab').on("click", function() {
            $(".flashes").hide();
        })
    });

    $(function() {
        $('#login-tab').on("click", function() {
            $(".flashes").hide();
        })
    });

});
