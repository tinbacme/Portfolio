cd /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad
BASE="Wide hero illustration for a designer portfolio: a soft bank of cumulus clouds drifting across, with a small flock of four simple birds, lots of open empty space in the middle for a headline. Transparent background, no paper, no text, no letters, no signature, no frame."
python3 tools/gen_new.py sk-pencil "$BASE Style: graphite pencil sketch from an industrial designer's sketchbook, light construction lines, perspective guide lines, smudged soft shading, varied line weight, a few loose hatching strokes. Grey graphite only." 1536x1024 transparent &
python3 tools/gen_new.py sk-marker "$BASE Style: industrial-design marker rendering, cool grey alcohol markers (Copic) with crisp black fineliner outlines and white gel-pen highlights, bold confident strokes, a single accent of sky blue marker." 1536x1024 transparent &
wait
python3 tools/gen_new.py sk-ink "$BASE Style: loose sumi ink and watercolour wash, wet-on-wet indigo and soft blue, bleeding edges, a few dry-brush strokes, birds as quick single brush marks, airy and calm." 1536x1024 transparent &
python3 tools/gen_new.py sk-riso "$BASE Style: two-colour risograph print, cobalt blue and warm coral, visible grain and halftone texture, slight misregistration between the two colours, flat graphic cloud shapes." 1536x1024 transparent &
wait
python3 tools/gen_new.py sk-tech "$BASE Style: technical orthographic line drawing like a product design spec sheet, thin precise cyan-blue lines, clouds drawn as clean geometric arcs with centre marks, dashed construction circles and dimension lines with arrowheads but no numbers, birds as tiny precise chevrons." 1536x1024 transparent &
wait
echo ALLDONE
