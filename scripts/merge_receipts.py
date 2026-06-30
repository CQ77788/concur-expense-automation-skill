from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image
from pypdf import PdfReader, PdfWriter


IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".tif", ".tiff"}


def image_to_pdf(image_path: Path, pdf_path: Path) -> None:
    image = Image.open(image_path)
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    image.save(pdf_path, "PDF", resolution=150.0)


def merge_files(inputs: list[Path], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    writer = PdfWriter()
    temporary_files: list[Path] = []

    for source in inputs:
        source = source.resolve()
        pdf_source = source
        if source.suffix.lower() in IMAGE_SUFFIXES:
            pdf_source = output.parent / f"{source.stem}.tmp.pdf"
            image_to_pdf(source, pdf_source)
            temporary_files.append(pdf_source)

        reader = PdfReader(str(pdf_source))
        for page in reader.pages:
            writer.add_page(page)

    with output.open("wb") as handle:
        writer.write(handle)

    for temp in temporary_files:
        temp.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge receipt PDFs/images into one PDF.")
    parser.add_argument("output", type=Path, help="Output PDF path")
    parser.add_argument("inputs", nargs="+", type=Path, help="Input PDF/image files")
    args = parser.parse_args()

    merge_files(args.inputs, args.output)


if __name__ == "__main__":
    main()

