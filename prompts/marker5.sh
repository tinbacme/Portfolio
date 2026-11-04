cd /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad
S="Match the exact rendering style of this reference image: an industrial designer's marker rendering with cool grey Copic marker shading, confident black fineliner outlines, crisp white gel-pen highlights, and a single accent of sky-blue marker. Draw a NEW subject (not clouds):"
E="Single object, centered, three-quarter view, generous empty margin, transparent background, no paper texture, no text, no letters, no logos, no signature, no frame."
python3 tools/gen_edit.py mk-plane parts/sk-marker.png "$S a small passenger airliner in flight, three-quarter view, sky-blue accent on the tail and window line. $E" 1536x1024 &
python3 tools/gen_edit.py mk-matcha parts/sk-marker.png "$S a ceramic matcha bowl with frothy green tea, a bamboo whisk (chasen) resting beside it on a small whisk stand, sky-blue accent as a thin glaze ring on the bowl, the matcha rendered in soft green marker. $E" 1536x1024 &
wait
python3 tools/gen_edit.py mk-lamp parts/sk-marker.png "$S a modern LED desk lamp with an articulated two-segment arm and a slim round head, sky-blue accent on the light glow underneath, like a product concept rendering. $E" 1536x1024 &
python3 tools/gen_edit.py mk-laptop parts/sk-marker.png "$S an open laptop at three-quarter view, the screen showing a simple rounded search bar with a magnifying glass icon and a few blank result cards, sky-blue accent on the search bar. $E" 1536x1024 &
wait
python3 tools/gen_edit.py mk-suitcase parts/sk-marker.png "$S a carry-on travel suitcase standing upright with its handle extended, a few blank travel stickers and a luggage tag, sky-blue accent on one sticker. $E" 1536x1024
echo ALLDONE
