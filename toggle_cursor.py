import os
from pathlib import Path
import sys

def find_latest_roblox_folder() -> Path:
    versions_dir = Path.home() / "AppData" / "Local" / "Bloxstrap" / "Versions"
    version_folders = [f for f in versions_dir.iterdir() if f.is_dir()]
    latest_folder = max(version_folders, key=lambda f: f.stat().st_mtime)
    return latest_folder / "content" / "textures"

def toggle_file(original: Path, backup: Path):
    try:
        if original.exists():
            original.rename(backup)
        elif backup.exists():
            backup.rename(original)
    except:
        pass  # Silent failure

def main():
    try:
        textures_path = find_latest_roblox_folder()
        toggle_file(textures_path / "MouseLockedCursor.png", textures_path / "MouseLockedCursor.png.disabled")
        toggle_file(textures_path / "ArrowCursor.png", textures_path / "ArrowCursor.png.disabled")
        toggle_file(textures_path / "Cursors", textures_path / "Cursors.disabled")
    except:
        pass  # Silent failure

if __name__ == "__main__":
    main()
