// Runs in <head> before first paint: flag that JS is on, then apply the saved theme.
// Light is the default look; a visitor's saved choice ("light" or "dark") wins.
document.documentElement.classList.add('js');
document.documentElement.dataset.theme = 'light';
try { const t = localStorage.getItem('theme'); if (t === 'dark' || t === 'light') document.documentElement.dataset.theme = t; } catch (e) {}
