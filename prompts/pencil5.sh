cd /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad
while ! grep -q ALLDONE /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/tasks/b6h6p1q85.output 2>/dev/null; do sleep 5; done
S="Match the exact drawing style of this reference image: blue coloured-pencil / ballpoint hatching on white paper, dense directional hatch strokes building up the form, soft unshaded paper highlights, loose and hand-made, slightly imperfect. Draw a NEW subject (not clouds):"
E="Single object, three-quarter view, centered with generous margin, transparent background, no paper texture, no text, no letters, no numbers, no signature, no circled callouts."
python3 tools/gen_edit.py pc-plane parts/id_clouds.png "$S a small passenger airliner in flight. $E" 1536x1024 &
python3 tools/gen_edit.py pc-matcha parts/id_clouds.png "$S a ceramic matcha bowl with frothy tea and a bamboo whisk on a small stand. $E" 1536x1024 &
wait
python3 tools/gen_edit.py pc-lamp parts/id_clouds.png "$S a modern LED desk lamp with an articulated two-segment arm and a round head. $E" 1536x1024 &
python3 tools/gen_edit.py pc-laptop parts/id_clouds.png "$S an open laptop showing a simple rounded search bar and a few result cards. $E" 1536x1024 &
wait
python3 tools/gen_edit.py pc-suitcase parts/id_clouds.png "$S a carry-on suitcase with its handle extended and a luggage tag. $E" 1536x1024
echo ALLDONE
