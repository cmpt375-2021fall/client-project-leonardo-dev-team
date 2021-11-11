    // When the user scrolls down 50px from the top of the document, resize the header's font size
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
      if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        document.getElementById("header").style.backgroundColor = "white";
      } else {
        document.getElementById("header").style.backgroundColor = "transparent";
      }
    }
function dropdown() {
  var x = document.getElementById("button");
      if (x.style.display === "block") {
        x.style.display = "none";
      } else {
        x.style.display = "block";
        document.getElementById("header").style.backgroundColor = "white";
      }
}