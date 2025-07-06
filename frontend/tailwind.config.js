/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class', // Enable dark mode via .dark class
  content: [
    './src/**/*.{js,jsx,ts,tsx}',
    './public/index.html',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#1e293b', // slate-800
        secondary: '#334155', // slate-700
        accent: '#38bdf8', // sky-400
        background: '#0f172a', // slate-900
        surface: '#1e293b',
        'on-primary': '#f1f5f9', // slate-100
      },
    },
  },
  plugins: [],
};
