// M.AutoInit();
let message = "welcome"
$(document).ready(function(){
  $('.parallax').parallax();
});

$(document).ready(function(){
  $('.sidenav').sidenav();
});

$(document).ready(function(){
  $('.collapsible').collapsible();
});
      
message +='/hjere'
   
// alert(message);


// all fading shit
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
  
  message+="/fade"
  // alert(message);

// Overwrite scrollOffset option for scrollspy to 0px
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.scrollspy');
    var instances = M.ScrollSpy.init(elems, {scrollOffset: 0});
});

message+="/scroll"


//fixes issues with sidenav not reloading tabs in menu
const menuItems = document.querySelectorAll("#mobile-links a.loadMenu");
menuItems.forEach(element => {
  element.addEventListener('click', () => {
    $('.sidenav').sidenav('close');
    setTimeout(() => {
      location.reload();
    }, 30);
  });
});

// message+="/menu"

const homeNavItems = document.querySelectorAll("#mobile-links a.closeNav");
homeNavItems.forEach(element => {
  element.addEventListener('click', () => {
    $('.sidenav').sidenav('close');
  });
});

// alert(message);

// const p = document.querySelector('.test #p');
// const but = document.querySelector('.test #but')
// but.addEventListener('click', function() {
//   p.innerText = 'helo'
// });

// const butt = document.querySelector('.test #butt')
// butt.addEventListener('click', () => {
//   p.innerText = 'helo2'
// });


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
    var aTags = document.getElementsByTagName('a');
    //console.log(aTags.length);
    for (i = 0; i < aTags.length; i++){
        //console.log(aTags[i].innerText);
        if (aTags[i].innerText.includes('Free Google Reviews widget')){
            aTags[i].remove();
            //console.log('hi');
        }

        if (aTags[i].innerText.includes('Widget is deactivated. Please, visit Elfsight Apps.')){
            aTags[i].remove();
            //console.log('hi');
        }

    }
}
