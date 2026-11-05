cd /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad
I="A single polished app-style 3D icon object, soft studio lighting, gentle shadows, smooth slightly glossy materials, rendered like a modern macOS app icon illustration, centered, filling most of the frame, transparent background, no rounded-square plate, no text, no letters, no logos."
run(){ python3 tools/gen_new.py "$1" "$I Subject: $2" 1024x1024 transparent; }
run k-matcha "a ceramic matcha bowl in soft sage green with frothy bright green matcha and a small bamboo whisk leaning on it." &
run k-plane "a small white passenger airplane with a blue tail, three-quarter view, slightly banking." &
wait
run k-lamp "an articulated desk lamp in warm orange enamel with a glowing bulb." &
run k-laptop "an open silver laptop whose screen shows a simple rounded search bar on a soft blue gradient." &
wait
run k-suitcase "a vintage hard-shell travel suitcase in teal with a brown leather handle and a couple of small travel stickers without text." &
run k-caphe "a tall glass of Vietnamese iced coffee with condensed milk layers, ice cubes and a small metal phin filter on top." &
wait
run k-cloud "a puffy white cumulus cloud with soft blue shading." &
run k-search "a chunky magnifying glass with a blue rim and a glossy lens." &
wait
echo ALLDONE
