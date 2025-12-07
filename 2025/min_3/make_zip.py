import base64
import zlib

with open("3min.py", "r") as in_file:
    file_data = in_file.read()

compressed = zlib.compress(file_data.encode("utf-8"), level=9)
encoded = base64.b85encode(compressed).decode("utf-8")

with open("3zip.py", "w", encoding="ascii") as out_file:
    out_file.write(
        f"import zlib as z, base64 as b;exec(z.decompress(b.b85decode('{encoded}')))"
    )
