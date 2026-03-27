// Playwright link checker for Docusaurus site
const { chromium } = require('playwright');

const BASE_URL = 'http://localhost:3001/expertflow-cx-documentation';
const MAX_PAGES = 2000;

async function main() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();

  const visited = new Set();
  const queue = [BASE_URL + '/'];
  const broken = []; // { url, foundOn, status }

  async function checkPage(url, foundOn) {
    const page = await context.newPage();
    let status;
    try {
      const response = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 15000 });
      status = response ? response.status() : 0;

      if (status >= 400) {
        broken.push({ url, foundOn, status });
        await page.close();
        return [];
      }

      // Collect internal links from this page
      const links = await page.$$eval('a[href]', (anchors, base) => {
        return anchors
          .map(a => {
            try { return new URL(a.href, base).href; } catch { return null; }
          })
          .filter(Boolean);
      }, url);

      await page.close();

      return links.filter(link =>
        link.startsWith(BASE_URL) &&
        !link.includes('#') &&
        !link.endsWith('.png') &&
        !link.endsWith('.jpg') &&
        !link.endsWith('.svg') &&
        !link.endsWith('.ico') &&
        !link.endsWith('.pdf')
      );
    } catch (err) {
      broken.push({ url, foundOn, status: `ERROR: ${err.message.split('\n')[0]}` });
      try { await page.close(); } catch {}
      return [];
    }
  }

  let processed = 0;
  while (queue.length > 0 && processed < MAX_PAGES) {
    const url = queue.shift();
    const normalized = url.replace(/\/$/, '');
    if (visited.has(normalized)) continue;
    visited.add(normalized);
    processed++;

    process.stdout.write(`\r[${processed}] Checking: ${url.replace(BASE_URL, '').slice(0, 80).padEnd(80)}`);

    const links = await checkPage(url, url);
    for (const link of links) {
      const norm = link.replace(/\/$/, '');
      if (!visited.has(norm)) queue.push(link);
    }
  }

  console.log(`\n\nScanned ${processed} pages.\n`);

  if (broken.length === 0) {
    console.log('✅ No broken links found!');
  } else {
    console.log(`❌ Found ${broken.length} broken links:\n`);
    for (const { url, foundOn, status } of broken) {
      const path = url.replace(BASE_URL, '') || '/';
      const from = foundOn.replace(BASE_URL, '') || '/';
      console.log(`  [${status}] ${path}`);
      console.log(`        found on: ${from}`);
    }
  }

  await browser.close();
}

main().catch(err => { console.error(err); process.exit(1); });
