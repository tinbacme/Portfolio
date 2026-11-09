/* dc-lite: runs a Claude Design board (.dc.html) as a plain web page.
   Supports what the homepage board uses: {{holes}} in text and attributes,
   on* event attributes, ref, <sc-for list as>, <sc-if value>, and a
   React-style class (props, state, setState, lifecycle, renderVals). */
(function () {
  const HOLE = /\{\{\s*([^}]*?)\s*\}\}/g;
  const ONE = /^\{\{\s*([^}]*?)\s*\}\}$/;
  const EVT = { focus: 'focusin', blur: 'focusout' };

  class DCLogic {
    constructor(props) { this.props = props || {}; this.state = {}; }
    setState(u, cb) {
      const prev = this.state;
      const v = typeof u === 'function' ? u(this.state, this.props) : u;
      this.state = Object.assign({}, this.state, v);
      this.__dc && this.__dc.schedule(prev, cb);
    }
    forceUpdate(cb) { this.__dc && this.__dc.schedule(this.state, cb); }
  }
  window.DCLogic = DCLogic;

  function lookup(scope, expr) {
    if (expr === 'true') return true;
    if (expr === 'false') return false;
    if (expr === 'null') return null;
    if (/^-?\d+(\.\d+)?$/.test(expr)) return Number(expr);
    if (/^(['"]).*\1$/.test(expr)) return expr.slice(1, -1);
    const parts = expr.split('.');
    let v = scope(parts[0]);
    for (let i = 1; i < parts.length && v != null; i++) v = v[parts[i]];
    return v;
  }
  const interp = (str, scope) => {
    const m = str.match(ONE);
    if (m) { const v = lookup(scope, m[1]); return v == null ? '' : String(v); }
    return str.replace(HOLE, (_, e) => { const v = lookup(scope, e); return v == null ? '' : String(v); });
  };

  function mount(tplRoot, host, comp) {
    let vals = {};
    const top = (k) => vals[k];
    const refs = [];

    // Build real DOM from a template node; returns { node, binds[] }
    function build(t, scope, binds) {
      if (t.nodeType === 3) {
        const n = document.createTextNode(t.data);
        if (t.data.includes('{{')) { const src = t.data; binds.push(() => { const v = interp(src, scope); if (n.data !== v) n.data = v; }); }
        return n;
      }
      if (t.nodeType !== 1) return document.createComment('');
      const tag = t.localName;
      if (tag === 'helmet') return document.createComment('helmet');
      if (tag === 'sc-for') return buildFor(t, scope, binds);
      if (tag === 'sc-if') return buildIf(t, scope, binds);
      const el = t.namespaceURI && t.namespaceURI !== 'http://www.w3.org/1999/xhtml'
        ? document.createElementNS(t.namespaceURI, t.localName) : document.createElement(tag);
      for (const a of Array.from(t.attributes)) {
        const name = a.name, val = a.value;
        if (name.startsWith('hint-')) continue;
        if (name.length > 2 && name.startsWith('on') && val.includes('{{')) {
          const key = (val.match(ONE) || [])[1];
          const ev = name.slice(2).toLowerCase();
          el.addEventListener(EVT[ev] || ev, (e) => { const fn = lookup(scope, key); if (typeof fn === 'function') fn(e); });
          continue;
        }
        if (name === 'ref') { const key = (val.match(ONE) || [])[1]; refs.push(() => { const fn = lookup(scope, key); if (typeof fn === 'function') fn(el); }); continue; }
        if (val.includes('{{')) {
          binds.push(() => { const v = interp(val, scope); if (el.getAttribute(name) !== v) a.namespaceURI ? el.setAttributeNS(a.namespaceURI, name, v) : el.setAttribute(name, v); });
          continue;
        }
        a.namespaceURI ? el.setAttributeNS(a.namespaceURI, name, val) : el.setAttribute(name, val);
      }
      const kids = tag === 'template' ? t.content.childNodes : t.childNodes;
      for (const c of Array.from(kids)) el.appendChild(build(c, scope, binds));
      return el;
    }

    function buildIf(t, scope, binds) {
      const el = document.createElement('sc-if');
      const key = (t.getAttribute('value') || '').match(ONE);
      let built = false;
      binds.push(() => {
        const on = !!(key ? lookup(scope, key[1]) : false);
        if (on && !built) { built = true; const inner = []; for (const c of Array.from(t.childNodes)) el.appendChild(build(c, scope, inner)); binds.push(...inner); inner.forEach((f) => f()); }
        el.style.display = on ? 'contents' : 'none';
      });
      return el;
    }

    function buildFor(t, scope, binds) {
      const el = document.createElement('sc-for');
      const key = (t.getAttribute('list') || '').match(ONE), as = t.getAttribute('as') || 'item';
      const items = [];
      binds.push(() => {
        const list = (key && lookup(scope, key[1])) || [];
        for (let i = 0; i < list.length; i++) {
          if (!items[i]) {
            const it = { value: list[i], binds: [], nodes: [] };
            const s = (k) => (k === as ? it.value : k === as + 'Index' ? i : scope(k));
            for (const c of Array.from(t.childNodes)) { const n = build(c, s, it.binds); it.nodes.push(n); el.appendChild(n); }
            items[i] = it;
          }
          items[i].value = list[i];
          items[i].binds.forEach((f) => f());
        }
        while (items.length > list.length) items.pop().nodes.forEach((n) => n.remove());
      });
      return el;
    }

    const binds = [];
    const frag = document.createDocumentFragment();
    for (const c of Array.from(tplRoot.childNodes)) frag.appendChild(build(c, top, binds));
    const update = () => { vals = comp.renderVals() || {}; binds.forEach((f) => f()); };
    update();
    host.appendChild(frag);
    refs.forEach((f) => f());

    let queued = false, prevState = null, cbs = [];
    comp.__dc = {
      schedule(prev, cb) {
        if (!queued) { prevState = prev; queued = true; Promise.resolve().then(() => {
          queued = false; update();
          if (comp.componentDidUpdate) try { comp.componentDidUpdate(comp.props, prevState); } catch (e) { console.error(e); }
          const c = cbs; cbs = []; c.forEach((f) => f());
        }); }
        if (cb) cbs.push(cb);
      },
    };
    if (comp.componentDidMount) comp.componentDidMount();
  }

  window.dcLite = {
    run({ template, host, Component, props }) {
      const comp = new Component(props);
      mount(template.content, host, comp);
      window.addEventListener('pagehide', () => comp.componentWillUnmount && comp.componentWillUnmount());
      return comp;
    },
  };
})();
