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
    featuredGrid.innerHTML = sampleItems
      .map(
        (item) => `
          <article class="card">
            <h3 class="card-title">${item.title}</h3>
            <p class="card-meta">by ${item.author}</p>
          </article>
        `
      )
      .join('');
  }
});
