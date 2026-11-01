#!/usr/bin/env python3
"""Generate README.md and docs/data.json from data/servers.json. Stdlib only.

    python3 scripts/build.py          # rewrite generated files
    python3 scripts/build.py --check  # fail if they are out of date (used in CI)
"""
import json, sys, datetime, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data" / "servers.json").read_text(encoding="utf-8"))
META = DATA["meta"]
SERVERS = DATA["servers"]
VERIFIED = datetime.date.fromisoformat(META["verified"])

CATEGORIES = [
    ("BIM authoring", "🏛️", "Create, query and edit building models: Revit, Archicad, Vectorworks and friends."),
    ("CAD / drafting", "📐", "2D/3D drafting and DWG/DXF automation: AutoCAD, FreeCAD, SolidWorks and general CAD."),
    ("3D modeling & rendering", "🧊", "Modeling, scenes and renders: Rhino, SketchUp, 3ds Max, Blender, Unreal, Twinmotion."),
    ("OpenBIM / IFC", "🧱", "Open standards: read, check and author IFC models."),
    ("GIS & site analysis", "🗺️", "Maps, parcels and context for site analysis."),
    ("Structural & energy analysis", "📊", "Structural, energy and daylight analysis tools."),
    ("Construction management", "🏗️", "Clash detection, RFIs, issues, sheets and project platforms."),
    ("Cloud / APIs", "☁️", "Cloud platforms and vendor APIs (Autodesk Platform Services and similar)."),
    ("Presentation & design tools", "🎨", "Photoshop, Illustrator, InDesign, Figma, Canva and whiteboards for boards, drawings and review."),
    ("AI imagery & 3D generation", "✨", "Image, 3D-model and Gaussian-splat generation for concepts and visualization."),
    ("Other", "🧰", "Everything else that is useful on an architecture workflow."),
]
KIND_LABEL = {"official": "Official", "company": "Company", "community": "Community"}
KIND_BADGE = {"official": "🟦 Official", "company": "🟧 Company", "community": "⬜ Community"}


def months_old(d):
    if not d:
        return None
    y, m, dd = map(int, d.split("-"))
    return (VERIFIED.year - y) * 12 + (VERIFIED.month - m)


def status(s):
    a = months_old(s.get("updated"))
    if a is None:
        return "⚪", "unknown"
    if a <= 6:
        return "🟢", "active"
    if a <= 12:
        return "🟡", "slow"
    return "🔴", "stale"


def esc(t):
    return (t or "").replace("|", "\\|").replace("\n", " ").strip()


def stars(n):
    if n is None:
        return "–"
    return f"{n/1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def sort_key(s):
    order = {"official": 0, "company": 1, "community": 2}
    return (order.get(s["kind"], 3), -(s.get("stars") or 0), s["name"].lower())


def slug(t):
    """GitHub heading anchor: lowercase, drop punctuation, spaces become hyphens (no collapsing)."""
    return re.sub(r"[^a-z0-9 \-]", "", t.lower()).strip().replace(" ", "-")


def row(s):
    icon, _ = status(s)
    soft = ", ".join(s.get("software") or [])
    desc = esc(s["description"])
    return f"| [{esc(s['name'])}]({s['url']}) | {esc(soft)} | {KIND_BADGE[s['kind']]} | {stars(s.get('stars'))} | {icon} {s.get('updated') or '–'} | {desc} |"


TOP_N = 10


def software_groups():
    """Top software by server count, same selection as the coverage grid."""
    groups = {}
    for s in SERVERS:
        for sw in s.get("software") or []:
            groups.setdefault(sw, []).append(s)
    ranked = [(sw, items) for sw, items in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())) if len(items) >= 3 and sw != "Other"]
    return ranked[:24]


def software_index():
    """Coverage grid: software name, number of servers, link to its section in BY_SOFTWARE.md."""
    cells = [f"[**{esc(sw)}** · {len(items)}](BY_SOFTWARE.md#{slug(sw)})" for sw, items in software_groups()]
    while len(cells) % 4:
        cells.append("")
    rows = ["| " + " | ".join(cells[i:i + 4]) + " |" for i in range(0, len(cells), 4)]
    return "| | | | |\n| :-- | :-- | :-- | :-- |\n" + "\n".join(rows)


