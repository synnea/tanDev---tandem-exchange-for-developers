$(document).ready(function () {

            // Activate sidebar toggle functionality


            if ($(window).width() <= 800) {
                $("#sidebar").removeClass("active");
                $('#content').removeClass('content-visibility');

                $('#sidebarCollapse').on('click', function () {
                    $('#sidebar').toggleClass('active', 500);
                    $('#content').toggleClass('content-visibility');
                });
            };


            if ($(window).width() > 800) {
                $("#sidebar").addClass("active");
                $('#content').removeClass('content-visibility');

            }


            $(window).on('resize', function () {

                if ($(window).width() <= 800) {
                    $("#sidebar").removeClass("active");
                    $('#content').removeClass('content-visibility');
    
                    $('#sidebarCollapse').on('click', function () {
                        $('#sidebar').toggleClass('active', 500);
                        $('#content').toggleClass('content-visibility');
                    });
                };

                if ($(window).width() > 800) {
                    $("#sidebar").addClass("active");
                    $('#content').removeClass('content-visibility');
    
                }
            });

        });



