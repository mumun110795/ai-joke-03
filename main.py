# ai-joke-03 entry (Python 3.13, standard library only): writes one fixed
# one-liner about AI coding agents to entry.txt in the output directory,
# byte for byte the same on every run, with no trailing newline.
import os
from pathlib import Path

JOKE = "I asked my agent to explain the code it wrote 90 seconds ago. It said, 'Great question,' and started guessing like it had been hired that morning."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
