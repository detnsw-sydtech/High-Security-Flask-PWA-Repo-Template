/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/app/templates/**/*.html",
    "./src/app/static/js/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui"]
      }
    }
  },
  plugins: []
};
