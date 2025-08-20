// Dark mode preference
const pref = localStorage.getItem('theme');
if (pref === 'dark' || (!pref && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  document.documentElement.classList.add('dark');
}
document.getElementById('themeToggle')?.addEventListener('click', () => {
  document.documentElement.classList.toggle('dark');
  localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
});

// Animated metric counters
function animateCounts() {
  document.querySelectorAll('[data-count]').forEach(el => {
    const end = parseFloat(el.getAttribute('data-count'));
    const start = 0, duration = 1200, t0 = performance.now();
    const step = (now) => {
      const t = Math.min((now - t0) / duration, 1);
      el.textContent = String(Math.floor(start + (end - start) * t));
      if (t < 1) requestAnimationFrame(step); else el.textContent = String(end);
    };
    requestAnimationFrame(step);
  });
}
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { animateCounts(); io.disconnect(); } });
}, { threshold: 0.3 });
document.querySelectorAll('[data-count]').forEach(el => io.observe(el));

// Footer year
document.getElementById('year').textContent = new Date().getFullYear();