def render_by_software():
    ranked = software_groups()
    toc = " · ".join(f"[{esc(sw)}](#{slug(sw)})" for sw, _ in ranked)
    out = [f"# Servers by software\n\nEvery verified server for the {len(ranked)} most covered programs. A server that works with several programs appears under each. Verified {META['verified']}.\n\n[← Back to the README](README.md) · [Setup guide](GUIDE.md) · [Full catalog](CATALOG.md)\n\n**Jump to:** {toc}\n"]
    for sw, items in ranked:
        items = sorted(items, key=sort_key)
        out.append(f"## {esc(sw)}\n\n{len(items)} servers · [↑ back to the list](#servers-by-software)\n\n| Server | Works with | Type | ★ | Updated | What it does |\n| :-- | :-- | :-- | --: | :-- | :-- |\n" + "\n".join(row(x) for x in items) + "\n")
    return "\n".join(out)


def render_catalog():
    out = [f"# Full catalog\n\nEvery verified server ({len(SERVERS)}), grouped by category. Verified {META['verified']}. The [searchable site]({META.get('site', 'docs/index.html')}) has filters.\n\n[← Back to the README](README.md)\n"]
    for c, e, blurb in CATEGORIES:
        items = sorted([s for s in SERVERS if s["category"] == c], key=sort_key)
        if not items:
            continue
        out.append(f"## {e} {c} ({len(items)})\n\n| Server | Works with | Type | ★ | Updated | What it does |\n| :-- | :-- | :-- | --: | :-- | :-- |\n" + "\n".join(row(s) for s in items) + "\n")
    return "\n".join(out)


AR_INSTALL = """<div dir="rtl">

## 🇪🇬 إزاي أركّب سيرفر؟ (بالعربي، خطوة بخطوة)

فيه طريقتين. ابدأ بالأولى لأنها الأسهل، ولو ما نفعتش جرّب التانية.

### الطريقة 1: الأسهل، خلّي Claude يركّب لك

1. افتح **Claude Code** (من الترمنال أو من تطبيق Claude). ده الأفضل لأنه يقدر يشغّل الأوامر ويعدّل الملفات على جهازك.
2. اختار السيرفر اللي عايزه من الجداول تحت، وافتح صفحته على GitHub، وانسخ الرابط.
3. الصق الرابط في Claude واكتب له:

</div>

```text
ركّب لي الـ MCP server ده على جهازي واتبع خطوات الـ README بتاعه خطوة خطوة،
واشرح لي أي حاجة لازم أعملها بإيدي: <الصق الرابط هنا>
```

<div dir="rtl">

4. Claude هيطلب إذنك قبل أي أمر. **اقرا كل طلب** قبل ما توافق.
5. لما يخلص، اقفل Claude تماماً وافتحه تاني، واسأله: `What tools do you have from this server?`

### الطريقة 2: بإيدك، مثال على Revit

هنركّب سيرفر [mcp-servers-for-revit](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit). محتاج: ويندوز، Revit من 2020 لـ 2026، و[Node.js](https://nodejs.org/) (نزّل نسخة LTS).

**1. نزّل Claude Desktop.** من [claude.ai/download](https://claude.ai/download)، ركّبه وسجّل دخول بحسابك.

**2. ركّب الـ plugin في Revit.** افتح صفحة [Releases](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/releases) بتاعة المشروع، ونزّل ملف الـ ZIP المناسب لنسخة Revit عندك، وفكّه، وانسخ اللي جواه في الفولدر ده:

</div>

```text
%AppData%\\Autodesk\\Revit\\Addins\\<نسخة Revit بتاعتك>\\
```

<div dir="rtl">

**3. ضيف السيرفر في Claude.** من القايمة اللي فوق في Claude اختار **Settings** ثم **Developer** ثم **Edit Config**. هيفتح ملف، الصق فيه ده واحفظ:

</div>

```json
{
  "mcpServers": {
    "mcp-server-for-revit": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "mcp-server-for-revit"]
    }
  }
}
```

<div dir="rtl">

لو في الملف سيرفرات تانية، ضيف ده جوه نفس الـ `"mcpServers"` وحط فاصلة بينهم.

**4. شغّل Revit.** لو سألك عن add-in مش معروف اضغط **Always Load**. بعدين افتح تبويب **mcp-servers-for-revit** في الشريط اللي فوق، واضغط **Settings**، وفعّل الأوامر اللي عايزها، واضغط **Save**.

**5. اقفل Claude تماماً وافتحه.** مش بس تقفل الشباك: كليك يمين على أيقونة Claude جنب الساعة واختار **Quit**، وافتحه تاني.

**6. جرّب.** افتح موديل (**نسخة منه، مش الأصلي**) واكتب لـ Claude: `What can you do in Revit? List your tools.` وابدأ بأسئلة قراءة بس، زي: "اعرض لي الـ levels اللي في الموديل".

لو حاجة ما اشتغلتش، بص على جدول المشاكل وحلولها في [الدليل الكامل](GUIDE.md#if-it-does-not-work) (بالإنجليزي). وبرضه لو كنت بتركّب برنامج تاني غير Revit (Blender, SketchUp, Rhino...)، الطريقة 1 هتمشي معاك على طول.

</div>
"""


