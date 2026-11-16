"""Stuart page: calm nav while scrolling. Scroll-position spy (one reading line, rAF-throttled) instead of the IO band,
spy paused while a click-scroll is running, and no-overshoot easing on the lens. usage: stuartspy.py <TinHome-Stuart.dc.html>"""
import sys
p = sys.argv[1]; s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (old[:90], s.count(old)); s = s.replace(old, new)
rep("transition:transform .55s cubic-bezier(.34,1.45,.5,1),width .45s cubic-bezier(.3,1.3,.5,1);",
    "transition:transform .5s cubic-bezier(.22,1,.36,1),width .45s cubic-bezier(.22,1,.36,1);will-change:transform,width;")
a = s.index("  svSpy() {"); b = s.index("  rvStart() {")
SPY = """  svSpy() { // the nav follows the page: the current role is the last one whose top has passed a line 35% down the screen
    if (this.svOn || !this.rootEl) return;
    if (window.innerHeight > 1600) return; // whole board shown at once (design canvas): no real scrolling, so keep Hi selected
    const ids = ["microsoft", "salesforce", "uo-teach", "2u", "uo-bs"];
    const read = () => {
      this.svRaf = 0; if (!this.rootEl) return;
      if (this.svLock != null) return; // a click is scrolling us to a role: hold the pill on it until the scroll settles
      const line = window.innerHeight * 0.35; let k = 5;
      ids.forEach((id, i) => { const el = this.rootEl.querySelector('#' + CSS.escape(id)); if (el && el.getBoundingClientRect().top <= line) k = i; });
      if (this.state.nav !== k) this.setState({ nav: k });
    };
    this.svScroll = () => {
      if (this.svLock != null) { clearTimeout(this.svLockT); this.svLockT = setTimeout(() => { this.svLock = null; read(); }, 160); return; }
      if (!this.svRaf) this.svRaf = requestAnimationFrame(read);
    };
    document.addEventListener('scroll', this.svScroll, { capture: true, passive: true }); window.addEventListener('resize', this.svScroll);
    this.svOn = true; read();
  }
  svHold(k) { // pin the pill on k while the page smooth-scrolls there, so it doesn't flick through every role on the way
    this.svLock = k; clearTimeout(this.svLockT); this.svLockT = setTimeout(() => { this.svLock = null; }, 1400);
  }
"""
s = s[:a] + SPY + s[b:]
rep("this.setState({ nav: k }); if (!el) return;", "this.setState({ nav: k }); this.svHold(k); if (!el) return;")
rep("try { window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); } catch (x) { window.scrollTo(0, 0); } this.setState({ nav: 5 }); }",
    "this.svHold(5); try { window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); } catch (x) { window.scrollTo(0, 0); } let box = this.rootEl && this.rootEl.parentElement; while (box && box !== document.body && box !== document.documentElement) { if (box.scrollTop > 0) { box.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); break; } box = box.parentElement; } this.setState({ nav: 5 }); }")
rep("if (this.svIO) this.svIO.disconnect();", "if (this.svScroll) { document.removeEventListener('scroll', this.svScroll, true); window.removeEventListener('resize', this.svScroll); } cancelAnimationFrame(this.svRaf); clearTimeout(this.svLockT);")
open(p, 'w').write(s); print('ok')
