(() => {
  // Mobile nav toggle
  const button = document.querySelector('.menu-btn');
  const nav = document.querySelector('.main-nav');
  if (button && nav) {
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
  }

  // Hand-drawn "SEER FRIGHTS" wordmark — drawn to match the book covers
  // (Anton petite caps + irregular drips). Injected as progressive enhancement:
  // the CSS text lock-up in .brand / .footer-logo stays as the no-JS fallback.
  const WORDMARK =
    '<svg class="sf-wordmark" viewBox="0 0 300 52" role="img" aria-label="Seer Frights" xmlns="http://www.w3.org/2000/svg">' +
    '<g fill="currentColor">' +
    '<text x="4" y="44" textLength="292" lengthAdjust="spacingAndGlyphs" font-family="Anton, Impact, \'Arial Narrow Bold\', sans-serif">' +
    '<tspan font-size="46">S</tspan><tspan font-size="33">EER</tspan><tspan font-size="46"> F</tspan><tspan font-size="33">RIGHTS</tspan>' +
    '</text>' +
    '<path d="M9 6c-1.3 0-2.2 1.4-2.2 5.5S7.7 17 9 17s2.2-1.4 2.2-5.5S10.3 6 9 6z"/>' +
    '<path d="M150 8c-1.1 0-1.8 1.1-1.8 4.5s.7 4.5 1.8 4.5 1.8-1.1 1.8-4.5S151.1 8 150 8z"/>' +
    '<path d="M230 10c-.9 0-1.5.9-1.5 3.5s.6 3.5 1.5 3.5 1.5-.9 1.5-3.5-.6-3.5-1.5-3.5z"/>' +
    '<path d="M10 40c-2.1 0-3.2 2.8-3.2 10.5 0 7.6 1.1 10.5 1.1 15.8 0 4 4.2 4 4.2 0 0-5.3-1.1-8.2-1.1-15.8 0-6.7 1.1-10.5-1-10.5z"/>' +
    '<path d="M33 41c-1.2 0-2 2.2-2 7 0 4.3 1.1 6 1.1 9.8 0 2.8 3 2.8 3 0 0-3.8-.7-5.5-.7-9.8 0-4.1.8-7-1.4-7z"/>' +
    '<path d="M52 41.5c-1.1 0-1.9 2.8-1.9 8 0 5.8 1.7 7.5 1.7 12.2 0 2.8 2.8 2.8 2.8 0 0-4.7-.9-6.4-.9-12.2 0-4.7.6-8-1.7-8z"/>' +
    '<path d="M73 41c-1.2 0-2 1.9-2 5.6 0 4.1 1.3 5.3 1.3 9 0 2.8 3 2.8 3 0 0-3.7-.5-4.9-.5-9 0-3.7.7-5.6-1.8-5.6z"/>' +
    '<path d="M92 39.5c-2.1 0-3.2 2.8-3.2 11.5 0 8.6 1.3 11.5 1.3 17.2 0 4.2 4.2 4.2 4.2 0 0-5.7-1.3-8.6-1.3-17.2 0-7.7 1.1-11.5-1.9-11.5z"/>' +
    '<path d="M109 41c-1.1 0-1.8 2.8-1.8 9 0 7.1 1.7 9 1.7 14.2 0 3 3 3 3 0 0-5.2-.9-7-.9-14.2 0-6.2.5-9-1.6-9z"/>' +
    '<path d="M130 39.5c-2.1 0-3.2 2.8-3.2 10.5 0 7.6 1.3 10.5 1.3 16.2 0 4 4.2 4 4.2 0 0-5.7-1.1-8.6-1.1-16.2 0-6.7.9-10.5-1.7-10.5z"/>' +
    '<path d="M149 41c-1.2 0-2 2.2-2 7.2 0 4.7 1.3 6.6 1.3 10.8 0 2.8 3 2.8 3 0 0-4.2-.6-6-.6-10.8 0-4.2.8-7.2-1.7-7.2z"/>' +
    '<path d="M170 41c-1.1 0-1.8 2.8-1.8 8 0 5.8 1.7 7.5 1.7 12.2 0 2.8 2.8 2.8 2.8 0 0-4.7-.9-6.4-.9-12.2 0-4.7.4-8-1.5-8z"/>' +
    '<path d="M190 41c-1.1 0-1.8 2-1.8 6 0 4.3 1.3 5.6 1.3 9.4 0 2.8 2.8 2.8 2.8 0 0-3.8-.5-5.1-.5-9.4 0-3.7.7-6-1.5-6z"/>' +
    '<path d="M211 41c-1.2 0-2 2.8-2 8.4 0 6.6 1.5 8.4 1.5 13.6 0 2.8 3 2.8 3 0 0-5.2-.8-7-.8-13.6 0-5.6.7-8.4-1.5-8.4z"/>' +
    '<path d="M233 39.5c-2.1 0-3.2 2.8-3.2 10.5 0 7.6 1.3 10.5 1.3 15.8 0 4 4.2 4 4.2 0 0-5.3-1.1-8.2-1.1-15.8 0-6.7.9-10.5-1.7-10.5z"/>' +
    '<path d="M254 41c-1.1 0-1.8 2.8-1.8 8 0 5.8 1.7 7.5 1.7 12.2 0 2.8 2.8 2.8 2.8 0 0-4.7-.9-6.4-.9-12.2 0-4.7.4-8-1.5-8z"/>' +
    '<path d="M274 41c-1.2 0-2 2.2-2 7.2 0 4.7 1.3 6.6 1.3 10.8 0 2.8 3 2.8 3 0 0-4.2-.6-6-.6-10.8 0-4.2.8-7.2-1.7-7.2z"/>' +
    '<path d="M291 41c-1.1 0-1.8 2.8-1.8 8.4 0 6.6 1.6 8.4 1.6 13.2 0 2.8 2.8 2.8 2.8 0 0-4.8-.8-6.6-.8-13.2 0-5.6.4-8.4-1.5-8.4z"/>' +
    '<circle cx="11" cy="68" r="2.5"/><circle cx="93" cy="71" r="2.7"/><circle cx="131" cy="69" r="2.5"/><circle cx="234" cy="68" r="2.3"/>' +
    '</g></svg>';

  document.querySelectorAll('.brand, .footer-logo').forEach((el) => {
    el.classList.add('has-wordmark');
    el.innerHTML = WORDMARK;
  });
})();
