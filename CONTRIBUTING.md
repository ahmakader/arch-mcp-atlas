# Contributing

Thanks for helping keep this list accurate. The README and the website are **generated** from [`data/servers.json`](data/servers.json), so you only edit that one file.

## Add a server

1. Open [`data/servers.json`](data/servers.json) and add an object to `servers`:

```json
{
  "name": "example-revit-mcp",
  "url": "https://github.com/owner/example-revit-mcp",
  "software": ["Revit"],
  "category": "BIM authoring",
  "maintainer": "owner",
  "kind": "community",
  "license": "MIT",
  "language": "C#",
  "description": "One factual sentence in your own words about what it does.",
  "requirements": "Windows, Revit 2024-2026, plugin install",
  "tools": ["get_current_view_elements", "create_line_based_element"],
  "stars": 120,
  "updated": "2026-10-01",
  "registry": false,
  "source": "https://github.com/owner/example-revit-mcp"
}
```

2. Run `python3 scripts/validate.py` and then `python3 scripts/build.py`.
3. Open a pull request. CI checks the data and that the generated files are up to date.

## Rules

- **It must be an MCP server** for architecture, engineering or construction software (or a tool an architect clearly uses on that workflow). Plain plugins with no MCP do not belong here.
- **Verify it.** `source` must be a page that shows the project exists and works (repo, README or official docs). Do not add things you have not opened.
- **Describe, do not advertise.** One factual sentence, under 220 characters. Only quote tool counts the README states.
- **Be honest about the type.** `official` = made by the software vendor; `company` = a company product; `community` = an individual or community project.
- **Categories** are fixed: `BIM authoring`, `CAD / drafting`, `3D modeling & rendering`, `OpenBIM / IFC`, `GIS & site analysis`, `Structural & energy analysis`, `Construction management`, `Cloud / APIs`, `Presentation & design tools`, `AI imagery & 3D generation`, `Other`.
- Dates are `YYYY-MM-DD`; `stars` is a whole number or `null`.

## Report a dead or unsafe server

Open an issue with the link and what you found (archived, no longer works, suspicious code). Removed entries are replaced, not left as stubs.
