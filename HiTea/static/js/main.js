// M.AutoInit();
$(document).ready(function(){
  $('.parallax').parallax();
});

$(document).ready(function(){
  $('.sidenav').sidenav();
});

$(document).ready(function(){
  $('.collapsible').collapsible();
});

$(document).ready(function(){
  $('.tabs').tabs();
});

$(document).ready(function(){
  $('.modal').modal();
});
      

// Fade Effect
const faders = document.querySelectorAll('.fade-in');
const appearOptions = {
  threshold: 0,
  rootMargin: "0px 0px -100px 0px"
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
    let elems = document.querySelectorAll('.scrollspy');
    let instances = M.ScrollSpy.init(elems, {scrollOffset: 0});
});


//fixes issues with sidenav not reloading tabs in menu
const menuItems = document.querySelectorAll("#mobile-links a.loadMenu");
menuItems.forEach(element => {
  element.addEventListener('click', () => {
    $('.sidenav').sidenav('close');
    setTimeout(() => {
      location.reload();
    }, 100);
  });
});

const homeNavItems = document.querySelectorAll("#mobile-links a.closeNav");
homeNavItems.forEach(element => {
  element.addEventListener('click', () => {
    $('.sidenav').sidenav('close');
  });
});

// Constantly updates copyright message in footer
let date = new Date()
let copyrightMsg = document.getElementById("copyright")
copyrightMsg.innerText = "HiTea " + date.getFullYear() + " \u00A9 All rights reservered"

// Alerts user after contact form has been successfully submitted
function contactFormAlert(){
  alert("Contact Form Successful Submitted!")
}

// Removing Elfsight Cover
const body = document.getElementsByTagName("body")[0]
body.addEventListener("load", () => {
    for (let i = 0; i < 3; i++)
    removeCover()
})
function removeCover(){
  setTimeout(() => {
    const aTags = document.querySelectorAll('a');
    for (i = 0; i < aTags.length; i++){
      if (aTags[i].innerText.includes('Free Google Reviews widget')){
        aTags[i].remove();
      }

      if (aTags[i].innerText.includes('Widget is deactivated. Please, visit Elfsight Apps.')){
        aTags[i].remove();
      }
    }
  }, 1000);
}
