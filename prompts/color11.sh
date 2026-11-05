cd /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad
CC="An authentic industrial design Copic marker rendering in COLOUR, the way product designers render on marker paper: loose black fineliner underdrawing with visible construction lines; the product's colour blocked in first with the lightest marker, then built up light to dark with 3-4 values of the SAME hue in fast parallel streaky strokes so each marker pass and overlap shows; warm grey markers layered under the colour for form shadows; a strong dark cast shadow; reflections as thin streaks of colour; crisp white gel-pen and white pencil edge highlights; a final quick black fineliner pass on contours. Behind the object, a loose hand-laid rectangular marker swatch in a pale complementary colour with streaky edges, like a designer's background block, offset slightly so the object pops out of it. Energetic and hand-made, not a clean digital render. Transparent background outside the swatch, no paper texture, no text, no letters, no logos, no signature."
O="Single object, three-quarter view, centered with generous margin."
IC="An industrial design concept sketch page in COLOUR: confident black fineliner and ballpoint linework stays dominant, with perspective guides, ellipse guides and cross-section contour lines left visible, a callout arrow to a circled detail; then quick marker colour washes on top in one main colour plus one small accent, laid loosely so they don't fill every edge, with grey marker shadows and white highlights. Transparent background, no paper texture, no text, no letters, no numbers, no logos, no signature."
python3 tools/gen_new.py cc-clouds "$CC Subject: a wide bank of cumulus clouds on the left and right with open space in the middle and a small flock of four birds; clouds rendered in white paper with cool and warm grey shadows and soft peach light on their tops, sitting on a loose sky-blue marker swatch." 1536x1024 transparent &
python3 tools/gen_new.py cc-plane "$CC Subject: a small passenger airliner in flight with a white fuselage, a deep teal belly stripe and a coral-red tail; pale sky-blue background swatch. $O" 1536x1024 transparent &
wait
python3 tools/gen_new.py cc-matcha "$CC Subject: a rust-terracotta glazed ceramic matcha bowl with bright green frothy tea and a natural bamboo whisk (chasen) on a cream ceramic stand; pale sage background swatch. $O" 1536x1024 transparent &
python3 tools/gen_new.py cc-lamp "$CC Subject: a modern LED desk lamp in safety orange with a dark grey articulated two-segment arm and a slim round head with a warm light glow; pale blue background swatch. $O" 1536x1024 transparent &
wait
python3 tools/gen_new.py cc-laptop "$CC Subject: an open space-grey laptop whose screen glows blue and shows a rounded search bar with a magnifying glass and a few result cards; pale yellow background swatch. $O" 1536x1024 transparent &
python3 tools/gen_new.py cc-suitcase "$CC Subject: a mustard-yellow carry-on suitcase standing upright with its handle extended, a brown leather luggage tag and a few colourful travel stickers; pale lilac background swatch. $O" 1536x1024 transparent &
wait
python3 tools/gen_new.py ic-plane "$IC Subject: a small passenger airliner in flight; main colour deep teal, accent coral on the tail. $O" 1536x1024 transparent &
python3 tools/gen_new.py ic-matcha "$IC Subject: a ceramic matcha bowl with frothy tea and a bamboo whisk on a stand; main colour matcha green, accent rust-terracotta on the bowl glaze. $O" 1536x1024 transparent &
wait
python3 tools/gen_new.py ic-lamp "$IC Subject: a modern LED desk lamp with an articulated two-segment arm and a round head; main colour safety orange, accent warm yellow light glow. $O" 1536x1024 transparent &
python3 tools/gen_new.py ic-laptop "$IC Subject: an open laptop showing a rounded search bar and result cards; main colour screen blue, accent warm yellow highlight on one result. $O" 1536x1024 transparent &
wait
python3 tools/gen_new.py ic-suitcase "$IC Subject: a carry-on travel suitcase with its handle extended, a luggage tag and stickers; main colour mustard yellow, accent coral on one sticker. $O" 1536x1024 transparent
echo ALLDONE
