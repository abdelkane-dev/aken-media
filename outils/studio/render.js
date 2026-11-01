// node render.js page.html sortie.mp4|dossier fps durée [transparent]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
(async () => {
  const [page_, out, fpsS, durS, transp] = process.argv.slice(2);
  const fps = +fpsS, dur = +durS, N = Math.ceil(fps * dur), alpha = transp === 'alpha';
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + require('path').resolve(page_)); await p.evaluate(() => document.fonts.ready);
  const args = alpha
    ? ['-y', '-v', 'error', '-f', 'image2pipe', '-c:v', 'png', '-r', fpsS, '-i', '-', '-c:v', 'qtrle', out]
    : ['-y', '-v', 'error', '-f', 'image2pipe', '-c:v', 'mjpeg', '-r', fpsS, '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-pix_fmt', 'yuv420p', out];
  const ff = spawn('ffmpeg', args, { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let i = 0; i < N; i++) {
    await p.evaluate(t => render(t), i / fps);
    const buf = await p.screenshot(alpha ? { type: 'png', omitBackground: true } : { type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close();
})();
