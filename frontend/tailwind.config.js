/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',
    '../blueprints/**/*.py',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#141414', // Nero scuro
        black: '#000000',
        yellow: '#fcc630',   // Giallo del brand
      },
    },
  },
  plugins: [],
}