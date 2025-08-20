// Smooth scroll for nav links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth"
    });
  });
});

// Fade-in animation on scroll
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("fade-in");
    }
  });
}, { threshold: 0.2 });

document.querySelectorAll(".section").forEach(section => {
  observer.observe(section);
});

// Typing effect for your title
const typingText = "Senior Product Manager · AI/ML";
let i = 0;
function typeWriter() {
  if (i < typingText.length) {
    document.getElementById("typing-title").innerHTML += typingText.charAt(i);
    i++;
    setTimeout(typeWriter, 100);
  }
}
document.addEventListener("DOMContentLoaded", typeWriter);

// Dark mode toggle
const toggle = document.getElementById("dark-toggle");
toggle.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
});
