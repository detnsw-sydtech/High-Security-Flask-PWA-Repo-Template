/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/app/templates/**/*.html",
    "./src/app/static/js/**/*.js",
    "./docs/**/*.md"
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        sths: {
          navy: "var(--sths-navy)",
          gold: "var(--sths-gold)",
          light: "var(--sths-light)",
          dark: "var(--sths-dark)"
        }
      },
      borderRadius: {
        sm: "var(--radius-sm)",
        md: "var(--radius-md)",
        lg: "var(--radius-lg)"
      },
      boxShadow: {
        card: "var(--shadow-card)"
      }
    }
  },
  plugins: []
};
