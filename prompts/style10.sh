cd /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad
E="Single object, centered, three-quarter view, generous empty margin, transparent background, no paper texture, no text, no letters, no numbers, no logos, no signature, no frame."
declare -A SUB
SUB[plane]="a small passenger airliner in flight"
SUB[matcha]="a ceramic matcha bowl with frothy tea and a bamboo whisk (chasen) on a small stand beside it"
SUB[lamp]="a modern LED desk lamp with an articulated two-segment arm and a slim round head"
SUB[laptop]="an open laptop whose screen shows a simple rounded search bar with a magnifying glass and a few blank result cards"
SUB[suitcase]="a carry-on travel suitcase standing upright with its handle extended, a luggage tag and a few blank stickers"
ID="Match the exact style of this reference image: an industrial design concept sketch with confident black fineliner and ballpoint lines, perspective construction lines and ellipse guides through the form, cross-section contour lines, light cool-grey marker shadows, small callout arrows and a circled detail. Draw a NEW subject (not clouds):"
TE="Match the exact style of this reference image: a technical spec drawing with thin precise cyan-blue lines, construction circles with centre marks, dashed hidden lines and dimension lines with arrowheads but no numbers, clean and architectural. Draw a NEW subject (not clouds):"
run() { python3 tools/gen_edit.py "$1" "$2" "$3 $4. $E" 1536x1024; }
for k in plane matcha lamp laptop suitcase; do
  run id-$k parts/sk-idsketch.png "$ID" "${SUB[$k]}" &
  run te-$k parts/sk-tech.png "$TE" "${SUB[$k]}" &
  wait
done
BL="Use this reference only for line quality. Draw ONE wide horizontal illustration of the design process for the same object repeated three times left to right, blending smoothly into each other with no hard borders: on the left a precise technical spec drawing in thin cyan-blue lines with construction circles, centre marks and dimension lines; in the middle the same object as a loose industrial design concept sketch in black fineliner with perspective guides and cross-section lines; on the right the same object as a finished industrial design marker rendering with cool grey Copic shading, black outlines, white highlights and one sky-blue accent. Transparent background, no text, no letters, no numbers, no frame. The object:"
python3 tools/gen_edit.py bl-lamp parts/sk-idsketch.png "$BL ${SUB[lamp]}." 1536x1024 &
python3 tools/gen_edit.py bl-plane parts/sk-idsketch.png "$BL ${SUB[plane]}." 1536x1024 &
wait
python3 tools/gen_edit.py bl-matcha parts/sk-idsketch.png "$BL ${SUB[matcha]}." 1536x1024
echo ALLDONE
