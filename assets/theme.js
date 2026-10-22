// Runs in <head> before first paint: flag that JS is on, then apply a saved theme.
// With no saved choice, the visitor's OS light/dark setting applies through CSS.
document.documentElement.classList.add('js');
try { const t = localStorage.getItem('theme'); if (t) document.documentElement.dataset.theme = t; } catch (e) {}
