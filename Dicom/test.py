"""Convert the sample DICOM test images to JPEG.

Run from any working directory with: python Dicom/test.py
"""
from pathlib import Path

import numpy as np
import pydicom
from PIL import Image

ROOT = Path(__file__).resolve().parent
INPUT_DIR = ROOT / "Test_Images"
OUTPUT_DIR = ROOT / "converted"


def convert_dcm_jpg(path: Path) -> Image.Image:
    """Read a DICOM file and scale its pixel array to an 8-bit JPEG image."""
    dataset = pydicom.dcmread(str(path))
    pixels = dataset.pixel_array.astype(float)
    peak = pixels.max()
    if peak <= 0:
        raise ValueError(f"DICOM image has no positive pixel values: {path.name}")
    scaled = (np.maximum(pixels, 0) / peak) * 255
    return Image.fromarray(np.uint8(scaled))


def main() -> int:
    files = sorted(INPUT_DIR.glob("*.dcm"))
    if not files:
        raise FileNotFoundError(f"No .dcm files found in {INPUT_DIR}")
    OUTPUT_DIR.mkdir(exist_ok=True)
    converted = 0
    for path in files:
        image = convert_dcm_jpg(path)
        image.save(OUTPUT_DIR / f"{path.stem}.jpg")
        converted += 1
    print(f"Converted {converted} DICOM files to {OUTPUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
