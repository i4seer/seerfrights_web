(() => {
  const button = document.querySelector('.menu-btn');
  const nav = document.querySelector('.main-nav');
  if (!button || !nav) return;
  button.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    button.setAttribute('aria-expanded', String(open));
  });
  nav.addEventListener('click', (event) => {
    if (event.target.closest('a')) {
      nav.classList.remove('open');
      button.setAttribute('aria-expanded', 'false');
    }
  });
})();
