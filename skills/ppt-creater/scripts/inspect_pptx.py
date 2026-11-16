#!/usr/bin/env python3
"""Inspect PPTX slide objects in presentation order without modifying the file."""

import argparse
import json
import posixpath
import re
import sys
import unicodedata
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import BadZipFile, ZipFile


def normalize(text):
    return re.sub(r"\s+", "", unicodedata.normalize("NFKC", text))


def read_slides(path):
    slides = []
    with ZipFile(path) as archive:
        presentation = ET.fromstring(archive.read("ppt/presentation.xml"))
        relationships = ET.fromstring(
            archive.read("ppt/_rels/presentation.xml.rels")
        )
        targets = {
            rel.attrib["Id"]: rel.attrib["Target"]
            for rel in relationships
            if rel.attrib.get("TargetMode") != "External"
        }
        for number, slide_id in enumerate(
            presentation.findall(".//{*}sldId"), start=1
        ):
            relationship_id = next(
                value
                for key, value in slide_id.attrib.items()
                if key.endswith("}id")
            )
            target = targets[relationship_id]
            part = posixpath.normpath(
                target.lstrip("/") if target.startswith("/")
                else posixpath.join("ppt", target)
            )
            root = ET.fromstring(archive.read(part))
            paragraphs = []
            for paragraph in root.findall(".//{*}p"):
                text = "".join(
                    node.text or "" for node in paragraph.findall(".//{*}t")
                )
                if text:
                    paragraphs.append(text)
            slides.append({
                "number": number,
                "part": part,
                "hidden": root.attrib.get("show") in {"0", "false"},
                "text": "\n".join(paragraphs),
                "native_tables": len(root.findall(".//{*}tbl")),
                "pictures": len(root.findall(".//{*}pic")),
                "native_charts": len(root.findall(".//{*}chart")),
            })
    return slides


def read_terms(path):
    entries = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(entries, list):
        raise ValueError("Terms must be a JSON list.")
    terms = []
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("Each term must be an object with a name.")
        name = entry.get("name")
        aliases = entry.get("aliases", [])
        if not isinstance(name, str) or not normalize(name):
            raise ValueError("Each term needs a nonempty name.")
        if not isinstance(aliases, list) or any(
            not isinstance(alias, str) or not normalize(alias)
            for alias in aliases
        ):
            raise ValueError("Aliases must be a list of nonempty strings.")
        terms.append({"name": name, "aliases": aliases})
    return terms


def check_terms(slides, terms):
    matched = []
    missing = []
    for term in terms:
        names = [term["name"], *term["aliases"]]
        occurrences = []
        for slide in slides:
            text = normalize(slide["text"])
            aliases = [name for name in names if normalize(name) in text]
            if aliases:
                occurrences.append({
                    "slide": slide["number"],
                    "matched_names": aliases,
                })
        if occurrences:
            matched.append({"name": term["name"], "occurrences": occurrences})
        else:
            missing.append(term["name"])
    return {"matched": matched, "missing": missing}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--terms", type=Path, help="JSON names and accepted aliases")
    parser.add_argument("--slide", type=int, help="One-based slide number to inspect")
    args = parser.parse_args()
    try:
        slides = read_slides(args.pptx)
        if args.slide is not None and not 1 <= args.slide <= len(slides):
            raise ValueError("Requested slide number is outside the deck.")
        selected = slides
        if args.slide is not None:
            selected = [slides[args.slide - 1]]
        report = {
            "file": str(args.pptx.resolve()),
            "slide_count": len(slides),
            "slides": selected,
            "text_scope": "Text in slide objects, excluding notes, images, "
                          "chart internals and inherited master text.",
        }
        exit_code = 0
        if args.terms:
            visible = [slide for slide in selected if not slide["hidden"]]
            report["coverage"] = check_terms(visible, read_terms(args.terms))
            exit_code = int(bool(report["coverage"]["missing"]))
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return exit_code
    except (OSError, BadZipFile, ET.ParseError, KeyError, ValueError, StopIteration) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
