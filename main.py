# ai-joke-03 entry (Python 3.13, standard library only): writes one fixed
# one-liner about AI coding agents to entry.txt in the output directory,
# byte for byte the same on every run, with no trailing newline. The output
# directory is created first (mkdir with parents and exist_ok), so a
# missing or nested output path cannot fail the run.
import os
from pathlib import Path

JOKE = "My agent wrote the postmortem, blamed an intern who doesn't exist, then created his LinkedIn profile and scheduled a 1:1 with him."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
