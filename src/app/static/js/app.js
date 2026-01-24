document.addEventListener('DOMContentLoaded', () => {
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.getElementById('nav-menu');
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      const expanded = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', String(!expanded));
      navMenu.classList.toggle('nav-menu--open', !expanded);
    });
  }

  const featuredGrid = document.getElementById('featured-grid');
  if (featuredGrid) {
    // Example dynamic content injection (replace with real API later)
    const sampleItems = [
      { title: 'Clean Code', author: 'Robert C. Martin' },
      { title: 'Designing Data-Intensive Applications', author: 'Martin Kleppmann' },
    ];

    // Clear any existing content safely
    featuredGrid.textContent = '';

    // Gold-standard secure DOM construction
    sampleItems.forEach((item) => {
      const article = document.createElement('article');
      article.className = 'card';

      const title = document.createElement('h3');
      title.className = 'card-title';
      title.textContent = item.title; // SAFE: escapes HTML

      const meta = document.createElement('p');
      meta.className = 'card-meta';
      meta.textContent = `by ${item.author}`; // SAFE: escapes HTML

      article.appendChild(title);
      article.appendChild(meta);
      featuredGrid.appendChild(article);
    });
  }
});
