// Add the class of active to the first carousel item upon load. This solution was also taken from Anna Greaves' FamilyHub project.


document.addEventListener("DOMContentLoaded", function () {
    $('#index-carousel .carousel-item:first').addClass('active');
});


