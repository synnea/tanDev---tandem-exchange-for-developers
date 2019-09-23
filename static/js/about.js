$(document).ready(function () {

    // initialize the scroll animations.

  $(function () {
    AOS.init();
  });

    // pushes down the overlay to prevent it from overlapping the menu options.

  $(function () {
    $('#hamburger').on("click", function () {
      $("#about-overlay").toggleClass("overlay-open");
    });
  });

});