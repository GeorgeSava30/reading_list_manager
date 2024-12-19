import sys
from pathlib import Path

root_path = Path(__file__).parent
src_path = root_path / "src"
sys.path.append(str(src_path))

from src.cli import CLI

if __name__ == "__main__":
    CLI.display_menu()
