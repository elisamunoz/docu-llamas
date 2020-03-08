$(document).ready(function() {
    $(window).scroll(fixedNavBar);
  });

function showField(id) {
    const fieldWrapper = $("#" + id);
    const field = $("#pattern_" + id);

    fieldWrapper.fadeIn(1000);
    field.attr("required", true);
}
function hiddeField(id) {
    const fieldWrapper = $("#" + id);
    const field = $("#pattern_" + id);

    fieldWrapper.fadeOut(1000);
    field.attr("required", false);
}

function filterCardsByCategory() {
    var cardsList = document.getElementById("cards");
    var categorySelect = document.getElementById("category");
    var category = categorySelect.options[categorySelect.selectedIndex].value;
    
    if(category === '') {
        $(cardsList).find('.card_wrapper').fadeIn(0);
    } else {
        $(cardsList).find('.card_wrapper').fadeOut(0);
        $(cardsList).find(`.card_wrapper[data-category='${category}']`).fadeIn(1000);
    }
}

// Fades out and set to no required no needed elements in addpattern.html`
function fadeOutElementPattern(){
    var categorySelect = document.getElementById("category");
    var category = categorySelect.options[categorySelect.selectedIndex].value;

    showField("needle_size");
    showField("gauge");
    showField("yarn_weight");
    showField("yardage");
    showField("size");
    showField("difficulty");

    switch(category) {
        case "sewing":
            hiddeField("gauge");
            hiddeField("needle_size");
        break;
        case "article":
            hiddeField("needle_size");
            hiddeField("gauge");
            hiddeField("yarn_weight");
            hiddeField("yardage");
            hiddeField("size");
            hiddeField("difficulty");
            break;
        default:
            break;
    }
};

// Navbar to fixed

function fixedNavBar() {
    if ($(this).scrollTop() > 500) {
      $(".navbar").addClass("fixed");
    } else {
      $(".navbar").removeClass("fixed");
    }
  }

