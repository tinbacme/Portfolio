cd /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad
S="Use the blue colour of this reference (blue ballpoint / coloured pencil on white paper), but make it a QUICK, LOOSE sketchbook drawing, not a finished illustration: fast wobbly searching lines with double and triple strokes where the form was felt out, lines overshooting past corners, light construction lines (centre axis, perspective guides, ellipse guides) left visible, sparse uneven scribbly hatching only in the shadows with lots of untouched white paper, edges left unfinished and open in places, slightly off proportions, a loose scribbled ground shadow. Looks drawn in two minutes by a designer. Draw a NEW subject (not clouds):"
E="Single object, three-quarter view, centered with generous margin, transparent background, no paper texture, no text, no letters, no numbers, no signature, no circled callouts."
python3 tools/gen_edit.py pc2-plane parts/id_clouds.png "$S a small passenger airliner in flight. $E" 1536x1024 &
python3 tools/gen_edit.py pc2-matcha parts/id_clouds.png "$S a ceramic matcha bowl with tea and a bamboo whisk on a small stand. $E" 1536x1024 &
wait
python3 tools/gen_edit.py pc2-lamp parts/id_clouds.png "$S a modern LED desk lamp with an articulated two-segment arm and a round head. $E" 1536x1024 &
python3 tools/gen_edit.py pc2-laptop parts/id_clouds.png "$S an open laptop showing a simple rounded search bar and a few result cards. $E" 1536x1024 &
wait
python3 tools/gen_edit.py pc2-suitcase parts/id_clouds.png "$S a carry-on suitcase with its handle extended and a luggage tag. $E" 1536x1024
echo ALLDONE
