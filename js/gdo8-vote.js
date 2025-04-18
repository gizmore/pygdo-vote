document.querySelectorAll('.gdt-stars').forEach(starbox => {
  const stars = starbox.querySelectorAll('span');
  const input = starbox.querySelector('input');

  function setStars(val) {
    stars.forEach(star => {
      star.textContent = parseInt(star.dataset.value) <= val ? '★' : '☆';
      star.classList.toggle('selected', parseInt(star.dataset.value) === val);
    });
    input.value = val;
  }

  stars.forEach(star => {
    star.addEventListener('mouseover', () => {
      const val = parseInt(star.dataset.value);
      stars.forEach(s => s.textContent = parseInt(s.dataset.value) <= val ? '★' : '☆');
    });
    star.addEventListener('mouseout', () => {
      setStars(parseInt(input.value));
    });
    star.addEventListener('click', () => {
      setStars(parseInt(star.dataset.value));
    });
  });

  // Init
  setStars(parseInt(input.value));
});