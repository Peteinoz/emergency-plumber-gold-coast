/* Moyle Plumbing site: mobile nav toggle and click-to-load video facade. */
(function () {
  'use strict';
  document.documentElement.classList.add('js');

  var btn = document.querySelector('.nav-btn');
  var nav = document.getElementById('site-nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  var facades = document.querySelectorAll('.video[data-video-id]');
  Array.prototype.forEach.call(facades, function (box) {
    var play = box.querySelector('.video-btn');
    if (!play) { return; }
    play.addEventListener('click', function () {
      var id = box.getAttribute('data-video-id');
      var title = box.getAttribute('data-video-title') || 'Video';
      var frame = document.createElement('iframe');
      frame.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?autoplay=1&rel=0';
      frame.title = title;
      frame.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
      frame.setAttribute('allowfullscreen', '');
      box.innerHTML = '';
      box.appendChild(frame);
    });
  });
})();
