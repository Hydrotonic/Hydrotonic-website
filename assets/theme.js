// Runs in <head> before first paint: flag that JS is on, then apply the saved theme.
// Dark is the default look; a visitor's saved choice ("light" or "dark") wins.
document.documentElement.classList.add('js');
try { const t = localStorage.getItem('theme'); if (t) document.documentElement.dataset.theme = t; } catch (e) {}
