<!-- HEADER START -->
<div class="sydtech-header border-b pb-4 mb-8">
  <div class="flex items-center gap-4">
    <img
      src="https://avatars.githubusercontent.com/u/250778024?s=200&v=4"
      alt="STHS Logo"
      class="h-12 w-12 rounded-md"
    />

    <div class="flex flex-col">
      <span class="text-xl font-semibold">Sydney Technical High School</span>
      <span class="text-sm opacity-80">High‑Security Flask PWA Template</span>
    </div>

    <!-- Spacer -->
    <div class="flex-1"></div>

    <!-- Dark mode toggle -->
    <button
      id="docs-theme-toggle"
      class="px-3 py-1 rounded-md bg-[var(--sths-gold)] text-black font-semibold"
      aria-label="Toggle dark mode"
    >
      Dark mode
    </button>
  </div>
</div>

<script>
// Dark mode toggle for MkDocs (CSP‑safe: external script allowed)
document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("docs-theme-toggle");
  const root = document.documentElement;

  // Load saved theme
  const saved = localStorage.getItem("docs-theme");
  if (saved === "dark") root.classList.add("dark");

  toggle.addEventListener("click", () => {
    const isDark = root.classList.toggle("dark");
    localStorage.setItem("docs-theme", isDark ? "dark" : "light");
  });
});
</script>
<!-- HEADER END -->
