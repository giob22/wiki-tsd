
(function () {
  var root = document.documentElement;
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  var size = parseFloat(lsGet('tsd-fs')) || 17;
  function applica() { document.body.style.fontSize = size + 'px'; }
  applica();
  var fm = document.getElementById('fm'), fp = document.getElementById('fp');
  if (fm) fm.onclick = function () { size = Math.max(13, size - 1); lsSet('tsd-fs', size); applica(); fitAll(); };
  if (fp) fp.onclick = function () { size = Math.min(26, size + 1); lsSet('tsd-fs', size); applica(); fitAll(); };

  // tema: sistema (segue il dispositivo), chiaro, scuro
  var temi = { sistema: null, chiaro: 'light', scuro: 'dark' };
  var tema = lsGet('tsd-tema'); if (!(tema in temi)) tema = 'sistema';
  function temaApplica() {
    if (temi[tema]) root.setAttribute('data-theme', temi[tema]); else root.removeAttribute('data-theme');
    document.querySelectorAll('.tm button').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.t === tema ? 'true' : 'false'); });
  }
  temaApplica();
  document.querySelectorAll('.tm button').forEach(function (b) { b.onclick = function () { tema = b.dataset.t; lsSet('tsd-tema', tema); temaApplica(); }; });

  // una formula troppo larga viene rimpicciolita finché sta in una riga (sotto la soglia resta lo scorrimento)
  var MIN = 0.3;
  function fit(el) {
    if (!el.dataset.ok) return;
    var blocco = el.classList.contains('block');
    el.style.fontSize = '';
    if (!blocco && !el.closest('summary')) {
      var c = el.closest('p,li,td,th,blockquote,div');
      el.classList.remove('wide');
      if (c && c.clientWidth && el.getBoundingClientRect().width > c.clientWidth - 8) el.classList.add('wide');
    }
    if (!blocco && !el.classList.contains('wide')) return;
    if (!el.clientWidth) return;
    var k = 1;
    for (var i = 0; i < 4 && k > MIN; i++) {
      var w = larghezza(el);
      if (w <= el.clientWidth - 1) break;
      k = Math.max(MIN, k * (el.clientWidth - 1) / w * 0.985);
      el.style.fontSize = k + 'em';
    }
  }
  // larghezza occupata dalla formula (più il numero d'equazione, che sta a destra)
  function larghezza(el) {
    var basi = el.querySelectorAll('.katex-html > .base');
    if (!basi.length) return el.scrollWidth;
    var l = 1e9, r = -1e9;
    basi.forEach(function (b) { var q = b.getBoundingClientRect(); l = Math.min(l, q.left); r = Math.max(r, q.right); });
    var tag = el.querySelector('.tag');
    return (r - l) + (tag ? tag.getBoundingClientRect().width + 12 : 0);
  }
  function fitAll() { document.querySelectorAll('.math[data-ok]').forEach(fit); }
  var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(fitAll, 150); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitAll);

  function rendi(el) {
    if (el.dataset.ok || !window.katex) return;
    el.dataset.ok = '1';
    try { katex.render(el.textContent, el, { displayMode: el.classList.contains('block'), throwOnError: false, strict: false }); } catch (e) {}
    fit(el);
  }
  function rendiIn(nodo) { nodo.querySelectorAll('.math').forEach(function (e) { rendi(e); fit(e); }); }
  function chiuso(el) { if (el.closest('summary')) return false; var d = el.closest('details'); while (d) { if (!d.open) return true; d = d.parentElement && d.parentElement.closest('details'); } return false; }
  function avvia() {
    document.querySelectorAll('.math').forEach(function (el) { if (!chiuso(el)) rendi(el); });
    document.querySelectorAll('details').forEach(function (d) { d.addEventListener('toggle', function () { if (d.open) rendiIn(d); }); });
    // apre i dettagli che contengono l'ancora richiesta
    function apriAncora() {
      var id = decodeURIComponent(location.hash.slice(1)); if (!id) return;
      var el = document.getElementById(id); if (!el) return;
      var d = el.closest('details');
      while (d) { d.open = true; d = d.parentElement && d.parentElement.closest('details'); }
      rendiIn(document.body); el.scrollIntoView();
    }
    window.addEventListener('hashchange', apriAncora); apriAncora();
    setTimeout(fitAll, 500);
    document.body.setAttribute('data-pronto', '1');
  }
  window.addEventListener('load', avvia);
  // lightbox
  var lb = document.getElementById('lb');
  document.addEventListener('click', function (e) {
    var t = e.target;
    if (t.tagName === 'IMG' && t.classList.contains('zoom')) { lb.innerHTML = '<img src="' + t.src + '" alt="">'; lb.hidden = false; }
    else if (lb && !lb.hidden) { lb.hidden = true; lb.innerHTML = ''; }
  });
  // anteprima delle equazioni richiamate nel testo, ad esempio «(10)»
  var eqTex = {}, eqEl = {};
  document.querySelectorAll('.math[data-eq]').forEach(function (b) {
    var tex = b.textContent;
    b.dataset.eq.split(' ').forEach(function (n) { eqTex[n] = tex; eqEl[n] = b; });
  });
  var pop = document.createElement('div'); pop.id = 'eqpop'; pop.hidden = true; document.body.appendChild(pop);
  var popT = null, popA = null;
  var tocco = !(window.matchMedia && matchMedia('(hover: hover)').matches);
  function popNascondi() { clearTimeout(popT); pop.hidden = true; popA = null; }
  function popMostra(a) {
    var n = a.dataset.eq;
    if (!eqTex[n] || !window.katex) return;
    clearTimeout(popT); popA = a;
    pop.innerHTML = '<div class="ph"><span>Equazione (' + n + ')</span><a href="#eq-' + n + '">vai all’equazione ↓</a></div><div class="math block"></div>';
    var m = pop.lastChild; m.dataset.ok = '1';
    pop.hidden = false;
    var tex = eqTex[n].replace(/\\tag\{\d+\}/g, '');
    try { katex.render(tex, m, { displayMode: true, throwOnError: false, strict: false }); } catch (e) {}
    fit(m);
    var r = a.getBoundingClientRect(), w = pop.offsetWidth, h = pop.offsetHeight;
    var x = Math.min(Math.max(8, r.left - 16), Math.max(8, window.innerWidth - w - 8));
    var y = r.bottom + 6;
    if (y + h > window.innerHeight - 8 && r.top - h - 6 > 8) y = r.top - h - 6;
    pop.style.left = x + 'px'; pop.style.top = Math.max(8, y) + 'px';
  }
  function flash(n) {
    var b = eqEl[n]; if (!b) return;
    b.classList.add('flash'); setTimeout(function () { b.classList.remove('flash'); }, 1800);
  }
  function flashHash() { var m = /^#eq-(\d+)$/.exec(location.hash); if (m) flash(m[1]); }
  window.addEventListener('hashchange', flashHash); window.addEventListener('load', flashHash);
  function eqLink(t) { return t.closest ? t.closest('a.eqref') : null; }
  document.addEventListener('mouseover', function (e) {
    if (tocco) return;
    var a = eqLink(e.target);
    if (a) { if (a === popA && !pop.hidden) { clearTimeout(popT); return; } clearTimeout(popT); popT = setTimeout(function () { popMostra(a); }, 120); }
    else if (e.target.closest && e.target.closest('#eqpop')) clearTimeout(popT);
  });
  document.addEventListener('mouseout', function (e) {
    if (tocco) return;
    if (eqLink(e.target) || (e.target.closest && e.target.closest('#eqpop'))) { clearTimeout(popT); popT = setTimeout(popNascondi, 260); }
  });
  document.addEventListener('focusin', function (e) { var a = eqLink(e.target); if (a) popMostra(a); });
  document.addEventListener('focusout', function (e) { if (eqLink(e.target)) popT = setTimeout(popNascondi, 200); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') popNascondi(); });
  document.addEventListener('click', function (e) {
    var a = eqLink(e.target);
    if (a && tocco) { e.preventDefault(); if (popA === a && !pop.hidden) popNascondi(); else popMostra(a); return; }
    if (!(e.target.closest && e.target.closest('#eqpop a'))) { if (!(e.target.closest && e.target.closest('#eqpop'))) popNascondi(); return; }
    popNascondi();
  });
  window.addEventListener('scroll', function () { if (!pop.hidden) popNascondi(); }, { passive: true });

  var su = document.getElementById('su');
  window.addEventListener('scroll', function () { if (su) su.hidden = window.scrollY < 600; }, { passive: true });
})();
