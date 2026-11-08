// Moteur d'animation déterministe : render(t) place chaque élément selon le temps t (s).
const E = {
  ease: x => x <= 0 ? 0 : x >= 1 ? 1 : 1 - Math.pow(1 - x, 3),
  back: x => { x = Math.min(Math.max(x, 0), 1); const c = 1.70158; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); },
};
function lin(a, b, p) { return a + (b - a) * p; }
function animEl(el, local) {
  const at = parseFloat(el.dataset.at || 0), dur = parseFloat(el.dataset.dur || 0.6);
  const p = (local - at) / dur, e = E.ease(p), b = E.back(p);
  const kind = el.dataset.anim;
  let o = 1, tr = '';
  switch (kind) {
    case 'fade': o = e; break;
    case 'up': o = e; tr = `translateY(${lin(80, 0, e)}px)`; break;
    case 'down': o = e; tr = `translateY(${lin(-80, 0, e)}px)`; break;
    case 'left': o = e; tr = `translateX(${lin(-140, 0, e)}px)`; break;
    case 'right': o = e; tr = `translateX(${lin(140, 0, e)}px)`; break;
    case 'pop': o = Math.min(1, p * 3); tr = `scale(${p <= 0 ? 0.4 : lin(0.4, 1, b)})`; break;
    case 'stamp': o = Math.min(1, Math.max(0, p * 4)); tr = `scale(${p <= 0 ? 2.4 : lin(2.4, 1, E.ease(p))}) rotate(-12deg)`; break;
    case 'grow': tr = `scaleY(${e})`; el.style.transformOrigin = 'bottom'; break;
    case 'growx': tr = `scaleX(${e})`; el.style.transformOrigin = 'left'; break;
    case 'type': { const full = el.dataset.full || (el.dataset.full = el.textContent); el.textContent = full.slice(0, Math.round(full.length * Math.min(Math.max(p, 0), 1))); break; }
    case 'count': { const to = parseFloat(el.dataset.to); const v = Math.round(to * e); el.textContent = v.toLocaleString('fr-FR').replace(/ | /g, ' ') + (el.dataset.suffix || ''); break; }
    case 'tap': { const q = local - at; const s = q > 0 && q < 0.35 ? 1 - 0.12 * Math.sin(q / 0.35 * Math.PI) : 1; tr = `scale(${s})`; if (q > 0.15) el.classList.add('tapped'); else el.classList.remove('tapped'); break; }
    case 'float': { tr = `translateY(${Math.sin((local + at) * 2) * 10}px)`; break; }
  }
  if (el.dataset.out) { const op = E.ease((local - parseFloat(el.dataset.out)) / 0.35); o *= 1 - op; }
  el.style.opacity = o; if (tr) el.style.transform = (el.dataset.base || '') + ' ' + tr;
}
function render(t) {
  const C = window.CONF;
  // fond animé
  document.querySelectorAll('.orb').forEach((o, i) => {
    const a = t * 0.25 + i * 2.1;
    o.style.transform = `translate(${Math.sin(a) * 160}px, ${Math.cos(a * 0.8) * 200}px)`;
  });
  const bar = document.getElementById('bar'); if (bar) bar.style.width = (t / C.duration * 100) + '%';
  document.querySelectorAll('.scene').forEach(sc => {
    const s = parseFloat(sc.dataset.start), e = parseFloat(sc.dataset.end);
    const fi = sc.dataset.nofade ? 1 : E.ease((t - s) / 0.3), fo = 1 - E.ease((t - e) / 0.3);
    const vis = t >= s - 0.01 && t <= e + 0.3;
    sc.style.opacity = vis ? Math.min(fi, fo) : 0;
    if (sc.classList.contains('photo')) sc.style.transform = vis ? `scale(${lin(1, 1.07, Math.min(1, (t - s) / Math.max(e - s, 1)))})` : '';
    else sc.style.transform = vis ? `scale(${lin(1.04, 1, fi) * lin(1, 0.97, 1 - fo)})` : '';
    if (vis) sc.querySelectorAll('[data-anim]').forEach(el => animEl(el, t - s));
  });
  // sous-titres karaoké
  const cap = document.getElementById('cap');
  if (cap && C.chunks && !C.nocap) {
    const c = C.chunks.find(c => t >= c.start - 0.05 && t < c.end + 0.12);
    if (!c) { cap.innerHTML = ''; return; }
    const words = c.text.split(' '); const pr = (t - c.start) / Math.max(c.end - c.start, 0.1);
    const pop = E.back((t - c.start + 0.05) / 0.18);
    cap.innerHTML = words.map((w, i) => `<span class="w ${i / words.length <= pr ? 'on' : ''}">${w}</span>`).join('');
    cap.style.transform = `scale(${lin(0.85, 1, pop)})`;
  }
}
