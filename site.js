(() => {
  const button = document.querySelector('.menu-btn');
  const nav = document.querySelector('.main-nav');
  if (!button || !nav) return;
  const close = () => { nav.classList.remove('open'); button.setAttribute('aria-expanded','false'); };
  button.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    button.setAttribute('aria-expanded', String(open));
  });
  nav.addEventListener('click', e => { if (e.target.closest('a')) close(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  document.addEventListener('click', e => { if (!nav.contains(e.target) && !button.contains(e.target) && nav.classList.contains('open')) close(); });
})();
