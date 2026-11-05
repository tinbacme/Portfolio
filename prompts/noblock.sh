cd /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad
P="Keep this sketch exactly the same — same object, same linework, same accent colour, same position and size, same hatched ground shadow — but completely remove the flat rectangular colour block in the background, leaving only the sketch itself on a transparent background. No text, no new elements."
for k in plane matcha; do python3 tools/gen_edit.py nb-$k parts/ln-$k.png "$P" 1536x1024 & done; wait
for k in lamp laptop; do python3 tools/gen_edit.py nb-$k parts/ln-$k.png "$P" 1536x1024 & done; wait
python3 tools/gen_edit.py nb-suitcase parts/ln-suitcase.png "$P" 1536x1024
echo ALLDONE
