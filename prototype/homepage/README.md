# Homepage prototype

A working web page built from the **TinHome copy** board (`canvas/project/TinHome-2goy.dc.html`) on the design canvas.

- `index.html`: the generated page. Open it directly in a browser.
- `assets/`: the board's images.
- `dc-lite.js`: a small runtime that runs the board's own code (template holes, loops, events, Tweak values) outside the canvas.
- `build.py`: regenerates `index.html` from the board.

## Workflow

1. Design on the canvas board, including its Tweaks.
2. Pull the latest board and any new images, then rebuild:

   ```
   python3 build.py <board.dc.html> <assets dir> .
   ```

3. Republish the prototype page.

Each Tweak's current value on the canvas is baked into the prototype. The only prototype-specific additions are phone-width rules in `build.py`: smaller side padding, fluid work images and a scaled About board. They keep the page from scrolling sideways on phones.