def render_readme():
    n = len(SERVERS)
    off = sum(1 for s in SERVERS if s["kind"] == "official")
    soft = sorted({x for s in SERVERS for x in (s.get("software") or [])})
    toc = "\n".join(f"- [{e} {c}](#{slug(e + ' ' + c) if False else slug(c)})  <sub>{sum(1 for s in SERVERS if s['category']==c)}</sub>" for c, e, _ in CATEGORIES if any(s["category"] == c for s in SERVERS))
    sections = []
    for c, e, blurb in CATEGORIES:
        items = sorted([s for s in SERVERS if s["category"] == c], key=sort_key)
        if not items:
            continue
        more = ""
        if len(items) > TOP_N:
            more = f"\n<sub>…and **{len(items) - TOP_N}** more in the [full catalog](CATALOG.md).</sub>\n"
        sections.append(f"### {c}\n\n{e} {blurb}\n\n| Server | Works with | Type | ★ | Updated | What it does |\n| :-- | :-- | :-- | --: | :-- | :-- |\n" + "\n".join(row(s) for s in items[:TOP_N]) + "\n" + more)
    badges = (
        f'<img alt="servers" src="https://img.shields.io/badge/servers-{n}-D3722A?style=for-the-badge&labelColor=16302C">\n'
        f'  <img alt="verified" src="https://img.shields.io/badge/verified-{META["verified"].replace("-", "--")}-1F5D56?style=for-the-badge&labelColor=16302C">\n'
        f'  <img alt="PRs welcome" src="https://img.shields.io/badge/PRs-welcome-F2904C?style=for-the-badge&labelColor=16302C">'
    )
    return f"""<div align="center">

<img src="assets/banner.svg" alt="Arch MCP Atlas: architecture × MCP servers" width="100%">

<p>
  {badges}
</p>

**Arch MCP Atlas: a verified directory of MCP servers for architecture software.**<br>
Let Claude and other AI assistants work inside Revit, 3ds Max, SketchUp, Rhino, AutoCAD, Archicad, Blender and more.

[**Browse the searchable site →**]({META.get('site', 'docs/index.html')}) &nbsp;·&nbsp; [**Setup guide for beginners →**](GUIDE.md) &nbsp;·&nbsp; [Add a server](CONTRIBUTING.md) &nbsp;·&nbsp; [Raw data](data/servers.json)

</div>

---

## New to MCP? Start here

<a href="GUIDE.md"><img src="docs/guide/02-pick-your-way.svg" alt="Three ways to connect an MCP server to Claude" width="100%"></a>

**[Open the setup guide →](GUIDE.md)** Five steps with pictures: install Claude Desktop, add a server, switch it on in your software (real examples for Revit and Blender), and check that it works. No coding needed. The same guide is on the [website]({META.get('site', 'docs/index.html').rstrip('/')}/guide.html).

{AR_INSTALL}
## What is this?

[MCP (Model Context Protocol)](https://modelcontextprotocol.io) is an open standard, introduced by Anthropic in November 2024, that lets an AI assistant call tools in other software. An **MCP server** is the small program that sits next to your application and exposes what it can do (create walls, read parameters, render a view) to the AI.

This list collects the ones that matter for architecture and AEC work, with what each is for, who maintains it and whether it is still alive. Each entry was checked on **{META['verified']}** against its repository, vendor page or registry listing. A few vendor pages block automated access and were confirmed through secondary sources; treat those as less certain and always read the project's own README before installing.

**{n} servers** in **{len({s['category'] for s in SERVERS})} categories**, **{off}** of them official from the software vendor.

## How to read the tables

| Mark | Meaning |
| :-- | :-- |
| 🟦 Official · 🟧 Company · ⬜ Community | Who made it: the software vendor, a company product, or an individual / community project |
| 🟢 / 🟡 / 🔴 / ⚪ | Last update within 6 months / within 12 months / older / unknown, relative to the verification date |
| ★ | GitHub stars when shown (– if not a GitHub project or not visible) |

> [!CAUTION]
> An MCP server can run commands and change your model. Start with read-only questions, work on a **copy** of the project, review what the AI does, and only install servers whose code you trust. Many of these are community projects that run scripts inside your CAD or BIM software.

## Coverage by software

Software with the most servers. Each link jumps to that software's servers in [BY_SOFTWARE.md](BY_SOFTWARE.md). The [searchable site]({META.get("site", "docs/index.html")}) has more filters.

{software_index()}

## Contents

{toc}

## The best of each category

Official and company servers come first, then community projects by GitHub stars. Only the top {TOP_N} per category are shown here; **everything is in the [full catalog](CATALOG.md)**.

{chr(10).join(sections)}
## Connect a server

Install the server (and the plugin inside your software, if it needs one), then add it to Claude. The [setup guide](GUIDE.md) walks through it with pictures. The short version for Claude Desktop is **Settings → Developer → Edit Config**, paste the server's snippet from its README, save, and fully restart Claude. For Claude Code the command is `claude mcp add my-server -- npx -y package-name`.

## Contributing

Know a server that is missing, or one that is broken or abandoned? Open an [issue](../../issues/new/choose) or a pull request. The README and the website are generated from [`data/servers.json`](data/servers.json), so edit that file and run `python3 scripts/build.py`. See [CONTRIBUTING.md](CONTRIBUTING.md) for the rules (every entry must link to a page that shows it exists and works).

## Disclaimer

Independent list, not affiliated with Autodesk, Trimble, McNeel, Graphisoft, Blender Foundation, Epic Games or any listed project. Names and logos belong to their owners. Information may be out of date: check each project's own page before you rely on it.

<div align="center"><sub>Curated by <a href="https://github.com/{META['owner']}">{META['author']}</a> · MIT licensed</sub></div>
"""


def main():
    readme = render_readme()
    site = json.dumps({"meta": META, "categories": [c for c, _, _ in CATEGORIES], "servers": sorted(SERVERS, key=sort_key)}, ensure_ascii=False, indent=1)
    targets = {ROOT / "README.md": readme, ROOT / "CATALOG.md": render_catalog() + "\n", ROOT / "BY_SOFTWARE.md": render_by_software() + "\n", ROOT / "docs" / "data.json": site + "\n"}
    if "--check" in sys.argv:
        bad = [str(p.relative_to(ROOT)) for p, t in targets.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
        if bad:
            print("Out of date, run: python3 scripts/build.py ->", ", ".join(bad))
            sys.exit(1)
        print("Generated files are up to date.")
        return
    for p, t in targets.items():
        p.write_text(t, encoding="utf-8")
    print(f"Wrote README.md, CATALOG.md, BY_SOFTWARE.md and docs/data.json ({len(SERVERS)} servers)")


if __name__ == "__main__":
    main()
