/* Moyle Plumbing site: mobile nav toggle. */
(function () {
  'use strict';
  var btn = document.querySelector('.nav-btn');
  var nav = document.getElementById('site-nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

})();
