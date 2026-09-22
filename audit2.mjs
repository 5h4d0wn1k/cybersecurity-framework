import puppeteer from 'puppeteer-core';
const browser = await puppeteer.launch({ executablePath: '/usr/bin/google-chrome-stable', args: ['--no-sandbox','--headless=new'] });
const page = await browser.newPage();
const logs=[]; page.on('pageerror',e=>logs.push('ERR: '+e.message));
page.on('requestfailed',r=>logs.push('REQFAIL: '+r.url()));
await page.setViewport({ width:1440, height:900 });
await page.goto('http://localhost:8899/page.html', { waitUntil:'networkidle2', timeout:30000 });
await new Promise(r=>setTimeout(r,800));
const out = await page.evaluate(() => {
  const nodes=[...document.querySelectorAll('svg g.node')];
  const rects=nodes.map(n=>{const el=n.querySelector('.bg')||n;const r=el.getBoundingClientRect();return {l:n.querySelector('text')?.textContent?.slice(0,24),cls:n.getAttribute('class'),x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width),h:Math.round(r.height)}});
  const visible=rects.filter(r=>r.w>0);
  return { count: nodes.length, visible: visible.length,
    minX: Math.min(...visible.map(r=>r.x)), maxX: Math.max(...visible.map(r=>r.x+r.w)),
    minY: Math.min(...visible.map(r=>r.y)), maxY: Math.max(...visible.map(r=>r.y+r.bottom)),
    viewportW: innerWidth, viewportH: innerHeight,
    focusedRow: visible.slice(0,6),
    pillarCls: visible.find(r=>/tpillar/.test(r.cls))?.cls,
    groupCls: visible.find(r=>/tgroup/.test(r.cls))?.cls };
});
console.log(JSON.stringify(out,null,1));
console.log('LOGS:', logs.length?logs:'none');
await browser.close();
