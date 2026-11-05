cd /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad
N="No people, no text, no letters, no logos, no signature, no border."
MOSS="A minimal 3D product still life: a low rolling miniature landscape of soft green moss along the bottom of the frame against a plain warm cream background that fills the upper two thirds; soft natural light, shallow depth of field, calm and premium, lots of empty space for text. On the moss, on the right side:"
FUZZ="A surreal minimal 3D render of soft rolling hills covered in short fuzzy matcha-green felt-like grass under a flat warm beige-cream sky, with small fluffy peach-tinted volumetric clouds; the hills occupy only the bottom third, the rest is empty sky for text; soft diffuse light, calm and playful."
w() { python3 tools/gen_new.py "$1" "$2 $N" 1536x1024 opaque; }
w wd-moss-lamp "$MOSS a small modern LED desk lamp with an articulated arm, its warm light glowing softly onto the moss." &
w wd-moss-laptop "$MOSS a small open laptop whose screen glows with a simple rounded search bar, sitting nestled in the moss." &
wait
w wd-moss-suitcase "$MOSS a small mustard-yellow carry-on suitcase standing in the moss with its handle up, like a traveller resting." &
w wd-moss-plane "$MOSS a single white folded paper airplane resting on the moss as if it just landed." &
wait
w wd-fuzz-plane "$FUZZ A tiny white airliner flies above the hills on the right, leaving a thin straight contrail across the sky." &
w wd-fuzz-matcha "$FUZZ Nestled between two hills on the right sits an oversized ceramic matcha bowl like a small lake of bright green tea, with a bamboo whisk standing beside it like a tree." &
wait
w wd-aerial-terraces "A top-down aerial painting in rich textured gouache: curving rice and tea terraces in fresh greens on hillsides, a thin winding river in teal, a few pine trees casting long shadows, and the small soft shadow of a passing airplane gliding across the terraces. Calm, meditative, lots of brush texture." &
w wd-window-meadow "A photograph from inside an airplane cabin looking out through an oval airplane window: outside, rolling green hills and a meadow of red, orange, yellow and white wildflowers streak by with strong horizontal motion blur under a clear blue sky; the cream window frame is softly in focus. Airy and joyful." &
wait
echo ALLDONE
