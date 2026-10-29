#!/usr/bin/env python3
"""Validate structural and delivery invariants for a standalone HTML deck."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("html", type=Path)
    parser.add_argument("--min-slides", type=int, default=6)
    args = parser.parse_args()

    if not args.html.is_file():
        print(f"ERROR: file not found: {args.html}")
        return 2

    text = args.html.read_text(encoding="utf-8")
    lowered = text.lower()
    errors: list[str] = []
    warnings: list[str] = []

    if "<!doctype html>" not in lowered:
        errors.append("missing HTML5 doctype")
    if not re.search(r"<html\b[^>]*\blang=", lowered):
        errors.append("missing <html lang=...>")
    if "name=\"viewport\"" not in lowered:
        errors.append("missing viewport metadata")

    slide_count = len(re.findall(r"<section\b[^>]*\bclass=[\"'][^\"']*\bslide\b", lowered))
    if slide_count < args.min_slides:
        errors.append(f"found {slide_count} slides; expected at least {args.min_slides}")

    unresolved = re.findall(r"\b(?:todo|tbd|fixme)\b|\{\{[^}]+\}\}", lowered)
    if unresolved:
        errors.append(f"unresolved placeholders: {', '.join(sorted(set(unresolved)))}")

    external_scripts = re.findall(r"<script\b[^>]*\bsrc=[\"'](?:https?:)?//", lowered)
    if external_scripts:
        errors.append("external script dependency found")

    remote_styles = re.findall(r"<link\b[^>]*\bhref=[\"'](?:https?:)?//", lowered)
    if remote_styles:
        warnings.append("remote stylesheet or linked asset found")

    if "@media print" not in lowered:
        errors.append("missing print stylesheet")
    if "arrowright" not in lowered:
        warnings.append("keyboard navigation does not mention ArrowRight")

    semantic_checks = {
        "reference section": r"\breference|参考文献|文献与图片来源",
        "discussion questions": r"\bdiscussion|讨论问题",
        "figure source or caption": r"<figcaption|figure source|图片来源|图源",
    }
    for label, pattern in semantic_checks.items():
        if not re.search(pattern, lowered):
            warnings.append(f"missing or ambiguous {label}")

    if re.search(r"<img\b(?![^>]*\balt=)", lowered):
        errors.append("image without alt text found")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARN:  {message}")

    print(
        f"Checked {args.html}: {slide_count} slides, "
        f"{len(errors)} errors, {len(warnings)} warnings"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
