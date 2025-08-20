// Dark mode toggle + saved preference
const themeToggle = document.getElementById('themeToggle');
const root = document.documentElement;
const pref = localStorage.getItem('theme');
if (pref === 'dark' || (!pref && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  document.documentElement.classList.add('dark');
}
themeToggle?.addEventListener('click', () => {
  document.documentElement.classList.toggle('dark');
  localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
});

// Animated counters for spotlight metrics
function animateCounts() {
  document.querySelectorAll('[data-count]').forEach(el => {
    const end = parseFloat(el.getAttribute('data-count'));
    const isPercent = el.nextElementSibling?.textContent.includes('%');
    const duration = 1400;
    const start = 0;
    const startTime = performance.now();
    const step = (now) => {
      const t = Math.min((now - startTime) / duration, 1);
      const val = Math.floor(t * (end - start) + start);
      el.textContent = isPercent ? `${val}` : `${val}`;
      if (t < 1) requestAnimationFrame(step);
      else el.textContent = isPercent ? `${end}` : `${end}`;
    };
    requestAnimationFrame(step);
  });
}
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => { if (entry.isIntersecting) { animateCounts(); observer.disconnect(); } });
}, { threshold: 0.3 });
document.querySelectorAll('#projects [data-count]').forEach(el => observer.observe(el));

// Year in footer
document.getElementById('year').textContent = new Date().getFullYear();
