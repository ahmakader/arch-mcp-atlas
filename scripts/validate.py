#!/usr/bin/env python3
"""Validate data/servers.json (schema, duplicates, formats). Exit 1 on problems."""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "data" / "servers.json").read_text(encoding="utf-8"))
CATS = {"BIM authoring", "CAD / drafting", "3D modeling & rendering", "OpenBIM / IFC", "GIS & site analysis", "Structural & energy analysis", "Construction management", "Cloud / APIs", "Presentation & design tools", "AI imagery & 3D generation", "Other"}
KINDS = {"official", "company", "community"}
REQ = ["name", "url", "software", "category", "maintainer", "kind", "description", "source"]
errors, seen = [], set()
for i, s in enumerate(data["servers"]):
    tag = f"#{i} {s.get('name', '?')}"
    for k in REQ:
        if not s.get(k):
            errors.append(f"{tag}: missing {k}")
    if s.get("category") not in CATS:
        errors.append(f"{tag}: bad category {s.get('category')!r}")
    if s.get("kind") not in KINDS:
        errors.append(f"{tag}: bad kind {s.get('kind')!r}")
    if not isinstance(s.get("software"), list) or not s.get("software"):
        errors.append(f"{tag}: software must be a non-empty list")
    if s.get("updated") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", s["updated"]):
        errors.append(f"{tag}: updated must be YYYY-MM-DD")
    if s.get("stars") is not None and not isinstance(s["stars"], int):
        errors.append(f"{tag}: stars must be an integer or null")
    key = (s.get("url") or "").lower().rstrip("/")
    if key in seen:
        errors.append(f"{tag}: duplicate url")
    seen.add(key)
    if len((s.get("description") or "")) > 220:
        errors.append(f"{tag}: description longer than 220 chars")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(data['servers'])} servers")
