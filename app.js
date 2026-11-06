
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
  var su = document.getElementById('su');
  window.addEventListener('scroll', function () { if (su) su.hidden = window.scrollY < 600; }, { passive: true });
})();
