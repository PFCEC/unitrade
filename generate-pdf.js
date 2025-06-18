const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new', // 或 'true' 視 Node 版本而定
  });
  const page = await browser.newPage();

  // 要產出 PDF 的網址（可多頁迴圈）
  const urls = [
    'http://127.0.0.1:4000/unitrade/' 
  ];

  for (const url of urls) {
    await page.goto(url, { waitUntil: 'networkidle0' });

    const fileName = url.split('/').filter(s => s).pop() || 'index';

    await page.pdf({
      path: `${fileName}.pdf`,
      format: 'A4',
      printBackground: true,
      margin: { top: '20mm', bottom: '20mm', left: '15mm', right: '15mm' }
    });

    console.log(`📄 Saved PDF for ${url}`);
  }

  await browser.close();
})();
