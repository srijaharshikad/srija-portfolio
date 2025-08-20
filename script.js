// Dark mode preference
const pref = localStorage.getItem('theme');
if (pref === 'dark' || (!pref && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  document.documentElement.classList.add('dark');
}
document.getElementById('themeToggle')?.addEventListener('click', () => {
  document.documentElement.classList.toggle('dark');
  localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
});

// Metric counters
function animateCounts() {
  document.querySelectorAll('[data-count]').forEach(el => {
    const end = parseFloat(el.getAttribute('data-count'));
    const duration = 1200;
    const start = 0;
    const t0 = performance.now();
    const step = (now) => {
      const t = Math.min((now - t0) / duration, 1);
      const val = Math.floor(t * (end - start) + start);
      el.textContent = `${val}`;
      if (t < 1) requestAnimationFrame(step);
      else el.textContent = `${end}`;
    };
    requestAnimationFrame(step);
  });
}
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { animateCounts(); observer.disconnect(); } });
}, { threshold: 0.3 });
document.querySelectorAll('[data-count]').forEach(el => observer.observe(el));

document.getElementById('year').textContent = new Date().getFullYear();
