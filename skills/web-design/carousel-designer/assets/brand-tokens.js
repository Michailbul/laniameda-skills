// Brand tokens — single source of truth
// Include this in every carousel via:
// <script>/* paste this file content */</script> after Tailwind CDN
tailwind.config = {
  theme: {
    extend: {
      colors: {
        primary:    '#8566AF',   // purple — badges, accents
        secondary:  '#BA943B',   // gold — kickers, highlights
        accent:     '#EA3F2C',   // red-orange — CTA, emphasis
        'accent-alt':'#FF552E',  // base hex — use sparingly
        brand:      '#09090B',   // near-black text
      },
      fontFamily: {
        display: ['"Arial Black"', '"Impact"', '"Segoe UI"', 'sans-serif'],
        body:    ['"Helvetica Neue"', '"Segoe UI"', 'Arial', 'sans-serif'],
        mono:    ['"SF Mono"', '"Menlo"', '"Consolas"', 'monospace'],
      },
      // LinkedIn slide canvas — do not change
      width:  { slide: '1080px' },
      height: { slide: '1350px' },
      // Grid overlay
      backgroundImage: {
        grid: 'linear-gradient(to right, rgba(9,9,11,.07) 1px, transparent 1px), linear-gradient(to bottom, rgba(9,9,11,.07) 1px, transparent 1px)',
      },
      backgroundSize: {
        grid: '54px 54px',
      },
    },
  },
}
