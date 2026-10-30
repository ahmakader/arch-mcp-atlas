<div align="center">

<img src="assets/banner.svg" alt="Arch MCP Atlas: architecture × MCP servers" width="100%">

<p>
  <img alt="servers" src="https://img.shields.io/badge/servers-330-D3722A?style=for-the-badge&labelColor=16302C">
  <img alt="verified" src="https://img.shields.io/badge/verified-2026--10--30-1F5D56?style=for-the-badge&labelColor=16302C">
  <img alt="PRs welcome" src="https://img.shields.io/badge/PRs-welcome-F2904C?style=for-the-badge&labelColor=16302C">
</p>

**Arch MCP Atlas: a verified directory of MCP servers for architecture software.**<br>
Let Claude and other AI assistants work inside Revit, 3ds Max, SketchUp, Rhino, AutoCAD, Archicad, Blender and more.

[**Browse the searchable site →**](https://ahmakader.github.io/arch-mcp-atlas/) &nbsp;·&nbsp; [Add a server](CONTRIBUTING.md) &nbsp;·&nbsp; [Raw data](data/servers.json)

</div>

---

## What is this?

[MCP (Model Context Protocol)](https://modelcontextprotocol.io) is an open standard, introduced by Anthropic in November 2024, that lets an AI assistant call tools in other software. An **MCP server** is the small program that sits next to your application and exposes what it can do (create walls, read parameters, render a view) to the AI.

This list collects the ones that matter for architecture and AEC work, with what each is for, who maintains it and whether it is still alive. Each entry was checked on **2026-10-30** against its repository, vendor page or registry listing. A few vendor pages block automated access and were confirmed through secondary sources; treat those as less certain and always read the project's own README before installing.

**330 servers** in **11 categories**, **29** of them official from the software vendor.

## How to read the tables

| Mark | Meaning |
| :-- | :-- |
| 🟦 Official · 🟧 Company · ⬜ Community | Who made it: the software vendor, a company product, or an individual / community project |
| 🟢 / 🟡 / 🔴 / ⚪ | Last update within 6 months / within 12 months / older / unknown, relative to the verification date |
| ★ | GitHub stars when shown (– if not a GitHub project or not visible) |

> [!CAUTION]
> An MCP server can run commands and change your model. Start with read-only questions, work on a **copy** of the project, review what the AI does, and only install servers whose code you trust. Many of these are community projects that run scripts inside your CAD or BIM software.

## By software

| Software | Servers | Top pick |
| :-- | --: | :-- |
| **Revit** | 29 | [Autodesk Revit MCP Server (Revit 2027 public MCP, Technical Preview)](https://blog.autodesk.io/revit-2027-mcp-server-release/) 🟦 |
| **SketchUp** | 23 | [Trimble SketchUp Connector (MCP)](https://news.trimble.com/2026-04-28-Trimble-Links-SketchUp-with-Anthropics-Claude,-Bringing-New-Conversational-AI-powered-Capabilities-to-3D-Modeling) 🟦 |
| **Blender** | 22 | [Blender Lab MCP Server (official)](https://www.blender.org/lab/mcp-server/) 🟦 |
| **AutoCAD** | 20 | [Autodesk AutoCAD and Civil 3D MCP Server (Tech Preview)](https://help.autodesk.com/view/ADSKMCP/ENU/) 🟦 |
| **Rhino** | 20 | [RhinoAI (McNeel Rhino MCP)](https://github.com/mcneel/RhinoAI) 🟦 |
| **IFC** | 18 | [bim.house MCP](https://bim.house) 🟧 |
| **Grasshopper** | 16 | [LAMCP (LAmbda MCP)](https://github.com/gramaziokohler/lamcp) ⬜ |
| **IfcOpenShell** | 12 | [IfcMCP (ifcopenshell-mcp)](https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.9.0/src/ifcmcp) 🟦 |
| **DXF** | 11 | [Aspicio](https://github.com/frontsail-ai/aspicio) 🟧 |
| **FreeCAD** | 9 | [freecad-mcp (neka-nat)](https://github.com/neka-nat/freecad-mcp) ⬜ |
| **Navisworks** | 9 | [NavisCoord](https://github.com/HorizunGroup/naviscoord-mcp) 🟧 |
| **Civil 3D** | 8 | [Civil 3D MCP (barbosaihan)](https://github.com/barbosaihan/civil3d-mcp) ⬜ |
| **QGIS** | 8 | [QGISMCP (jjsantos01)](https://github.com/jjsantos01/qgis_mcp) ⬜ |
| **Autodesk Construction Cloud** | 7 | [APS MCP Server (aps-mcp-server-nodejs)](https://github.com/autodesk-platform-services/aps-mcp-server-nodejs) 🟦 |
| **DWG** | 7 | [CADaddy](https://github.com/AICodeForgedev/cadaddy) 🟧 |
| **Fusion** | 7 | [Autodesk Fusion MCP](https://github.com/Autodesk/ai-integrations/tree/main/fusion/local-mcp-server) 🟦 |
| **Maya** | 7 | [MayaMCP (PatrickPalmer)](https://github.com/PatrickPalmer/MayaMCP) ⬜ |
| **Onshape** | 6 | [Onshape MCP (hedless)](https://github.com/hedless/onshape-mcp) ⬜ |
| **Photoshop** | 6 | [Adobe for Creativity (official remote MCP)](https://www.usecarly.com/blog/adobe-mcp/) 🟦 |
| **Unity** | 6 | [Unity MCP Server (official, AI Assistant package)](https://docs.unity3d.com/Packages/com.unity.ai.assistant@2.19/manual/integration/unity-mcp-overview.html) 🟦 |
| **Unreal Engine** | 6 | [Flopperam Unreal Engine MCP](https://github.com/flopperam/unreal-engine-mcp) 🟧 |
| **3ds Max** | 5 | [3dsmax-mcp (cl0nazepamm)](https://github.com/cl0nazepamm/3dsmax-mcp) ⬜ |
| **Figma** | 5 | [Figma MCP Server (official)](https://github.com/figma/mcp-server-guide) 🟦 |
| **Procore** | 5 | [Procore MCP Server (TylerIlunga)](https://github.com/TylerIlunga/procore-mcp-server) ⬜ |

## Contents

- [🏛️ BIM authoring](#bim-authoring)  <sub>45</sub>
- [📐 CAD / drafting](#cad--drafting)  <sub>36</sub>
- [🧊 3D modeling & rendering](#3d-modeling--rendering)  <sub>118</sub>
- [🧱 OpenBIM / IFC](#openbim--ifc)  <sub>20</sub>
- [🗺️ GIS & site analysis](#gis--site-analysis)  <sub>26</sub>
- [📊 Structural & energy analysis](#structural--energy-analysis)  <sub>9</sub>
- [🏗️ Construction management](#construction-management)  <sub>25</sub>
- [☁️ Cloud / APIs](#cloud--apis)  <sub>5</sub>
- [🎨 Presentation & design tools](#presentation--design-tools)  <sub>18</sub>
- [✨ AI imagery & 3D generation](#ai-imagery--3d-generation)  <sub>14</sub>
- [🧰 Other](#other)  <sub>14</sub>

## The best of each category

Official and company servers come first, then community projects by GitHub stars. Only the top 10 per category are shown here; **everything is in the [full catalog](CATALOG.md)**.

### BIM authoring

🏛️ Create, query and edit building models: Revit, Archicad, Vectorworks and friends.

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Archicad Public MCP Server (Beta) / AI Assistant MCP](https://help.graphisoft.com/AC/30/INT/Topics/001_GettingHelp/AI_Assistant/public_mcp_connection.html) | Archicad 30 | 🟦 Official | – | ⚪ – | Archicad 30 built-in beta MCP server that lets compatible desktop AI tools (Claude Desktop, Cursor, ChatGPT Desktop, VS Code) read and manage BIM elements in open projects via stdio. |
| [Autodesk Revit MCP Server (Revit 2027 public MCP, Technical Preview)](https://blog.autodesk.io/revit-2027-mcp-server-release/) | Revit | 🟦 Official | – | 🟢 2026-09-29 | Autodesk's own add-on that exposes an open Revit 2027 model to MCP clients such as Claude Desktop or Cursor; the April 2026 preview was read-only and a September 2026 update split it into Read, Write and… |
| [Horizun Revit MCP](https://github.com/HorizunGroup/horizun-revit-mcp) | Revit | 🟧 Company | 65 | 🟢 2026-10-22 | Free open-source Windows MCP server and Revit add-in for typed BIM edits, families, drawings, CAD-to-BIM, audits, quantities, Excel, Power BI and exports; README states 125 tools and 481 named suboperations. |
| [NavisCoord](https://github.com/HorizunGroup/naviscoord-mcp) | Navisworks | 🟧 Company | 20 | 🟢 2026-10-20 | Open-source MCP server and Navisworks add-in for clash coordination that works with ChatGPT Desktop, Claude Desktop, Claude Code and Codex. |
| [AI Connector for Revit (NonicaTab)](https://github.com/NonicaTeam/AI-Connector-for-Revit) | Revit | 🟧 Company | 19 | 🟢 2026-10-07 | Commercial NonicaTab feature that connects Claude, Cursor or Copilot to Revit through 50+ predefined tools to inspect, select, edit and document elements; the GitHub repo only tracks issues and releases. |
| [AEC Pilot MCP](https://github.com/hmertkaramann/aec-pilot-mcp) | Revit, AutoCAD, Civil 3D, Navisworks, 3ds Max | 🟧 Company | 2 | 🟢 2026-10-15 | Commercial local MCP server running inside each Autodesk app (Revit, AutoCAD, Civil 3D, Navisworks and more); README states 480+ actions. |
| [Revit Converter MCP (Labs Future)](https://github.com/labsfuture/revit-converter-remote-mcp-release) | Revit | 🟧 Company | 1 | 🟢 2026-05-26 | Remote MCP server that converts uploaded .rvt files to XKT, IFC or DWG and answers natural-language BIM queries about the stored models. |
| [vn-revit-mcp (InnoPro)](https://github.com/Innoprovn/vn-revit-mcp) | Revit | 🟧 Company | 1 | 🟢 2026-10-15 | Open-source MCP server and Revit add-in (Vietnamese-language docs) with in-Revit chat, commands writable as single .cs files, undoable model edits and a Revit API lookup skill. |
| [Navisworks MCP (AECO MCPs)](https://aecomcps.com/navisworks) | Navisworks | 🟧 Company | – | ⚪ – | Free plug-in for Navisworks Manage: model tree and properties, sets/viewpoints, Clash Detective tests, coordination QA reports, TimeLiner/quantities and NWD/DWF exports. |
| [Revit MCP (AECO MCPs)](https://aecomcps.com/revit) | Revit | 🟧 Company | – | ⚪ – | Free add-in that lets AI assistants read and edit the open Revit model: query elements, schedules and warnings, create/edit elements, families, sheets, QA checks and C# scripting, with single-step undo. |

<sub>…and **35** more in the [full catalog](CATALOG.md).</sub>

### CAD / drafting

📐 2D/3D drafting and DWG/DXF automation: AutoCAD, FreeCAD, SolidWorks and general CAD.

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Autodesk AutoCAD and Civil 3D MCP Server (Tech Preview)](https://help.autodesk.com/view/ADSKMCP/ENU/) | AutoCAD, Civil 3D | 🟦 Official | – | ⚪ – | Local MCP server that runs inside AutoCAD or Civil 3D (AutoCAD 2027 era) to query, analyze and modify the open drawing; per a third-party review, the only supported client is Autodesk Assistant and AutoCAD… |
| [Bentley MicroStation MCP Server (early access)](https://www.bentley.com/en/infrastructure-ai/mcp-servers/) | MicroStation | 🟦 Official | – | ⚪ – | Bentley MCP server giving AI agents read/write access to DGN content through the MicroStation Python API; early access to a restricted group of users. |
| [Aspicio](https://github.com/frontsail-ai/aspicio) | DXF, vector PDF | 🟧 Company | 6 | ⚪ – | TypeScript DXF/vector-PDF viewer and engine usable by AI agents. |
| [CADaddy](https://github.com/AICodeForgedev/cadaddy) | DWG, DXF | 🟧 Company | 2 | ⚪ – | Free Rust 2D CAD app that opens and saves DWG/DXF and exposes an MCP interface for AI agents; source-available (FSL-1.1). |
| [cadlens-mcp](https://github.com/cadlens-co/cadlens-mcp) | DWG, DXF, DWF, Cadlens API | 🟧 Company | 1 | 🟢 2026-08-11 | MCP wrapper for the hosted Cadlens CAD parsing API that converts DWG/DXF/DWF drawings into structured JSON for agents. |
| [CAD-MCP (daobataotie)](https://github.com/daobataotie/CAD-MCP) | AutoCAD, GstarCAD, ZWCAD | ⬜ Community | 654 | 🟢 2026-10-27 | MCP server controlling AutoCAD and other CAD programs through natural language; v2.0 README states 35 tools covering query, editing, layers, blocks and command passthrough. |
| [autocad-mcp (puran-water, AutoCAD LT)](https://github.com/puran-water/autocad-mcp) | AutoCAD LT, AutoCAD | ⬜ Community | 606 | 🟡 2026-02-20 | MCP server for AutoCAD LT with freehand AutoLISP via file IPC, plus a headless ezdxf backend for DXF generation on any OS. |
| [Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad) | AutoCAD | ⬜ Community | 266 | 🟢 2026-10-15 | Chinese/English AutoCAD MCP integration server; README says it is not actively maintained. |
| [AutoCAD MCP Pro (U-C4N/Autocad-MCP)](https://github.com/U-C4N/autocad-mcp) | AutoCAD | ⬜ Community | 203 | 🟢 2026-10-26 | Python MCP server with a live COM engine on Windows and a headless ezdxf engine; v1.7 README states 248 registered tools. |
| [multiCAD-mcp](https://github.com/AnCode666/multiCAD-mcp) | AutoCAD, ZWCAD | ⬜ Community | 151 | 🟢 2026-06-27 | FastMCP-based server to control AutoCAD and other CAD programs from Claude Desktop or Cursor. |

<sub>…and **26** more in the [full catalog](CATALOG.md).</sub>

### 3D modeling & rendering

🧊 Modeling, scenes and renders: Rhino, SketchUp, 3ds Max, Blender, Unreal, Twinmotion.

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [RhinoAI (McNeel Rhino MCP)](https://github.com/mcneel/RhinoAI) | Rhino, Grasshopper | 🟦 Official | 387 | 🟢 2026-10-29 | Free MIT-licensed plugin and MCP server from McNeel that connects Rhino and Grasshopper to Claude, Copilot, Codex, Gemini or local LLMs to create geometry, run commands, edit scripts and build Grasshopper… |
| [Autodesk Fusion MCP](https://github.com/Autodesk/ai-integrations/tree/main/fusion/local-mcp-server) | Fusion | 🟦 Official | 0 | 🟢 2026-10-29 | Thin stdio bridge (MCPB bundle for Claude Desktop, or direct URL for Cursor) to the MCP server built into the Autodesk Fusion desktop app, for creating, modifying and inspecting geometry in a running Fusion session. |
| [Blender Lab MCP Server (official)](https://www.blender.org/lab/mcp-server/) | Blender | 🟦 Official | – | ⚪ – | Official Blender MCP server and companion add-on that give an LLM a natural-language interface to Blender's Python API, docs and scene; the page warns it runs LLM-generated code with no safeguards. |
| [Cinema 4D built-in MCP server (Maxon)](https://digitalproduction.com/2026/10/01/cinema-4d-2026-4-mcp/) | Cinema 4D | 🟦 Official | – | ⚪ – | Maxon's MCP server built into Cinema 4D 2026.4+, off by default, token-protected, with selectable tool groups, Python-execution controls and undo-grouped actions (per press coverage). |
| [Trimble SketchUp Connector (MCP)](https://news.trimble.com/2026-04-28-Trimble-Links-SketchUp-with-Anthropics-Claude,-Bringing-New-Conversational-AI-powered-Capabilities-to-3D-Modeling) | SketchUp | 🟦 Official | – | 🟢 2026-04-28 | Trimble-hosted remote MCP connector (announced 2026-04-28) that lets Claude build SketchUp (.skp) models in a cloud session from text and images and return a preview and download link. |
| [Unity MCP Server (official, AI Assistant package)](https://docs.unity3d.com/Packages/com.unity.ai.assistant@2.19/manual/integration/unity-mcp-overview.html) | Unity | 🟦 Official | – | ⚪ – | Unity Editor acts as an MCP server (relay binary plus editor bridge) exposing scene, asset, script and console tools; the manual page states it is now deprecated in favour of the Unity CLI. |
| [MCP for Unity](https://github.com/CoplayDev/unity-mcp) | Unity | 🟧 Company | 15.6k | 🟢 2026-10-19 | Most-starred Unity MCP bridge; manage assets, control scenes, edit scripts and run tests from an MCP client, not affiliated with Unity Technologies. |
| [Flopperam Unreal Engine MCP](https://github.com/flopperam/unreal-engine-mcp) | Unreal Engine | 🟧 Company | 1.1k | ⚪ – | Unreal Editor MCP with a hosted version and an open-source local Python version (50+ tools across 9 domains per README); README says the project is now owned by Aura. |
| [EngineWire / Unreal Engine MCP](https://github.com/ChiR24/Unreal_mcp) | Unreal Engine | 🟧 Company | 997 | 🟢 2026-10-30 | MCP server plus native C++ Automation Bridge plugin to drive a live Unreal Editor (levels, Blueprints, UI, materials, effects); README says Unreal 5.0-5.8 and a single tool with over 400 capabilities in 0.6.0. |
| [Fusion-360-MCP-Server (AuraFriday)](https://github.com/AuraFriday/Fusion-360-MCP-Server) | Fusion | 🟧 Company | 127 | 🟡 2026-01-28 | Fusion add-in (listed on Autodesk App Store) connecting Fusion to the Aura Friday MCP-Link server so AI agents can drive it. |

<sub>…and **108** more in the [full catalog](CATALOG.md).</sub>

### OpenBIM / IFC

🧱 Open standards: read, check and author IFC models.

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [IfcMCP (ifcopenshell-mcp)](https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.9.0/src/ifcmcp) | IfcOpenShell, IFC | 🟦 Official | 2.9k | 🟢 2026-10-30 | MCP server in the IfcOpenShell monorepo that wraps ifcquery and ifcedit and keeps an IFC model in memory across calls for querying, validating, clash checking, quantifying and editing. |
| [construction-iso-19650-mcp](https://github.com/CSOAI-ORG/construction-iso-19650-mcp) | ISO 19650, UK BIM Level 2 | 🟧 Company | 0 | 🟢 2026-06-26 | MCP server advertised for UK BIM Level 2 / ISO 19650 compliance (EIR, BEP, MIDP, CDE validation); README is generic template text so depth is unverified. |
| [ifc-lite (with MCP server)](https://github.com/LTplus-AG/ifc-lite) | IFC, WebGPU viewer, TypeScript SDK | ⬜ Community | 454 | 🟢 2026-10-30 | IFC toolkit (viewer, SDK, CLI, Rust/WASM core) whose CLI can start an MCP server so agents can query and edit BIM data. |
| [ifc-bonsai-mcp (Show2Instruct)](https://github.com/Show2Instruct/ifc-bonsai-mcp) | Blender, Bonsai (BlenderBIM), IfcOpenShell, IFC | ⬜ Community | 68 | 🟢 2026-07-10 | Original MCP4IFC research server connecting LLMs to Bonsai in Blender to read, create and edit IFC elements; README says it is superseded by bonsai-mcp but kept for reproducibility. |
| [Bonsai_mcp (JotaDeRodriguez)](https://github.com/JotaDeRodriguez/Bonsai_mcp) | Blender, Bonsai (BlenderBIM), IfcOpenShell, IFC | ⬜ Community | 66 | 🟢 2026-09-06 | Fork of BlenderMCP that adds IFC-specific tools (project info, spatial structure, properties, relationships, quantities) through Bonsai plus Blender code execution. |
| [openbim-mcp (Fragment MCP Server)](https://github.com/helenkwok/openbim-mcp) | That Open / web-ifc fragments, IFC | ⬜ Community | 39 | 🔴 2025-09-18 | MCP server that converts IFC files to the fragment format, loads fragments and queries BIM elements by IFC category. |
| [ifcMCP (smartaec)](https://github.com/smartaec/ifcmcp) | IFC, IfcOpenShell | ⬜ Community | 34 | 🔴 2025-06-08 | FastMCP server that lets LLM agents query IFC files through IfcOpenShell (entities, properties, locations, spatial containment, wall openings, space boundaries). |
| [ifc-ids-mcp (IDS MCP Server)](https://github.com/vinnividivicci/ifc-ids-mcp) | IDS, IfcOpenShell (IfcTester), IFC | ⬜ Community | 28 | 🟢 2026-04-06 | MCP server that creates, validates and manages buildingSMART IDS 1.0 files deterministically using IfcOpenShell's IfcTester. |
| [ifcx-mcp (louistrue)](https://github.com/louistrue/ifcx-mcp) | IFC5 / IFCX, IDS, BCF, bSDD | ⬜ Community | 25 | 🟢 2026-04-12 | MCP server for authoring IFC5/IFCX models in memory (spatial tree, types, geometry hints, materials, classifications) with IDS validation, BCF export and glTF preview. |
| [bonsai-mcp (Show2Instruct)](https://github.com/Show2Instruct/bonsai-mcp) | Blender, Bonsai (BlenderBIM), IfcOpenShell, IFC | ⬜ Community | 13 | 🟢 2026-08-20 | Local MCP server that bridges MCP clients to a running Blender + Bonsai session to inspect the scene, query the loaded IFC project, capture the viewport and run guarded Python code in Blender. |

<sub>…and **10** more in the [full catalog](CATALOG.md).</sub>

### GIS & site analysis

🗺️ Maps, parcels and context for site analysis.

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [MCP for ArcGIS Location Services (beta)](https://developers.arcgis.com/ai-tools/mcp-arcgis-location-services/) | ArcGIS Location Platform, ArcGIS Online, ArcGIS Enterprise | 🟦 Official | – | ⚪ – | Esri-hosted MCP server exposing ArcGIS Location Services for geocoding, reverse geocoding, routing, elevation and static map images; marked beta. |
| [Geospatial Power Pack for Kiro](https://github.com/aws-samples/sample-geospatial-kiro-power-pack) | STAC, H3/S2, point cloud, 3D | 🟧 Company | 23 | 🟢 2026-09-24 | AWS sample bundling modular geospatial MCP servers (data connectors, CRS/geometry/raster/point-cloud/3D processing) with a Kiro hub. |
| [arcgis-mcp-server (Esri Saudi Arabia)](https://github.com/esrisaudiarabia/esrisaudiarabia-mcp) | ArcGIS Online, ArcGIS Enterprise | 🟧 Company | – | 🟡 2025-10-16 | Content-search MCP server for ArcGIS Portal/Online items using user credentials; published on PyPI by Esri Saudi Arabia. |
| [LandRecords.us Parcel MCP Server](https://landrecords.us/documentation/mcp-server) | US parcel data | 🟧 Company | – | ⚪ – | Read-only hosted MCP server over a nationwide US parcel layer with attribute, point, radius, bbox and polygon queries. |
| [Regrid MCP Server](https://regrid.com/mcp) | Regrid parcel data | 🟧 Company | – | ⚪ – | Hosted MCP server over Regrid's US and Canada parcel data with docs search, schema exploration, counts and live parcel retrieval. |
| [QGISMCP (jjsantos01)](https://github.com/jjsantos01/qgis_mcp) | QGIS | ⬜ Community | 1.1k | 🟡 2025-10-01 | Original QGIS-to-Claude MCP bridge based on BlenderMCP; socket plugin in QGIS plus MCP server for projects, layers and PyQGIS execution. Many forks derive from it. |
| [qgis-mcp (nkarasiak)](https://github.com/nkarasiak/qgis-mcp) | QGIS | ⬜ Community | 400 | 🟢 2026-10-17 | QGIS plugin plus FastMCP server where agents drive QGIS: layers, feature editing, Processing, styling, layouts/atlas, cross-layer SQL; README states 125 tools. |
| [open-streetmap-mcp (jagan-shanmugam)](https://github.com/jagan-shanmugam/open-streetmap-mcp) | OpenStreetMap | ⬜ Community | 230 | 🔴 2025-06-30 | OSM MCP server for geocoding, POI search, routing and neighborhood exploration (schools, parking, EV charging). |
| [MCP-Server-ArcGIS-Pro-AddIn](https://github.com/nicogis/MCP-Server-ArcGIS-Pro-AddIn) | ArcGIS Pro | ⬜ Community | 54 | 🟢 2026-07-30 | MCP server delivered as an ArcGIS Pro add-in. |
| [MCP-ArcGISPro (geo2004)](https://github.com/geo2004/MCP-ArcGISPro) | ArcGIS Pro | ⬜ Community | 45 | 🟢 2026-09-13 | Controls and automates ArcGIS Pro from Claude Desktop over MCP. |

<sub>…and **16** more in the [full catalog](CATALOG.md).</sub>

### Structural & energy analysis

📊 Structural, energy and daylight analysis tools.

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP) | EnergyPlus | 🟦 Official | 124 | 🟢 2026-05-07 | MCP server with 35 tools to load, validate, modify and simulate EnergyPlus IDF models. |
| [OpenStudio-MCP](https://github.com/NatLabRockies/openstudio-mcp) | OpenStudio, EnergyPlus | 🟦 Official | 57 | 🟢 2026-10-28 | MCP server to create, query and modify OpenStudio building energy models, run EnergyPlus and read results; README states 150+ tools. |
| [OpenSTAAD MCP Server](https://github.com/BentleySystems/openstaad-mcp) | STAAD.Pro | 🟦 Official | 54 | 🟢 2026-10-22 | Bentley's MCP server for STAAD.Pro via the OpenSTAAD API, with a code-execution tool and API guidance tools. |
| [dlubal-mcp](https://pypi.org/project/dlubal-mcp/) | RFEM 6, RSTAB 9, RSECTION 1 | 🟦 Official | – | 🟢 2026-10-29 | MCP server for running Dlubal applications via the dlubal.api gRPC client, with script tools and a read-only results tool. |
| [etabs-mcp (Moha2005269)](https://github.com/Moha2005269/etabs-mcp) | CSI ETABS | ⬜ Community | 19 | 🟢 2026-10-18 | Agentic MCP server for CSI ETABS v22+ to model, load, analyse, design and inspect structures through the official ETABS API. |
| [ETABS-mcp (mdvaleed7)](https://github.com/mdvaleed7/ETABS-mcp) | CSI ETABS | ⬜ Community | 10 | 🟢 2026-06-23 | MCP server connecting LLMs to ETABS via the COM API to create models, apply loads, run analysis and design checks and query tables. |
| [hcl-mcp](https://github.com/akontadakis/hcl-mcp) | Radiance, EPW weather | ⬜ Community | 0 | 🟢 2026-09-02 | Human-centric lighting MCP server: spectral sky from EPW, CIE S 026 alpha-opic and circadian metrics, and Radiance daylight/glare pipelines. |
| [leed-mcp](https://github.com/akontadakis/leed-mcp) | Radiance, LEED v4.1 | ⬜ Community | 0 | 🟢 2026-10-10 | Local MCP server for LEED v4.1 BD+C daylight and quality-views calculations on a Radiance model. |
| [rad-mcp](https://github.com/akontadakis/rad-mcp) | Radiance, EPW weather | ⬜ Community | 0 | 🟢 2026-10-26 | Local MCP server for Radiance daylight studies: annual daylight (2/3/5-phase), LM-83 sDA/ASE, EN 17037, glare and electric lighting; README states 21 tools. |

### Construction management

🏗️ Clash detection, RFIs, issues, sheets and project platforms.

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [aps-mcp-app-example](https://github.com/autodesk-platform-services/aps-mcp-app-example) | Autodesk Construction Cloud, APS Viewer, MCP Apps | 🟦 Official | 21 | 🟢 2026-04-21 | Example MCP server with MCP Apps support that browses ACC projects and designs and shows an interactive APS Viewer preview; a live demo is hosted by Autodesk. |
| [Bluebeam Revu MCP server](https://support.bluebeam.com/revu/resources/revu-mcp.html) | Bluebeam Revu | 🟦 Official | – | ⚪ – | Built-in local MCP server in Bluebeam Revu 21.9+ (Max plan) with dozens of tools for markups, text extraction, search, stamping, bookmarks, redaction, page scale and Studio Project access. |
| [Revizto MCP Server](https://revizto.com/resources/blog/introducing-mcp-server) | Revizto | 🟦 Official | – | 🟢 2026-07-24 | Hosted Revizto MCP server giving AI tools read access to issues, clashes, stamp templates and model/object properties and write access to issues. |
| [ScanBIM MCP (AI Hub for AEC)](https://github.com/ScanBIM-Labs/scanbim-mcp) | Revit, Navisworks, Autodesk Construction Cloud, Autodesk Platform Services, Twinmotion | 🟧 Company | 6 | 🟢 2026-04-21 | Hosted Cloudflare Workers hub of MCP servers for AEC; README describes 46 tools across 5 workers covering model upload/viewing, clashes, ACC, Revit, XR and RFIs. |
| [ACC MCP (ScanBIM Labs)](https://github.com/ScanBIM-Labs/acc-mcp) | Autodesk Construction Cloud, BIM 360 | 🟧 Company | 0 | 🟢 2026-04-21 | Hosted MCP worker for Autodesk Construction Cloud issues, RFIs and document search via APS (9 tools). |
| [Aginera MCP](https://aginera.ai/agents) | Construction drawings (PDF), DXF/DWG | 🟧 Company | – | ⚪ – | Hosted MCP server for preconstruction: run and read takeoffs on drawing sets, return measured routes and schedules, export quantities, convert PDF drawings to CAD and render floor plans. |
| [Estimaite MCP](https://github.com/nickpanagios/estimaite-mcp) | Construction drawing PDFs | 🟧 Company | 0 | 🟢 2026-08-05 | Hosted remote MCP server that measures and counts scope on a drawing PDF by trade, prices it and exports an estimate; the repo holds only the manifest and docs. |
| [Navisworks MCP (ScanBIM Labs)](https://github.com/ScanBIM-Labs/navisworks-mcp) | Navisworks, Autodesk Platform Services | 🟧 Company | 0 | 🟢 2026-04-21 | MCP worker for multi-file coordination, clash detection and viewpoints via APS (repo About text). |
| [Portravo Construction Takeoff](https://portravo.com/developers/mcp) | Construction plan PDFs | 🟧 Company | – | ⚪ – | Hosted MCP server that runs construction plan takeoffs from PDFs, tracks status and returns quantities for review and Excel download. |
| [OpenTakeoff](https://github.com/Kentucky-ai/opentakeoff) | PDF construction plans, flooring takeoff | ⬜ Community | 719 | 🟢 2026-10-29 | Open-source in-browser PDF takeoff engine for construction that agents drive through an MCP server (README states 58 tools) to load plans, set scale, measure, count and export. |

<sub>…and **15** more in the [full catalog](CATALOG.md).</sub>

### Cloud / APIs

☁️ Cloud platforms and vendor APIs (Autodesk Platform Services and similar).

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [APS MCP Server (aps-mcp-server-nodejs)](https://github.com/autodesk-platform-services/aps-mcp-server-nodejs) | Autodesk Construction Cloud, Autodesk Platform Services | 🟦 Official | 25 | 🟢 2026-05-07 | Sample MCP server from Autodesk Platform Services that gives AI clients access to ACC project data through the Data Management and ACC APIs, authenticated with Secure Service Accounts. |
| [Zoo MCP](https://github.com/KittyCAD/zoo-mcp) | Zoo CAD API | 🟧 Company | 11 | ⚪ – | MCP server exposing Zoo (KittyCAD) CAD utilities. |
| [aps-mcp-server (petrbroz, moved)](https://github.com/petrbroz/aps-mcp-server) | Autodesk Construction Cloud, BIM 360 | ⬜ Community | 41 | 🟡 2025-10-29 | Earlier experimental APS MCP server using Secure Service Accounts; README says the project moved to autodesk-platform-services/aps-mcp-server-nodejs. |
| [speckle-mcp (bimgeek)](https://github.com/bimgeek/speckle-mcp) | Speckle | ⬜ Community | 14 | 🔴 2025-08-23 | Python MCP server for Speckle; repository README is empty, pyproject describes it as an MCP server for Speckle integration (directory listings describe project and model-version access). |
| [speckle-mcp (Daviidro)](https://github.com/Daviidro/speckle-mcp) | Speckle, Revit, Rhino, AutoCAD, Blender | ⬜ Community | 0 | ⚪ – | MCP server to manage Speckle projects, models and versions in natural language and give instructions for sending/receiving via Speckle connectors; repo About says 8 tools. |

### Presentation & design tools

🎨 Photoshop, Illustrator, InDesign, Figma, Canva and whiteboards for boards, drawings and review.

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Excalidraw MCP App (official)](https://github.com/excalidraw/excalidraw-mcp) | Excalidraw | 🟦 Official | 5.6k | 🟡 2026-03-24 | Excalidraw MCP App server (remote https://mcp.excalidraw.com or local) streaming hand-drawn diagrams with interactive editing, useful for sketching and review. |
| [Figma MCP Server (official)](https://github.com/figma/mcp-server-guide) | Figma | 🟦 Official | 2.1k | 🟢 2026-10-28 | Figma's official remote MCP server (https://mcp.figma.com/mcp) giving agents design context and canvas write access; this repo is its guide. |
| [Adobe for Creativity (official remote MCP)](https://www.usecarly.com/blog/adobe-mcp/) | Photoshop, Illustrator, InDesign, Lightroom, Premiere, Express, Firefly | 🟦 Official | – | ⚪ – | Adobe-hosted remote MCP connector at adobe-creativity.adobe.io/mcp spanning Creative Cloud apps and Firefly (details from a third-party write-up; Adobe pages not reachable). |
| [Canva MCP (official remote)](https://mcp.canva.com/mcp) | Canva | 🟦 Official | – | ⚪ – | Canva's remote MCP server (registry entry) to create, search, edit and export designs and assets. |
| [Miro MCP Server (official)](https://developers.miro.com/docs/miro-mcp-server-frequently-asked-questions) | Miro | 🟦 Official | – | ⚪ – | Miro's hosted MCP gateway (https://mcp.miro.com) to read and edit boards, frames, stickies, shapes, docs and generate diagrams. |
| [Framelink MCP for Figma](https://github.com/GLips/Figma-Context-MCP) | Figma | 🟧 Company | 16.1k | 🟢 2026-06-24 | Popular MCP that feeds Figma layout data to coding agents such as Cursor to implement designs. |
| [Photoshop-MCP-IMT](https://github.com/Immersive-Media-Technologies/photoshop-mcp-imt) | Photoshop | 🟧 Company | 2 | 🟢 2026-10-28 | Photoshop MCP with a skills library, support for every UI language and Adobe generative features (Generative Fill, Expand, Upscale); registry lists 134 tools behind a 9-tool facade. |
| [Figma Console MCP](https://github.com/southleft/figma-console-mcp) | Figma | ⬜ Community | 2.6k | 🟢 2026-10-29 | Design-system-focused bidirectional Figma MCP with design-code parity, accessibility checks and write access. |
| [Photoshop MCP (alisaitteke)](https://github.com/alisaitteke/photoshop-mcp) | Photoshop | ⬜ Community | 771 | ⚪ – | Unofficial Photoshop MCP; README says 118 tools and a built-in chat window. |
| [adb-mcp (Photoshop and Premiere)](https://github.com/mikechambers/adb-mcp) | Photoshop, Premiere Pro | ⬜ Community | 735 | 🟢 2026-07-08 | Proof-of-concept that lets LLMs control Photoshop and Premiere through a UXP plugin and Node proxy; not endorsed by Adobe. |

<sub>…and **8** more in the [full catalog](CATALOG.md).</sub>

### AI imagery & 3D generation

✨ Image, 3D-model and Gaussian-splat generation for concepts and visualization.

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Tripo MCP (official)](https://github.com/VAST-AI-Research/tripo-mcp) | Tripo, Blender | 🟦 Official | 224 | 🔴 2025-04-14 | Official Tripo MCP (alpha) that generates 3D assets from natural language and imports them into Blender; last commit April 2025. |
| [Meshy MCP Server](https://github.com/meshy-dev/meshy-mcp-server) | Meshy | 🟦 Official | 86 | 🟢 2026-10-26 | Meshy's MCP server for text/image-to-3D, retexture, remesh, rigging, animation and conversion; README states 28 tools. |
| [Rodin API MCP](https://github.com/DeemosTech/rodin-api-mcp) | Hyper3D Rodin | 🟦 Official | 6 | 🔴 2025-04-22 | MCP exposing the Rodin 3D generation API; GitHub shows the repository archived (read-only) on 2026-10-28. |
| [Midjourney MCP (AceDataCloud)](https://github.com/AceDataCloud/MidjourneyMCP) | Midjourney | 🟧 Company | 16 | 🟢 2026-10-18 | MCP for Midjourney image/video generation, upscaling, variations, blending and editing via the Ace Data Cloud API (not Midjourney itself). |
| [GetFacade MCP](https://github.com/getfacade/mcp) | GetFacade.ai | 🟧 Company | 1 | 🟢 2026-10-01 | MCP for designing, pricing and documenting house exteriors from a photo. |
| [ComfyUI MCP (artokun)](https://github.com/artokun/comfyui-mcp) | ComfyUI | ⬜ Community | 880 | ⚪ – | Local-first MCP server plus sidebar agent for ComfyUI to generate images/video/audio, author workflows and edit live graphs. |
| [ComfyUI MCP Server (joenorton)](https://github.com/joenorton/comfyui-mcp-server) | ComfyUI | ⬜ Community | 411 | 🟡 2026-02-17 | Lightweight Python MCP server to generate and iteratively refine images, audio and video with a local ComfyUI. |
| [Nano Banana MCP](https://github.com/ConechoAI/Nano-Banana-MCP) | Gemini image | ⬜ Community | 236 | 🟡 2025-11-04 | MCP for Gemini 2.5 Flash Image generation and iterative editing with reference images. |
| [Stability AI MCP](https://github.com/tadasant/mcp-server-stability-ai) | Stable Diffusion | ⬜ Community | 84 | 🔴 2025-06-24 | MCP integrating Stability AI hosted API for image generation, editing and upscaling; last commit June 2025. |
| [Sketchfab MCP Server](https://github.com/gregkop/sketchfab-mcp-server) | Sketchfab | ⬜ Community | 44 | 🔴 2025-03-09 | MCP to search, inspect and download 3D models from Sketchfab (gltf, glb, usdz, source). |

<sub>…and **4** more in the [full catalog](CATALOG.md).</sub>

### Other

🧰 Everything else that is useful on an architecture workflow.

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Autodesk Product Help MCP](https://github.com/Autodesk/ai-integrations/tree/main/product-help/remote-mcp-server) | AutoCAD, Revit, Civil 3D, Maya, Fusion, Inventor | 🟦 Official | 0 | 🟢 2026-10-29 | Autodesk-hosted, read-only remote MCP server (Streamable HTTP, no authentication) that searches official Autodesk Help and Support documentation for 110+ products. |
| [solidworks-api-mcp](https://github.com/ZCAD-Products/solidworks-api-mcp) | SolidWorks API docs | 🟧 Company | 9 | 🟢 2026-10-12 | Documentation-search MCP over about 14,000 SolidWorks API entries; not a CAD controller. |
| [Legis-Link](https://github.com/eutech-directory/legis-link-mcp) | AU/UK/US/Canada/EU construction codes | 🟧 Company | 1 | 🟢 2026-10-30 | Construction compliance MCP server returning a verdict with standard and clause for trade questions across AU, UK, US, Canada and EU codes. |
| [permitstack-mcp](https://github.com/PermitStack/permitstack-mcp) | PermitStack API, US building permits | 🟧 Company | 1 | 🟢 2026-10-21 | MCP server for the PermitStack API to search US building-permit records across thousands of cities. |
| [AI Architectures MCP](https://plans.ai-architectures.com/ai-assistants) | DXF, DWG, IFC (house plans) | 🟧 Company | – | ⚪ – | Remote MCP server to search free house plans and have AI-drafted CAD floor plans (DXF/DWG/PDF) created and changed. |
| [bim.house MCP](https://bim.house) | IFC, DXF | 🟧 Company | – | ⚪ – | Site states external AI can use MCP for building-material search, property creation and building-code checks; exports IFC4/DXF/STL; details sparse. |
| [3D New Era AI](https://github.com/leandrodaf/3d-new-era-ai) | home design editor | ⬜ Community | 36 | 🟢 2026-10-29 | Open-source Rust floor-plan and home design editor with built-in MCP server so agents draw walls and furnish rooms. |
| [ArchLang](https://github.com/ChanMeng666/archlang) | floor plans (DSL) | ⬜ Community | 26 | ⚪ – | Floor-plans-as-code DSL compiling to SVG, DXF or PDF; listed on Glama as an MCP server. |
| [building-standards-act-mcp](https://github.com/Sora-bluesky/building-standards-act-mcp) | Japanese Building Standards Act, e-Gov API v2 | ⬜ Community | 5 | 🟢 2026-10-28 | MCP server that fetches Japanese building-regulation text from the e-Gov API v2 to ground AI answers in permit reviews. |
| [pointcloud-mcp](https://github.com/jyou-syo/pointcloud-mcp) | LAS/LAZ point clouds, CloudCompare | ⬜ Community | 2 | 🟢 2026-05-17 | MCP server for LAS/LAZ point-cloud processing: loading, differencing surveys, cut/fill volumes, heatmaps and PDF reports (README in Japanese with English version). No E57 mentioned. |

<sub>…and **4** more in the [full catalog](CATALOG.md).</sub>

## Connect a server (quick start)

Most servers follow the same pattern. Install the server (and its plugin or add-in inside the software if it needs one), then add it to your AI client. For example, in Claude Desktop's `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "my-server": {
      "command": "uvx",
      "args": ["package-name"]
    }
  }
}
```

In Claude Code: `claude mcp add my-server -- uvx package-name`. Each server's own README has the exact command, the supported software versions and any plugin you must install first.

## Contributing

Know a server that is missing, or one that is broken or abandoned? Open an [issue](../../issues/new/choose) or a pull request. The README and the website are generated from [`data/servers.json`](data/servers.json), so edit that file and run `python3 scripts/build.py`. See [CONTRIBUTING.md](CONTRIBUTING.md) for the rules (every entry must link to a page that shows it exists and works).

## Disclaimer

Independent list, not affiliated with Autodesk, Trimble, McNeel, Graphisoft, Blender Foundation, Epic Games or any listed project. Names and logos belong to their owners. Information may be out of date: check each project's own page before you rely on it.

<div align="center"><sub>Curated by <a href="https://github.com/ahmakader">Ahmed Kader</a> · MIT licensed</sub></div>
