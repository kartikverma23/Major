"""Validate the repository's local chest X-ray dataset layout.

This is a lightweight preflight check; it does not train a model or make a
clinical prediction.
"""
from pathlib import Path
import argparse

IMAGE_EXTENSIONS = {".jpeg", ".jpg", ".png"}
EXPECTED_SPLITS = ("train", "test", "val")
EXPECTED_CLASSES = ("NORMAL", "PNEUMONIA")


def find_dataset_root(repo_root: Path) -> Path:
    candidates = [
        repo_root / "chest-xray-pneumonia" / "chest_xray" / "chest_xray",
        repo_root / "chest-xray-pneumonia" / "chest_xray",
    ]
    for candidate in candidates:
        if all((candidate / split).is_dir() for split in EXPECTED_SPLITS):
            return candidate
    raise FileNotFoundError(
        "Could not find train/test/val under chest-xray-pneumonia/chest_xray."
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = find_dataset_root(args.repo_root.resolve())
    print(f"Dataset root: {root.relative_to(args.repo_root.resolve())}")
    total = 0
    for split in EXPECTED_SPLITS:
        counts = {}
        for label in EXPECTED_CLASSES:
            folder = root / split / label
            files = [p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS]
            counts[label] = len(files)
            total += len(files)
        print(f"{split}: {counts}")
    print(f"Total image files: {total}")
    if total == 0:
        raise RuntimeError("Dataset folders were found, but no image files were detected.")
    print("Dataset layout check: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
