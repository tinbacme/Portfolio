# Reference teardown: what the 9 example sites actually do

Captured Nov 8, 2026 in a headless browser, so this reflects the live pages: the intro frame, the hero, then four scroll positions, plus the fonts and libraries each page loaded. labs.griflan.com needs WebGPU and crashed the browser. michelangelus.studiogusto.com refused this browser. daddyyankee.com sits behind an ENTER gate the script couldn't pass.

| Site | Big idea | Type | Color | Motion / tech |
|---|---|---|---|---|
| sadok.mx | A 3D Game Boy is the navigation. Power it on, D-pad through projects, calm case-study pages | Handjet + Press Start 2P (pixel) | Near-black, rainbow road | Astro, Three.js, Rive, sound, plain-list fallback |
| thewhoopsies.co.uk | One continuous camera move through a drawing: scroll goes into the character's eye, into a bed, out to the book floating in space | Custom handwriting font made for the brand + Cormorant | Yellow, hot pink, cream, black | GSAP ScrollTrigger + SplitText |
| nexplayground.com | Scale play: a product cube shrinks while giant type builds "ONE LITTLE CUBE. A GIANT…" | BD Karlo at 150 px + **Be Vietnam Pro** body | Teal, green, warm gray | Lenis smooth scroll, 2 canvases |
| madebyigor.com | Extreme scale contrast: full-width "CREATIVE DEVELOPER" in a condensed serif against 10 px text | PP Editorial Old + OT Jubilee | One saturated teal, full bleed, with a coral swirl | Next.js, WebGL shader background |
| auge-xp.com | The work is the hero: a sliding wall of project images over a giant wordmark | PP Neue Montreal, Greed Bold, Farnham Display | Warm gray + black + one yellow tag | Next.js, canvas |
| daddyyankee.com | An ENTER gate, then a 40,000 px scroll story | ABC Diatype Compressed at **420 px** | Royal blue, cream, acid yellow | Webflow, Lenis, a custom worker |
| mikes.cv | Airplane window + "flight plan" career timeline | MB Sans + MB Mono (custom) | Off-white | Vite, no canvas |
| michelangelus | A typeface launch: the font is the experience | Michelangelus (their own) | Blue + pink | Next.js, Lenis |

## Principles (what my generated images were missing)

1. **One idea, and it does the navigating.** The Game Boy, the camera dive, the shrinking cube. None of them is a hero picture with a nav bar on top.
2. **Type is the main visual and it is characterful.** Every site uses a custom or licensed display face at extreme size (150–420 px) next to very small text. None uses a default sans at a polite size.
3. **Commit to a color.** Saturated, full-bleed, usually one or two colors. Off-white minimalism shows up only where the work itself carries the page (mikes.cv, auge).
4. **Scroll is choreography.** Four of the eight use Lenis and one uses GSAP ScrollTrigger. Things transform as you scroll, not section after section.
5. **Wit in the small copy.** "We wanted Hobnobs, they gave us website cookies instead." "A rhyming story about witches. How original." "You are player/visitor #43,525." "Thank you for flying."
6. **Calm where reading happens.** Case-study pages go quiet (sadok, mikes) and always offer a plain path to the work.

## For Tin

- **Be Vietnam Pro**, Nex's body face, was designed by Vietnamese type designers, and it is free on Google Fonts. It makes a fitting body face, with Vietnamese diacritics as a feature.
- Keep the minimalism, but make it tense: giant type, one committed color, extreme scale contrast. Not beige and calm.
- The "tiny thing I built" Easter egg plus wit in the plain-warm voice covers principle 5.
- The idea must survive as motion. Judge it as a short motion study, not a still image.
- Use image generation only for art (illustration, texture, objects) made from chosen references. Set the type and layout by hand.
