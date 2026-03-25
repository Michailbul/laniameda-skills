/**
 * render.mjs — Playwright carousel renderer
 * Usage: node render.mjs [--html src/slides.html] [--out dist]
 *
 * Outputs:
 *   dist/carousel.pdf        — LinkedIn-ready PDF (7 pages, 1080x1350)
 *   dist/slides/01.png ...   — PNG per slide (2x retina)
 */
import fs   from 'node:fs/promises'
import path from 'node:path'
import os   from 'node:os'
import { fileURLToPath } from 'node:url'
import { chromium } from 'playwright'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const args      = process.argv.slice(2)
const htmlArg   = args[args.indexOf('--html') + 1]
const outArg    = args[args.indexOf('--out')  + 1]

const htmlPath  = path.resolve(htmlArg  || path.join(__dirname, '..', 'src', 'slides.html'))
const distDir   = path.resolve(outArg   || path.join(__dirname, '..', 'dist'))
const slidesDir = path.join(distDir, 'slides')
const pdfPath   = path.join(distDir, 'carousel.pdf')

const W = 1080, H = 1350

// ── arm64 fallback browser paths (macOS) ──────────────────────────────────
const FALLBACK_EXECUTABLES = [
  process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH,
  path.join(os.homedir(), 'Library', 'Caches', 'ms-playwright',
    'chromium_headless_shell-1208', 'chrome-headless-shell-mac-arm64', 'chrome-headless-shell'),
  path.join(os.homedir(), 'Library', 'Caches', 'ms-playwright',
    'chromium-1208', 'chrome-mac-arm64',
    'Google Chrome for Testing.app', 'Contents', 'MacOS', 'Google Chrome for Testing'),
].filter(Boolean)

async function launch () {
  try { return await chromium.launch({ headless: true }) } catch {}
  for (const exe of FALLBACK_EXECUTABLES) {
    try { await fs.access(exe); return await chromium.launch({ headless: true, executablePath: exe }) } catch {}
  }
  throw new Error('No usable Chromium found. Run: npx playwright install chromium-headless-shell')
}

// ── main ──────────────────────────────────────────────────────────────────
await fs.mkdir(slidesDir, { recursive: true })

const browser = await launch()
const page    = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 })

await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' })
await page.emulateMedia({ media: 'screen' })
if (document?.fonts) await page.evaluate(() => document.fonts.ready)
await page.waitForTimeout(300)

const slides = await page.locator('.slide').all()
console.log(`Found ${slides.length} slides`)

for (let i = 0; i < slides.length; i++) {
  const file = path.join(slidesDir, `${String(i + 1).padStart(2, '0')}.png`)
  await slides[i].screenshot({ path: file, type: 'png' })
  console.log(`  ✓ ${path.basename(file)}`)
}

await page.pdf({
  path: pdfPath,
  width: `${W}px`, height: `${H}px`,
  printBackground: true,
  margin: { top: '0px', right: '0px', bottom: '0px', left: '0px' },
  preferCSSPageSize: true,
})
console.log(`  ✓ carousel.pdf`)

await browser.close()
console.log(`\nDone → ${distDir}`)
