$(document).ready(function() {
    $(window).scroll(fixedNavBar);
    parallaxContent();
  });


// Navbar to fixed

function fixedNavBar() {
  if ($(this).scrollTop() > 200) {
    $(".navbar").addClass("navbar-small");
    $(".navbar-brand").addClass("navbar-brand-small");
    $(".navbar-brand").addClass("navbar-smaller-font");
  } else {
    $(".navbar").removeClass("navbar-small");
    $(".navbar-brand").removeClass("navbar-brand-small");
    $(".navbar-brand").removeClass("navbar-smaller-font");
  }
}


// Parallax effect

function parallaxContent() {
  const parllax = document.querySelector(".parallax");

  window.addEventListener("scroll", function() {
    let offset = window.pageYOffset;

    if(!!parllax) {
      parllax.style.backgroundPositionY = offset * 0.5 + "px";
    }
  });
}


// Fades out and set to no required no needed elements in addpattern.html and editpattern.html
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


// Shows required fields used in Add-EditPattern page

function showField(id) {
  const fieldWrapper = $("#" + id);
  const field = $("#pattern_" + id);

  fieldWrapper.fadeIn(1000);
  field.attr("required", true);
}

// Hides not required fields used in Add-EditPattern page

function hiddeField(id) {
  const fieldWrapper = $("#" + id);
  const field = $("#pattern_" + id);

  fieldWrapper.fadeOut(1000);
  field.attr("required", false);
}




