var body = document.querySelector("body");
var modal = document.querySelector(".modal");
var modalButton = document.querySelector(".modal-button");
var closeButton = document.querySelector(".close-button");
var scrollDown = document.querySelector(".scroll-down");
var isOpened = false;

var openModal = function openModal() {
  modal.classList.add("is-open");
  body.style.overflow = "hidden";
};

var closeModal = function closeModal() {
  modal.classList.remove("is-open");
  body.style.overflow = "initial";
};

window.addEventListener("scroll", function () {
  if (window.scrollY > window.innerHeight / 3 && !isOpened) {
    isOpened = true;
    scrollDown.style.display = "none";
    openModal();
  }
});

modalButton.addEventListener("click", openModal);
closeButton.addEventListener("click", closeModal);

document.onkeydown = function (evt) {
  evt = evt || window.event;
  evt.keyCode === 27 ? closeModal() : false;
};