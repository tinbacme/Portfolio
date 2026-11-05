cd /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad
while ! grep -q ALLDONE /tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/tasks/bg86y4c9w.output 2>/dev/null; do sleep 5; done
python3 tools/gen_new.py px-globe "Pixel art planet Earth globe, a perfect sphere seen from space, centred on the Pacific Ocean so that Southeast Asia and Vietnam are visible on the left edge and the west coast of North America (Oregon and Washington) on the right edge; flat two-colour pixel style with large square pixels: ocean in bright sky blue (#2f8cff), land in pure white, a few lighter blue pixels for shallow seas; crisp hard pixel edges, no gradients, no clouds, no labels. Transparent background around the sphere. No text, no letters." 1024x1024 transparent
echo ALLDONE
