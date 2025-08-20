// Dark mode
const pref = localStorage.getItem('theme');
if (pref === 'dark' || (!pref && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  document.documentElement.classList.add('dark');
}
document.getElementById('themeToggle')?.addEventListener('click', () => {
  document.documentElement.classList.toggle('dark');
  localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
});

// Reveal-on-scroll
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('show'); }
  });
}, { threshold: 0.16 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Animated counters
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
const io2 = new IntersectionObserver((entries) => {
  if (entries.some(e => e.isIntersecting)) { animateCounts(); io2.disconnect(); }
}, { threshold: 0.3 });
document.querySelectorAll('[data-count]').forEach(el => io2.observe(el));

// Tabs (Work section)
const tabs = document.querySelectorAll('.tab');
const panes = document.querySelectorAll('.tabpane');
tabs.forEach(btn => btn.addEventListener('click', () => {
  tabs.forEach(b => b.classList.remove('bg-brand-600','text-white'));
  btn.classList.add('bg-brand-600','text-white');
  panes.forEach(p => p.classList.add('hidden'));
  const target = document.querySelector(btn.dataset.target);
  target.classList.remove('hidden');
  target.classList.add('show'); // ensure revealed
}));

// Footer year
document.getElementById('year').textContent = new Date().getFullYear();
