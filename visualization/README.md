# Interleaved bid explorer

Extract the ZIP and open index.html in a browser. It runs offline. Choose a seed count, move j, and switch between a target exactly at the breakpoint a^j and targets approaching it from above. The colored lanes follow the residue classes of the exponents. Filled circles mark stopping bids. Costs still include earlier bids when they are outside the visible window.

The GIF starts at the worked fair-bit case just above a^5. The stopping bids are a^6 and a^7, so the expected cost divided by the target has right limit 6305/1944. Later breakpoint limits approach 27/8. Use existing Python and Pillow to regenerate with python3 visualization/render.py. Fonts can change the GIF bytes.
