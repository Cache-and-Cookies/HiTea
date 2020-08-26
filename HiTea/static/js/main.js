M.AutoInit();

// all fading shit
const faders = document.querySelectorAll('.fade-in');
const appearOptions = {
    threshold: 0,
    rootMargin: "0px 0px -200px 0px"
  };
const appearOnScroll = new IntersectionObserver(function(
    entries,
    appearOnScroll
  ) {
    entries.forEach(entry => {
      if (!entry.isIntersecting) {
        return;
      } else {
        entry.target.classList.add("appear");
        appearOnScroll.unobserve(entry.target);
      }
    });
  },
  appearOptions);
  
  faders.forEach(fader => {
    appearOnScroll.observe(fader);
  });


// Overwrite scrollOffset option for scrollspy to 0px
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.scrollspy');
    var instances = M.ScrollSpy.init(elems, {scrollOffset: 0});
});

//fixes issues with sidenav not reloading tabs in menu
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems, {
    onCloseEnd: function() {
      location.reload();
    }
  });
});

// Constantly updates copyright message in footer
var date = new Date()
var copyrightMsg = document.getElementById("copyright")
copyrightMsg.innerText = "HiTea " + date.getFullYear() + " \u00A9 All rights reservered"

// Alerts user after contact form has been successfully submitted
function contactFormAlert(){
    alert("Contact Form Successful Submitted!")
}

// Removing Elfsight Cover
function removeCover(){
    var aTags = document.getElementsByTagName('a')
    for (i = 0; i < aTags.length; i++){
        if (aTags[i].textContent == 'Widget is deactivated. Please, visit Elfsight Apps.'){
            console.log(aTags[i]);
            aTags[i].remove();
            break;
        }
    }
}