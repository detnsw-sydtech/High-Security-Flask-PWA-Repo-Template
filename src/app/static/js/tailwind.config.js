/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/app/templates/**/*.html",
    "./src/app/static/js/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        sths: {
          navy: "#0b1f33",
          gold: "#f5b400",
          light: "#f5f7fb",
          dark: "#1f2933"
        }
      }
    }
  },
  plugins: []
};
