cd /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad
B="Redraw this exact illustration in the same blue ballpoint pen sketch style, same paper-free transparent background, same overall composition, size and position, same birds. Change only this: the big puffy cloud mass is now formed into the shape of"
E=", still made of soft billowy cloud puffs and hatching so it reads as a cloud that happens to look like that object. No text, no letters, no logos."
python3 tools/gen_edit.py cm-search parts/id_clouds.png "$B a long rounded search bar with a small magnifying glass at its left end$E" 1536x1024 &
python3 tools/gen_edit.py cm-house parts/id_clouds.png "$B a simple house with a pitched roof, a chimney and a door$E" 1536x1024 &
wait
python3 tools/gen_edit.py cm-lamp parts/id_clouds.png "$B an industrial-designed LED desk lamp with a long arm and a round head$E" 1536x1024
echo DONE
