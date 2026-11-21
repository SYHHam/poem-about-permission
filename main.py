"""Write one short poem about agency to /output/entry.txt."""

import os

POEM = """The Map

I asked you the way.
You handed me the map,
folded twice, creased
along the road you took.

I ran my thumb along the crease,
then folded it again
along a road of mine."""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(POEM)
