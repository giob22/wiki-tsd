
(function () {
  var root = document.documentElement;
  function lsGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  var size = parseFloat(lsGet('tsd-fs')) || 17;
  function applica() { document.body.style.fontSize = size + 'px'; }
  applica();
  var fm = document.getElementById('fm'), fp = document.getElementById('fp');
  if (fm) fm.onclick = function () { size = Math.max(13, size - 1); lsSet('tsd-fs', size); applica(); };
  if (fp) fp.onclick = function () { size = Math.min(26, size + 1); lsSet('tsd-fs', size); applica(); };

  function rendi(el) {
    if (el.dataset.ok || !window.katex) return;
    el.dataset.ok = '1';
    try { katex.render(el.textContent, el, { displayMode: el.classList.contains('block'), throwOnError: false, strict: false }); } catch (e) {}
    if (!el.classList.contains('block') && !el.closest('summary')) { var c = el.closest('p,li,td,th,blockquote,div'); if (c && el.getBoundingClientRect().width > c.clientWidth - 8) el.classList.add('wide'); }
  }
  function rendiIn(nodo) { nodo.querySelectorAll('.math').forEach(rendi); }
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
