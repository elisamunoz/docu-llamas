

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

function fadeOutCards() {
    var categorySelect = document.getElementById("category")
    var category = categorySelect.options[categorySelect.selectedIndex].value;

    if (category == "knitting"){
        console.log("knitting")
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
    

