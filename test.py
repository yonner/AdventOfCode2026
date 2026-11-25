from pathlib import Path

text_buffer = Path("myfile.txt").read_text(encoding="utf-8")

print(text_buffer)