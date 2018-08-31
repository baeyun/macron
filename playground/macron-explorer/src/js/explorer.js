/* @macron es5 */

var main = document.getElementById('main');
var accessors = document.querySelectorAll('[data-access]');
var keys = document.querySelectorAll('[data-key]');

accessors.forEach(function(a) {
  a.addEventListener('click', function(e) {
    // console.log(a.getAttribute('data-access'))
    // Only first instance counts as querySelector()
    main.innerHTML = document.querySelector('[data-key=' + a.getAttribute('data-access') + ']').innerHTML;
  })
})