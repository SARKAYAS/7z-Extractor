# pip install py7zr
import py7zr
from pathlib import Path

src = Path("kali-linux-2025.2-vmware-amd64.7z")
out_dir = Path("kali-linux-2025.2-vmware-amd64")
out_dir.mkdir(exist_ok=True)

with py7zr.SevenZipFile(src, mode='r') as archive:
    archive.extractall(path=out_dir)
