const counters = document.querySelectorAll(".counter-container span");
const container = document.querySelector(".counter-container");
let activated = false;

window.addEventListener("scroll", () => {
  if (
    pageYOffset > container.offsetTop - container.offsetHeight - 200 &&
    activated === false
  ) {
    counters.forEach((counter) => {
      counter.innerText = 0;

      let count = 0;
      function updateCount() {
        const target = parseInt(counter.dataset.count);
        if (count < target) {
          count++;
          counter.innerText = count;
          setTimeout(updateCount, 100);
        } else {
          counter.innerText = target;
        }
      }
      updateCount();
      activated = true;
    });
  } else if (
    pageYOffset < container.offsetTop - container.offsetHeight - 500 ||
    (pageYOffset === 0 && activated === true)
  ) {
    counters.forEach((counter) => {
      counter.innerText = 0;
    });
    activated = false;
  }
});

const swiper = new Swiper(document.querySelector(".mySwiper"), {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    bulletActiveClass: "active",
  },
});
