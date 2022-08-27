var messageBox = document.querySelector('.js-message');
  var btn = document.querySelector('.js-message-btn');
  var card = document.querySelector('.js-profile-card');
  var closeBtn = document.querySelectorAll('.js-message-close');
  var message  = document.getElementById("message")

  btn.addEventListener('click',function (e) {
      e.preventDefault();
      card.classList.add('active');
  });

  closeBtn.forEach(function (element, index) {
     console.log(element);
      element.addEventListener('click',function (e) {
          e.preventDefault();
          card.classList.remove('active');
      });
  });

  function show(){
    if (confirm("You are about to send a message to someone you don't know, please make sure you don't share any personal or confidential details, Enjoy your stay  #TSUMI!")) {
        txt = "Arlight Cool!";
      } else {
        txt = "OK sure😃!";
      }
  }