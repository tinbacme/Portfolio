cd /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad
P="Redraw this same industrial design marker sketch — same object, same pose, same colours, same composition — but: make the black outlines noticeably THICKER and bolder (thick confident brush-pen contours, heavier on the shadow side), and leave MUCH MORE WHITE PAPER: the marker colour is lighter and less dense, laid in only a few quick streaky strokes mostly on the shadow side and along the edges, with wide white reflection bands and large untouched white areas on the lit side, so the drawing feels airy and sketchy rather than fully saturated. Keep the construction lines and the hatched ground shadow. Transparent background, no text, no letters, no circled callouts."
for k in plane matcha; do python3 tools/gen_edit.py pl-$k parts/pr-$k.png "$P" 1536x1024 & done; wait
for k in lamp laptop; do python3 tools/gen_edit.py pl-$k parts/pr-$k.png "$P" 1536x1024 & done; wait
python3 tools/gen_edit.py pl-suitcase parts/pr-suitcase.png "$P" 1536x1024
echo ALLDONE
