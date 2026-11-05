cd /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad
L="A fast, imperfect industrial design ideation sketch, the kind a designer dashes off in 3-5 minutes in a sketchbook, definitely NOT clean or polished: wobbly hand-drawn ballpoint and fineliner lines with searching double and triple strokes where the designer felt for the form, lines overshooting past corners, ghosted light construction lines and ellipses left everywhere, slightly off proportions and imperfect ellipses, some contours redrawn heavier over lighter attempts; a quick loose callout arrow to a scribbled circled detail; then a hasty marker wash in one main colour plus one small accent that misses the edges, leaves white gaps, streaks and overlaps, bleeds slightly past the lines, with a scrappy grey marker shadow underneath and a couple of white-pen highlight flicks. Raw, human, energetic. Transparent background, no paper texture, no text, no letters, no numbers, no logos, no signature."
O="Single object, three-quarter view, centered with generous margin."
python3 tools/gen_new.py lo-plane "$L Subject: a small passenger airliner in flight; main colour teal, accent coral on the tail. $O" 1536x1024 transparent &
python3 tools/gen_new.py lo-matcha "$L Subject: a ceramic matcha bowl with frothy tea and a bamboo whisk on a stand; main colour matcha green, accent rust-terracotta glaze. $O" 1536x1024 transparent &
wait
python3 tools/gen_new.py lo-lamp "$L Subject: a modern LED desk lamp with an articulated two-segment arm and a round head; main colour safety orange, accent warm yellow light. $O" 1536x1024 transparent &
python3 tools/gen_new.py lo-laptop "$L Subject: an open laptop showing a rounded search bar and result cards; main colour screen blue, accent yellow on one result. $O" 1536x1024 transparent &
wait
python3 tools/gen_new.py lo-suitcase "$L Subject: a carry-on suitcase with its handle extended, a luggage tag and stickers; main colour mustard yellow, accent coral sticker. $O" 1536x1024 transparent
echo ALLDONE
