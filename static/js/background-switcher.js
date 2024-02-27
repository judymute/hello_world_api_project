document.addEventListener("DOMContentLoaded", function() {
  var backgrounds = [
    '/static/images/chat-background-1.jpg',
    '/static/images/chat-background-2.jpg',
    '/static/images/chat-background-3.jpg',
    '/static/images/chat-background-4.jpg',
    '/static/images/chat-background-5.jpg',
    '/static/images/chat-background-6.jpg',
    '/static/images/chat-background-7.jpg',
    '/static/images/chat-background-8.jpg',
    '/static/images/chat-background-9.jpg',
    '/static/images/chat-background-10.jpg',
    '/static/images/chat-background-11.jpg',
    '/static/images/chat-background-12.jpg',
    '/static/images/chat-background-13.jpg',
    '/static/images/chat-background-14.jpg',
    '/static/images/chat-background-15.jpg',
    '/static/images/chat-background-16.jpg',
    '/static/images/chat-background-17.jpg',
    '/static/images/chat-background-18.jpg',

  ];
  var selectedBackground = backgrounds[Math.floor(Math.random() * backgrounds.length)];
  document.body.style.backgroundImage = 'url("' + selectedBackground + '")';
});
