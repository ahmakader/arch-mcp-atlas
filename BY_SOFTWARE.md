# Servers by software

Every verified server for the 24 most covered programs. A server that works with several programs appears under each. Verified 2026-10-30.

[← Back to the README](README.md) · [Setup guide](GUIDE.md) · [Full catalog](CATALOG.md)

**Jump to:** [Revit](#revit) · [AutoCAD](#autocad) · [Blender](#blender) · [SketchUp](#sketchup) · [Rhino](#rhino) · [Fusion](#fusion) · [Grasshopper](#grasshopper) · [IFC](#ifc) · [Civil 3D](#civil-3d) · [FreeCAD](#freecad) · [Maya](#maya) · [DXF](#dxf) · [Navisworks](#navisworks) · [IfcOpenShell](#ifcopenshell) · [ZWCAD](#zwcad) · [Autodesk Construction Cloud](#autodesk-construction-cloud) · [3ds Max](#3ds-max) · [Inventor](#inventor) · [Onshape](#onshape) · [DWG](#dwg) · [QGIS](#qgis) · [Unity](#unity) · [Unreal Engine](#unreal-engine) · [Figma](#figma)

## Revit

45 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [aps-sample-mcp-server-revit-automation](https://github.com/autodesk-platform-services/aps-sample-mcp-server-revit-automation) | Revit, APS | 🟦 Official | 10 | 🟡 2026-03-09 | Sample remote HTTP MCP server that automates Revit through the APS Automation API using Secure Service Account auth; README calls it an exploratory vibe-coded proof of concept. |
| [Autodesk Product Help MCP](https://github.com/Autodesk/ai-integrations/tree/main/product-help/remote-mcp-server) | AutoCAD, Revit, Civil 3D, Maya, Fusion, Inventor | 🟦 Official | 0 | 🟢 2026-10-29 | Autodesk-hosted, read-only remote MCP server (Streamable HTTP, no authentication) that searches official Autodesk Help and Support documentation for 110+ products. |
| [Autodesk Revit MCP Server (Revit 2027 public MCP, Technical Preview)](https://blog.autodesk.io/revit-mcp-server-update/) | Revit | 🟦 Official | – | 🟢 2026-09-29 | Autodesk's own add-on (Technical Preview) that exposes an open Revit 2027 model to MCP clients such as Claude Desktop or Cursor over local STDIO |
| [Horizun Revit MCP](https://github.com/HorizunGroup/horizun-revit-mcp) | Revit | 🟧 Company | 65 | 🟢 2026-10-22 | Free open-source Windows MCP server and Revit add-in for typed BIM edits, families, drawings, CAD-to-BIM, audits, quantities, Excel, Power BI and exports; README states 125 tools and 481 named suboperations. |
| [AI Connector for Revit (NonicaTab)](https://github.com/NonicaTeam/AI-Connector-for-Revit) | Revit | 🟧 Company | 19 | 🟢 2026-10-07 | Commercial NonicaTab feature that connects Claude, Cursor or Copilot to Revit through 50+ predefined tools to inspect, select, edit and document elements; the GitHub repo only tracks issues and releases. |
| [ScanBIM MCP (AI Hub for AEC)](https://github.com/ScanBIM-Labs/scanbim-mcp) | Revit, Navisworks, Autodesk Construction Cloud, Autodesk Platform Services, Twinmotion | 🟧 Company | 6 | 🟢 2026-04-21 | Hosted Cloudflare Workers hub of MCP servers for AEC; README describes 46 tools across 5 workers covering model upload/viewing, clashes, ACC, Revit, XR and RFIs. |
| [AEC Pilot MCP](https://github.com/hmertkaramann/aec-pilot-mcp) | Revit, AutoCAD, Civil 3D, Navisworks, 3ds Max | 🟧 Company | 2 | 🟢 2026-10-15 | Commercial local MCP server running inside each Autodesk app (Revit, AutoCAD, Civil 3D, Navisworks and more); README states 480+ actions. |
| [Revit Converter MCP (Labs Future)](https://github.com/labsfuture/revit-converter-remote-mcp-release) | Revit | 🟧 Company | 1 | 🟢 2026-05-26 | Remote MCP server that converts uploaded .rvt files to XKT, IFC or DWG and answers natural-language BIM queries about the stored models. |
| [vn-revit-mcp (InnoPro)](https://github.com/Innoprovn/vn-revit-mcp) | Revit | 🟧 Company | 1 | 🟢 2026-10-15 | Open-source MCP server and Revit add-in (Vietnamese-language docs) with in-Revit chat, commands writable as single .cs files, undoable model edits and a Revit API lookup skill. |
| [Revit MCP by ArchBench](https://github.com/3d-mcp/revit-mcp) | Revit | 🟧 Company | 0 | 🟢 2026-09-13 | Independent experimental Revit connector using pyRevit, with read-only or write bridge modes and an opt-in code-execution tool; alpha release. |
| [ScanBIM Revit MCP](https://github.com/ScanBIM-Labs/revit-mcp) | Revit | 🟧 Company | 0 | 🟢 2026-04-21 | Hosted Cloudflare Worker MCP server that works on uploaded Revit files via Autodesk Platform Services: elements, parameters, schedules, clash detection and IFC export. |
| [Skopia floor-plan layout](https://github.com/Skopia-mcp/Skopia-mcp) | DXF, AutoCAD, Revit | 🟧 Company | 0 | 🟢 2026-09-18 | Hosted MCP engine that draws a floor plan in real millimetres and projects consistent sections and elevations, exporting SVG, sheets or DXF. |
| [Twinmotion MCP](https://github.com/ScanBIM-Labs/twinmotion-mcp) | Twinmotion, Revit | 🟧 Company | 0 | 🟢 2026-04-21 | Twinmotion rendering pipeline via APS; README lists 5 tools. |
| [revit-mcp (original, archived/deprecated)](https://github.com/mcp-servers-for-revit/revit-mcp) | Revit | ⬜ Community | 475 | 🟡 2026-02-25 | The original TypeScript MCP server for Revit that pairs with the separate revit-mcp-plugin; its README now says the repo is being archived in favour of the mono repo. |
| [mcp-servers-for-revit (revit-mcp, Sparx fork)](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit) | Revit | ⬜ Community | 414 | 🟢 2026-04-05 | Mono repo combining a TypeScript MCP server, a C# Revit add-in and a command set so AI clients can read, create, modify and delete Revit elements; it is a fork of the original revit-mcp project with extra tools. |
| [mcp-server-for-revit-python](https://github.com/mcp-servers-for-revit/mcp-server-for-revit-python) | Revit | ⬜ Community | 220 | 🟢 2026-10-14 | pyRevit-based MCP server that uses pyRevit Routes as a bridge to Revit; README says the project is being prepared for Autodesk Marketplace review and retains 20 tools including Python execution. |
| [REVIT_MCP_study (Revit MCP)](https://github.com/shuotao/REVIT_MCP_study) | Revit | ⬜ Community | 109 | 🟢 2026-10-23 | Open-source MCP server plus C# Revit add-in; README states 239 MCP tools backed by 90 BIM SOPs (building code, quantity take-off, compliance checks). No license file found. |
| [rvt-mcp (BIMwright)](https://github.com/bimwright/rvt-mcp) | Revit | ⬜ Community | 107 | 🟢 2026-10-23 | MCP gateway for Revit with toolset gating and transaction-safe batch execution; README badge states 237 tools. |
| [Autodesk-Revit-MCP-Server / AEC Model Bridge](https://github.com/Sam-AEC/aec-model-bridge) | Revit | ⬜ Community | 90 | 🟢 2026-10-28 | Open-source MCP server and native add-in for Revit with a local-only bridge, folder allow-listing, and write tools blocked until a plan is approved (look_only mode refuses them outright). |
| [mcp-servers-for-revit (LuDattilo fork)](https://github.com/LuDattilo/revit-mcp-server) | Revit | ⬜ Community | 82 | 🟢 2026-04-09 | Fork of the revit-mcp project with a much larger tool set (README states 138 tools) plus an optional in-Revit Claude chat panel; targets Revit 2023-2027. |
| [RevitMCP (oakplank)](https://github.com/oakplank/RevitMCP) | Revit | ⬜ Community | 64 | 🟢 2026-09-30 | pyRevit extension plus Python MCP server (stdio) exposing 46 tools against a live Revit session. |
| [pyRevit-based Revit MCP (Demolinator)](https://github.com/Demolinator/revit-mcp-server) | Revit | ⬜ Community | 40 | 🟢 2026-09-30 | FastMCP server for Revit via pyRevit Routes; README states 48 tools for design, editing, analysis, clash detection, MEP, interop, documentation and model persistence. |
| [xml.Revit.MCP (ZedMoster/revit-mcp)](https://github.com/ZedMoster/revit-mcp) | Revit | ⬜ Community | 39 | 🟡 2025-12-24 | Python MCP package bridging AI assistants to Revit through the xml.Revit plugin, with tools such as creating doors and windows. |
| [RevitMCPGraphQL](https://github.com/GraphBIM/RevitMCPGraphQL) | Revit | ⬜ Community | 20 | 🟢 2026-07-02 | In-Revit GraphQL server for read and write operations with a Python client, built at a weekend hackathon as a GraphQL take on Revit MCP. |
| [AutodeskDynamo_MCP](https://github.com/ChimingLu/AutodeskDynamo_MCP) | Dynamo, Revit | ⬜ Community | 12 | 🟢 2026-10-20 | MCP integration that lets an AI drive Dynamo directly, with a node recipe registry, reusable node patterns, Dynamo Player input/output support and deployment scripts for Revit 2020-2027. |
| [Model MCP for Revit (revit-model-mcp)](https://github.com/sharafutdinovdi/revit-model-mcp) | Revit | ⬜ Community | 7 | 🟢 2026-10-30 | MCP server for live Revit projects where each change is one named undo entry and a read-only mode is one switch away; ships as MSI/Intune-ready installer and on PyPI. |
| [revit-mcp-toolkit](https://github.com/okuno-dsi/revit-mcp-toolkit) | Revit | ⬜ Community | 7 | 🟢 2026-09-13 | Japanese-language MCP-compatible toolkit (server plus add-in) for Revit automation over JSON-RPC, aimed at Japanese practice; not affiliated with Autodesk. |
| [vn-revit-mcp (andyluu98)](https://github.com/andyluu98/vn-revit-mcp) | Revit | ⬜ Community | 6 | 🟢 2026-10-16 | Vietnamese-language toolkit pairing pyRevit 7's MCP with a read-focused MCP for counts, quantities and Excel export; runs nine bundled scripts and 10 of 11 tools only read the model. |
| [BURAK-BIM](https://github.com/BURAKAFRIDI92/BURAK-BIM) | Revit, AutoCAD, Civil 3D, Navisworks, Inventor, ReCap | ⬜ Community | 2 | 🟢 2026-10-25 | Single MCP connector covering the Autodesk AEC stack (Revit, AutoCAD, Civil 3D, Plant 3D, Navisworks, Inventor, ReCap, Robot) versions 2022-2027 using locally compiled bridges. |
| [revit_mcp_dotnet_template](https://github.com/PiggyAndrew/revit_mcp_dotnet_template) | Revit | ⬜ Community | 2 | 🟡 2025-11-06 | .NET Core MCP server plus a Revit plugin template that bridges AI clients to Revit. |
| [revit-bridge (intent bridge)](https://github.com/revitbridge/revit-bridge) | Revit | ⬜ Community | 1 | 🟢 2026-10-27 | MCP server plus Claude Code plugin (skill and confirmation hook) that bridges designers' intent to Revit via a local add-in TCP listener. |
| [revit-mcp (hungpixi)](https://github.com/hungpixi/revit-mcp) | Revit, Dynamo | ⬜ Community | 1 | 🟢 2026-09-10 | Node.js MCP server with a native C# bridge connecting AI assistants to Revit and Dynamo for 2D-to-3D BIM modeling and model inspection. |
| [revit-mcp (rui-branco)](https://github.com/rui-branco/revit-mcp) | Revit | ⬜ Community | 1 | 🟢 2026-10-16 | MCP server to read and edit the open Revit model from an MCP client via a bundled C# bridge add-in; installable through npx or a Claude Code plugin. |
| [revit-mcp-hardened](https://github.com/elkhouryrafik-boop/revit-mcp-hardened) | Revit | ⬜ Community | 1 | 🟢 2026-08-03 | Fork of mcp-server-for-revit-python adding token auth, capability profiles, gated code execution and a strict MCP error contract. |
| [autodesk-cad-mcp-agent](https://github.com/MAvinash24/autodesk-cad-mcp-agent) | Fusion, Inventor, Revit, APS | ⬜ Community | 0 | 🟢 2026-09-09 | FastAPI microservice combining a C++ geometry evaluator with an MCP JSON-RPC interface and a RAG knowledge engine over Autodesk API docs. |
| [bim-cli Claude Code plugin](https://github.com/HelloHowAreYouHaveANiceDay/bim-cli-plugin) | Revit, AutoCAD, SketchUp, Blender | ⬜ Community | 0 | 🟢 2026-10-29 | Claude Code plugin exposing the Windows bim-cli verbs as MCP tools to drive Revit 2024-2027, check PDF drawing sets and look up US site/flood data. |
| [EraCore Revit MCP](https://github.com/soewal19/eracore-revit-mcp) | Revit, pyRevit | ⬜ Community | 0 | 🟢 2026-08-12 | Hexagonal-architecture MCP server exposing 7 typed Revit tools (model info, element listing, wall creation, batch parameter updates, schedule export) via pyRevit, with a fake mode for testing. |
| [MCP Revit Families](https://github.com/yllld/MCP-Revit-Families) | Revit, pyRevit | ⬜ Community | 0 | 🟢 2026-09-29 | Local MCP server that works in an open Revit 2021 family (RFA) via pyRevit, planning changes, creating geometry and filling confirmed equipment parameters; README calls it a limited prototype. |
| [pyRevit Foundry MCP](https://github.com/OnePowerUser88/pyRevitFoundryMCP) | pyRevit, Revit | ⬜ Community | 0 | 🟡 2026-02-14 | MCP server for developing and maintaining pyRevit extensions through static analysis: bundle inventory, bundle.yaml generation, import audit, duplicate detection and dry-run patches. |
| [Revit MCP (AECO MCPs)](https://aecomcps.com/revit) | Revit | ⬜ Community | – | ⚪ – | Free add-in that lets AI assistants read and edit the open Revit model: query elements, schedules and warnings, create/edit elements, families, sheets, QA checks and C# scripting, with single-step undo. |
| [revit-mcp (Antigravity bridge)](https://github.com/AndreyStartsev/revit-mcp) | Revit | ⬜ Community | 0 | 🟢 2026-10-09 | Standalone MCP bridge to Revit built for Google Antigravity and also usable from Claude Desktop, Cursor, Cline and Windsurf; Python server with a .NET 8 Revit add-in. |
| [revit-mcp-automation](https://github.com/ArchitectureWorld/revit-mcp-automation) | Revit | ⬜ Community | 0 | 🟢 2026-10-29 | Local Windows automation layer that launches an isolated Revit 2020 instance on demand, handles common dialogs and resumes the original model operation; reuses mcp-servers-for-revit tools (31 tools pe |
| [revit-mcp-stdio](https://github.com/DavidChin0/revit-mcp-stdio) | Revit, pyRevit | ⬜ Community | 0 | 🟢 2026-08-02 | pyRevit-based Revit MCP server with a stdio bridge over a Windows named pipe (plus HTTP fallback); README states 48 tools covering design, editing, analysis, clash detection and MEP. |
| [revit-tunnel-mcp](https://github.com/xiuchuan666/revit-tunnel-mcp) | Revit, pyRevit | ⬜ Community | 0 | 🟢 2026-08-27 | Specialised MCP for previewing, creating and verifying shield-tunnel segment rings in Revit 2025, with each segment placed as its own family instance inside a transaction group. |
| [speckle-mcp (Daviidro)](https://github.com/Daviidro/speckle-mcp) | Speckle, Revit, Rhino, AutoCAD, Blender | ⬜ Community | 0 | 🟢 2026-08-09 | MCP server to manage Speckle projects, models and versions in natural language and give instructions for sending/receiving via Speckle connectors; repo About says 8 tools. |

## AutoCAD

35 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Autodesk AutoCAD and Civil 3D MCP Server (Tech Preview)](https://help.autodesk.com/view/ADSKMCP/ENU/) | AutoCAD, Civil 3D | 🟦 Official | – | ⚪ – | Autodesk's local MCP server (Tech Preview / public beta) that runs inside AutoCAD or Civil 3D (AutoCAD 2027 era, Windows) so AI assistants can query, analyze, navigate and modify objects in the open drawing, check… |
| [Autodesk Product Help MCP](https://github.com/Autodesk/ai-integrations/tree/main/product-help/remote-mcp-server) | AutoCAD, Revit, Civil 3D, Maya, Fusion, Inventor | 🟦 Official | 0 | 🟢 2026-10-29 | Autodesk-hosted, read-only remote MCP server (Streamable HTTP, no authentication) that searches official Autodesk Help and Support documentation for 110+ products. |
| [AEC Pilot MCP](https://github.com/hmertkaramann/aec-pilot-mcp) | Revit, AutoCAD, Civil 3D, Navisworks, 3ds Max | 🟧 Company | 2 | 🟢 2026-10-15 | Commercial local MCP server running inside each Autodesk app (Revit, AutoCAD, Civil 3D, Navisworks and more); README states 480+ actions. |
| [Skopia floor-plan layout](https://github.com/Skopia-mcp/Skopia-mcp) | DXF, AutoCAD, Revit | 🟧 Company | 0 | 🟢 2026-09-18 | Hosted MCP engine that draws a floor plan in real millimetres and projects consistent sections and elevations, exporting SVG, sheets or DXF. |
| [CAD-MCP (daobataotie)](https://github.com/daobataotie/CAD-MCP) | AutoCAD, GstarCAD, ZWCAD | ⬜ Community | 654 | 🟢 2026-10-27 | MCP server controlling AutoCAD and other CAD programs through natural language; v2.0 README states 35 tools covering query, editing, layers, blocks and command passthrough. |
| [autocad-mcp (puran-water, AutoCAD LT)](https://github.com/puran-water/autocad-mcp) | AutoCAD LT, AutoCAD | ⬜ Community | 606 | 🟡 2026-02-20 | MCP server for AutoCAD LT with freehand AutoLISP via file IPC, plus a headless ezdxf backend for DXF generation on any OS. |
| [Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad) | AutoCAD | ⬜ Community | 266 | 🟢 2026-10-15 | Chinese/English AutoCAD MCP integration server; README says it is not actively maintained. |
| [AutoCAD MCP Pro (U-C4N/Autocad-MCP)](https://github.com/U-C4N/autocad-mcp) | AutoCAD | ⬜ Community | 203 | 🟢 2026-10-26 | Python MCP server with a live COM engine on Windows and a headless ezdxf engine; v1.7 README states 248 registered tools. |
| [multiCAD-mcp](https://github.com/AnCode666/multiCAD-mcp) | AutoCAD, ZWCAD | ⬜ Community | 151 | 🟢 2026-06-27 | FastMCP-based server to control AutoCAD and other CAD programs from Claude Desktop or Cursor. |
| [best-cad-mcp](https://github.com/LokmenoWer/best-cad-mcp) | AutoCAD | ⬜ Community | 33 | 🟢 2026-10-28 | Local handle-first MCP server for real AutoCAD drawings with a guarded inspect, plan, validate and export workflow. |
| [AutoCAD_MCP (ahmetcemkaraca, archived)](https://github.com/ahmetcemkaraca/AutoCAD_MCP_archive) | AutoCAD | ⬜ Community | 31 | 🟢 2026-10-09 | Experimental archived MCP bridge for AutoCAD on Windows; README lists five non-mutating tools and points to ACKaraca/AutoCAD_MCP for continued development. |
| [dwg-mcp](https://github.com/bimwright/dwg-mcp) | AutoCAD | ⬜ Community | 22 | 🟢 2026-10-30 | MCP gateway for AutoCAD 2022-2027 with text reading, spatial clustering, drawing translation rewriting and code execution. |
| [vn-autocad-claude](https://github.com/andyluu98/vn-autocad-claude) | AutoCAD, AutoCAD LT | ⬜ Community | 9 | 🟢 2026-10-21 | Fork-style AutoCAD/LT MCP server with eight consolidated tools, File IPC on Windows and headless ezdxf on macOS/Linux. |
| [AutoCAD-MCP (codesknight)](https://github.com/codesknight/AutoCAD-MCP) | AutoCAD | ⬜ Community | 8 | 🟢 2026-07-14 | Chinese-language MCP server for natural-language AutoCAD drawing from Claude Desktop or Cursor, derived from daobataotie/CAD-MCP. |
| [autocad-mcp (YQArch)](https://github.com/xstaar/autocad-mcp) | AutoCAD, YQArch | ⬜ Community | 8 | 🟢 2026-04-12 | MCP server for the YQArch architectural plugin exposing 684 architectural commands through 55 tools (walls, doors, windows, stairs, dimensions, hatching) to Claude. |
| [autocad-mcp-server (vigneshpbmenon)](https://github.com/vigneshpbmenon/autocad-mcp-server) | AutoCAD | ⬜ Community | 6 | 🔴 2025-07-06 | Early FastMCP/pyautocad server for basic AutoCAD drawing primitives (lines, polylines, circles, arcs). |
| [autocad-mcp (piping & pipe supports)](https://github.com/C48H74/autocad-mcp) | AutoCAD, AutoCAD Plant 3D | ⬜ Community | 5 | 🟢 2026-10-05 | MCP server for AutoCAD and Plant 3D with a live COM engine or a headless ezdxf engine; README states 50 tools aimed at piping and pipe-support drawings, live-tested on Plant 3D 2021 only. |
| [AutoCAD-mcp (liqi82)](https://github.com/liqi82/autocad-mcp) | AutoCAD | ⬜ Community | 2 | 🟢 2026-09-10 | COM-based MCP server for 2D AutoCAD drafting (draw, dimension, layers, blocks, mechanical title blocks/BOM); README says 54 commands were verified against a live drawing. |
| [BURAK-BIM](https://github.com/BURAKAFRIDI92/BURAK-BIM) | Revit, AutoCAD, Civil 3D, Navisworks, Inventor, ReCap | ⬜ Community | 2 | 🟢 2026-10-25 | Single MCP connector covering the Autodesk AEC stack (Revit, AutoCAD, Civil 3D, Plant 3D, Navisworks, Inventor, ReCap, Robot) versions 2022-2027 using locally compiled bridges. |
| [CAD-MCP (piexl)](https://github.com/piexl/CAD-MCP) | AutoCAD, GstarCAD, ZWCAD | ⬜ Community | 2 | 🟡 2026-02-01 | Natural-language CAD control server for AutoCAD, GstarCAD and ZWCAD: lines, circles, arcs, polylines, text, hatches, dimensions, layers and DWG saving. |
| [autocad-mcp (dxlary)](https://github.com/dxlary/autocad-mcp) | AutoCAD | ⬜ Community | 1 | 🟢 2026-10-06 | Dependency-light MCP server (standard library plus pywin32) driving a running AutoCAD through COM for office automation, built for the WorkBuddy client. |
| [@lisp MCP Server](https://github.com/atlisp-org/mcp-server) | AutoCAD, ZWCAD, GstarCAD, BricsCAD | ⬜ Community | 0 | 🟢 2026-10-29 | MCP server for @lisp package management that also exposes 340+ tools for AI control of AutoCAD-compatible CAD via COM. |
| [AutoCAD 2027 for Mac MCP (geongyeelee)](https://github.com/geongyeelee/autocad-mcp) | AutoCAD | ⬜ Community | 0 | 🟢 2026-10-29 | Dual-mode MCP server for AutoCAD 2027 on macOS: live GUI mode via a native runtime extension and a headless mode using AcCoreConsole and ezdxf. |
| [AutoCAD-Control-Engineering](https://github.com/gujiu502/AutoCAD-Control-Engineering) | AutoCAD | ⬜ Community | 0 | 🟢 2026-10-03 | MCP host with a native .NET plugin extension for transactional AutoCAD control, plus reusable examples for generating and verifying electrical drawings. |
| [autocad-mcp (bisingwaj)](https://github.com/bisingwaj/autocad-mcp) | AutoCAD | ⬜ Community | 0 | 🟢 2026-09-22 | French-documented AutoCAD MCP server that returns rendered drawing images for self-correction, batches whole plans into one undo step, and includes a cross-platform DXF engine that works without AutoC |
| [autocad-mcp (gabrielbsandim)](https://github.com/gabrielbsandim/autocad-mcp) | AutoCAD, BricsCAD, ZWCAD, GstarCAD | ⬜ Community | 0 | 🟢 2026-10-20 | Local MCP server that connects Claude Desktop to an open AutoCAD (or BricsCAD/ZWCAD/GstarCAD) via COM, or edits DXF/DWG files directly on Mac and AutoCAD LT. |
| [autocad-mcp-pro (IAmWillZero)](https://github.com/IAmWillZero/autocad-mcp-pro) | AutoCAD | ⬜ Community | 0 | 🟢 2026-10-27 | Spanish-language MCP server that controls AutoCAD through COM to draw geometry, create structures and manage layers; derived from an earlier autocad-mcp-server. |
| [autocad-validation-mcp](https://github.com/agtmwebtoon/autocad-validation-mcp) | AutoCAD, AutoCAD LT | ⬜ Community | 0 | 🟢 2026-06-22 | AutoCAD and AutoCAD LT MCP server (LISP file-IPC or headless ezdxf) with a pre-execution geometry/dependency/collision validation layer and P&ID symbol support; derived from other autocad-mcp servers. |
| [bim-cli Claude Code plugin](https://github.com/HelloHowAreYouHaveANiceDay/bim-cli-plugin) | Revit, AutoCAD, SketchUp, Blender | ⬜ Community | 0 | 🟢 2026-10-29 | Claude Code plugin exposing the Windows bim-cli verbs as MCP tools to drive Revit 2024-2027, check PDF drawing sets and look up US site/flood data. |
| [CAD Agent Foundation](https://github.com/capskov/cad-agent-foundation) | AutoCAD | ⬜ Community | 0 | 🟢 2026-10-29 | Native AutoCAD MCP server and CLI for AI agents with bounded operations and write/save verification. |
| [CDT-AutoCAD](https://github.com/SlncTrZ/CDT-AutoCAD) | AutoCAD | ⬜ Community | 0 | 🟢 2026-10-23 | Generic AutoCAD execution provider for MCP clients with state verification and recovery; README states 87 public tools, accepted natively on AutoCAD 2027 and a separate headless DXF lane. |
| [DrawMCP](https://github.com/hj2018118/DrawMCP) | AutoCAD, ZWCAD, FreeCAD | ⬜ Community | 0 | 🟢 2026-10-26 | HTTP MCP server plus AutoCAD, ZWCAD and FreeCAD plugins and a desktop chat GUI to read, draw, edit and export CAD drawings across the three applications. |
| [mcp-autocad-server](https://github.com/chichicaste/mcp-autocad-server) | AutoCAD | ⬜ Community | 0 | 🟡 2025-10-24 | Early AutoCAD MCP server for natural-language drawing, layer management and element search; README warns it is not actively maintained and only basic functionality exists. |
| [multiCAD-MCP-Server (jmcaamanog)](https://github.com/jmcaamanog/multiCAD-mcp-server) | AutoCAD, ZWCAD, BricsCAD | ⬜ Community | 0 | 🟢 2026-10-20 | Spanish-language universal CAD control MCP with headless DXF engine and AECO standards. |
| [speckle-mcp (Daviidro)](https://github.com/Daviidro/speckle-mcp) | Speckle, Revit, Rhino, AutoCAD, Blender | ⬜ Community | 0 | 🟢 2026-08-09 | MCP server to manage Speckle projects, models and versions in natural language and give instructions for sending/receiving via Speckle connectors; repo About says 8 tools. |

## Blender

31 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Tripo MCP (official)](https://github.com/Tripo-Developer/tripo-mcp) | Tripo, Blender | 🟦 Official | 224 | 🔴 2025-04-14 | Official Tripo MCP (alpha) that generates 3D assets from natural language and imports them into Blender; last commit April 2025. |
| [Blender Lab MCP Server (official)](https://www.blender.org/lab/mcp-server/) | Blender | 🟦 Official | – | ⚪ – | Official Blender MCP server and companion add-on that give an LLM a natural-language interface to Blender's Python API, docs and scene; the page warns it runs LLM-generated code with no safeguards. |
| [JANCTION Render](https://github.com/JasmyLab-JANCTION/janction-render) | Blender, glTF, USD | 🟧 Company | 1 | 🟢 2026-10-30 | Cloud GPU render farm for Blender scenes and glTF/FBX/USD/STL files exposed as an MCP server and HTTP API; returns previews, frames or MP4 plus a lighting/framing verdict. |
| [Blender Bridge (hosted)](https://blenderbridge.com/) | Blender | 🟧 Company | – | ⚪ – | MCP bridge (registry-listed, OAuth endpoint https://mcp.blenderbridge.com/mcp) that lets an AI drive Blender on the user's own computer through the Blender Bridge desktop app: the AI writes Blender Python, checks… |
| [WillItBlender](https://willitblender.dev) | Blender | 🟧 Company | – | ⚪ – | Hosted Blender-as-a-service for agents: search a catalog of generated 3D assets, run Blender Python scripts or brief a studio agent, returning ready-to-use 3D models. |
| [Blender MCP (mcp-for-blender)](https://github.com/ahujasid/mcp-for-blender) | Blender | ⬜ Community | 32.8k | 🟢 2026-10-29 | The most-starred community Blender MCP: socket-based addon plus MCP server for prompt-driven modeling, materials, scene control and visual verification (formerly published as blender-mcp). |
| [Blender MCP VXAI](https://github.com/VxASI/blender-mcp-vxai) | Blender | ⬜ Community | 300 | 🔴 2025-03-21 | Blender MCP variant distributed via uvx that lets MCP clients create and modify 3D scenes in Blender from natural language, with a matching add-on. |
| [blenderwright (formerly blend-ai)](https://github.com/HoldMyBeer-gg/blenderwright) | Blender | ⬜ Community | 182 | 🟢 2026-10-28 | Blender MCP server with hundreds of tools across modeling, materials, shader nodes, lighting, rendering, animation, rigging, geometry nodes and more, plus guided workflows and mesh-quality analysis. |
| [blender-open-mcp (dhakalnirajan)](https://github.com/dhakalnirajan/blender-open-mcp) | Blender | ⬜ Community | 121 | 🟢 2026-10-27 | Local-first MCP server controlling a live Blender session through an add-on, with a switchable LLM backend (Ollama, LM Studio, llama.cpp, OpenAI-compatible) and PolyHaven tools. |
| [blender-mcp (pranav-deshmukh)](https://github.com/pranav-deshmukh/blender-mcp) | Blender | ⬜ Community | 98 | 🔴 2025-08-06 | Plug-and-play MCP server that lets an LLM drive Blender in real time via JSON commands over TCP, with full scene and object control. |
| [ifc-bonsai-mcp (Show2Instruct)](https://github.com/Show2Instruct/ifc-bonsai-mcp) | Blender, Bonsai (BlenderBIM), IfcOpenShell, IFC | ⬜ Community | 68 | 🟢 2026-07-10 | Original MCP4IFC research server connecting LLMs to Bonsai in Blender to read, create and edit IFC elements; README says it is superseded by bonsai-mcp but kept for reproducibility. |
| [Bonsai_mcp (JotaDeRodriguez)](https://github.com/JotaDeRodriguez/Bonsai_mcp) | Blender, Bonsai (BlenderBIM), IfcOpenShell, IFC | ⬜ Community | 66 | 🟢 2026-09-06 | Fork of BlenderMCP that adds IFC-specific tools (project info, spatial structure, properties, relationships, quantities) through Bonsai plus Blender code execution. |
| [sandraschi blender-mcp](https://github.com/sandraschi/blender-mcp) | Blender | ⬜ Community | 62 | 🟢 2026-10-29 | Headless-first Blender automation via FastMCP with 41 portmanteau tools (150+ operations) covering batch mesh/VSE/Grease Pencil work and Gaussian splats, plus an optional live viewport bridge. |
| [plateau-creative-mcp](https://github.com/pixelx-jp/plateau-creative-mcp) | Project PLATEAU, glTF, Blender | ⬜ Community | 33 | 🟢 2026-05-31 | MCP server turning Japan Project PLATEAU 3D city data into scene-editing tools and glTF/GLB export, with optional Blender rendering. |
| [djeada blender-mcp-server](https://github.com/djeada/blender-mcp-server) | Blender | ⬜ Community | 32 | 🟢 2026-09-23 | Blender MCP server with 27 tools across 7 namespaces (create objects, materials, render, export, run Python, async jobs) over a localhost add-on. |
| [Blender MCP AI](https://github.com/harveyxiacn/blender-mcp-ai) | Blender | ⬜ Community | 18 | 🟢 2026-10-13 | Independent Blender MCP server whose description claims 380 tools in 56 modules for Cursor, Windsurf and Claude Desktop. |
| [Frugal Blender MCP](https://github.com/mohakmalviya/frugal-blender-mcp) | Blender | ⬜ Community | 15 | 🟢 2026-10-15 | Blender MCP that exposes only four compact tools (discover, execute, inspect...) to minimise context tokens, with permission-gated Python. |
| [bonsai-mcp (Show2Instruct)](https://github.com/Show2Instruct/bonsai-mcp) | Blender, Bonsai (BlenderBIM), IfcOpenShell, IFC | ⬜ Community | 13 | 🟢 2026-08-20 | Local MCP server that bridges MCP clients to a running Blender + Bonsai session to inspect the scene, query the loaded IFC project, capture the viewport and run guarded Python code in Blender. |
| [ageless-h blender-mcp](https://github.com/ageless-h/blender-mcp) | Blender | ⬜ Community | 6 | 🟢 2026-04-19 | Layered Blender MCP (perception, declarative write, imperative write, fallback tools) for deep scene reading and node/animation/mesh editing. |
| [ceeyang blender_mcp](https://github.com/ceeyang/blender_mcp) | Blender | ⬜ Community | 4 | 🟢 2026-09-08 | Local MCP server plus Blender 5.2 extension with 159 typed tools in 17 categories (modeling, materials, lighting, cameras, rendering, UV/baking, rigging). |
| [SoDam Rhino Offline MCP](https://github.com/sodam-ai/SoDam-Rhino-MCP-Codex) | Rhino (.3dm files), Blender | ⬜ Community | 4 | 🟢 2026-09-25 | Local Windows MCP tool that generates and verifies architectural .3dm models from JSON specs without a Rhino licence, with Blender rendering. |
| [blender-mcp (zorak1103)](https://github.com/zorak1103/blender-mcp) | Blender | ⬜ Community | 2 | 🟢 2026-10-20 | MCP server for creating scenes, manipulating objects, assigning materials and configuring shader nodes in Blender, with CI and tagged releases. |
| [ellmos Blender Use MCP](https://github.com/ellmos-ai/ellmos-blender-use-mcp) | Blender | ⬜ Community | 2 | 🟢 2026-10-02 | Local-first MCP server for headless Blender asset QA: runs background scripts and verifies that exported FBX files reimport cleanly; no add-on or TCP port needed. |
| [kleer001 blender-mcp](https://github.com/kleer001/blender-mcp) | Blender | ⬜ Community | 2 | 🟢 2026-06-04 | Blender MCP exposing 175 dedicated typed tools across 25 domains (objects, shader and geometry nodes, rigging, physics, compositing) instead of a catch-all execute-code tool. |
| [ViperMesh for Blender](https://github.com/OpenRootdev/vipermesh-blender) | Blender | ⬜ Community | 2 | 🟢 2026-10-30 | Free open-source Blender MCP server and add-on aimed at fewer tokens, reusable scene-editing tools, persistent sessions and built-in scene checks. |
| [Blender MCP Client for Blender Lab add-on](https://github.com/A-to-PC/blender-lab-mcp-client) | Blender | ⬜ Community | 1 | 🟢 2026-08-17 | Fork of djeada/blender-mcp-server retargeted at the official Blender Lab add-on wire protocol, exposing the same 27 tools. |
| [4dgspl-tools](https://github.com/snmzzcenk/4dgspl-tools) | Blender, COLMAP, 4D Gaussian splatting | ⬜ Community | 0 | 🟢 2026-10-30 | Tools for 4D Gaussian splatting with a stdio MCP server to upload captures to 4dgspl.at and download results; includes a Blender multi-camera rig. |
| [bim-cli Claude Code plugin](https://github.com/HelloHowAreYouHaveANiceDay/bim-cli-plugin) | Revit, AutoCAD, SketchUp, Blender | ⬜ Community | 0 | 🟢 2026-10-29 | Claude Code plugin exposing the Windows bim-cli verbs as MCP tools to drive Revit 2024-2027, check PDF drawing sets and look up US site/flood data. |
| [Blender-MCP (Aayushdubey101)](https://github.com/Aayushdubey101/Blender-MCP) | Blender | ⬜ Community | 0 | 🟢 2026-07-19 | Pydantic-validated, plugin-extensible Blender MCP server with Docker support, CI on Python 3.10-3.12 and a Blender add-on. |
| [BlenderLens](https://github.com/pzalutski-pixel/blenderlens-mcp) | Blender | ⬜ Community | 0 | 🟢 2026-10-12 | Blender MCP that lets an agent model, texture and animate, live in your Blender window or in a background instance, with rendered previews and glTF/.blend export. |
| [speckle-mcp (Daviidro)](https://github.com/Daviidro/speckle-mcp) | Speckle, Revit, Rhino, AutoCAD, Blender | ⬜ Community | 0 | 🟢 2026-08-09 | MCP server to manage Speckle projects, models and versions in natural language and give instructions for sending/receiving via Speckle connectors; repo About says 8 tools. |

## SketchUp

23 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Trimble SketchUp Connector (MCP)](https://news.trimble.com/2026-04-28-Trimble-Links-SketchUp-with-Anthropics-Claude,-Bringing-New-Conversational-AI-powered-Capabilities-to-3D-Modeling) | SketchUp | 🟦 Official | – | 🟢 2026-04-28 | Trimble-hosted remote MCP connector (announced 2026-04-28) that lets Claude build SketchUp (.skp) models in a cloud session from text and images and return a preview and download link. |
| [Hueflow SketchUp MCP](https://github.com/hueflowstudio/hueflow-sketchup-mcp) | SketchUp | 🟧 Company | 7 | 🟢 2026-04-27 | Korean-localised SketchUp MCP server packaged by Hueflow Studio for interior-design and AI teaching. |
| [SketchupMCP (mhyrr)](https://github.com/mhyrr/sketchup-mcp) | SketchUp | ⬜ Community | 521 | 🟢 2026-04-25 | Original community SketchUp MCP server (inspired by Blender MCP) that uses a Ruby extension with a TCP server and a Python MCP server. |
| [sketchup-mcp2](https://github.com/zinin/sketchup-mcp2) | SketchUp | ⬜ Community | 56 | 🟢 2026-10-20 | Actively maintained SketchUp MCP server (PyPI sketchup-mcp2) with typed tools, a Ruby extension and a length-prefixed JSON-RPC protocol. |
| [SketchUp-MCP (BearNetwork)](https://github.com/BearNetwork-BRNKC/SketchUp-MCP) | SketchUp | ⬜ Community | 28 | 🟢 2026-08-07 | Traditional-Chinese localisation and enhancement of mhyrr/sketchup-mcp. |
| [SketchUp MCP Server (Tarkiin)](https://github.com/Tarkiin/SketchUp-MCP) | SketchUp | ⬜ Community | 14 | 🟢 2026-07-29 | Spanish-language SketchUp MCP server (stdio to HTTP :8080) for Claude, Cursor and Gemini to build 3D models programmatically. |
| [vn-sketchup-mcp](https://github.com/andyluu98/vn-sketchup-mcp) | SketchUp | ⬜ Community | 12 | 🟢 2026-09-01 | Vietnamese-localised, patched fork of mhyrr/sketchup-mcp with one-command install for Claude Code, Codex and Antigravity. |
| [Local MCP for SketchUp](https://github.com/dtzhlq/local-mcp-for-sketchup) | SketchUp | ⬜ Community | 11 | 🟢 2026-10-16 | Offline-capable local MCP bridge for reviewed SketchUp modelling; README states 48 tools in v0.4.2. |
| [SketchUp MCP (2ez4gcx)](https://github.com/2ez4gcx/sketchup-mcp) | SketchUp | ⬜ Community | 4 | 🟢 2026-10-21 | SketchUp MCP server with quantity takeoff by tag or material, modelling, materials, screenshots, exports and Ruby execution. |
| [Ringo SketchUp MCP](https://github.com/Ringophilia/Ringo-Sketchup-MCP) | SketchUp | ⬜ Community | 1 | 🟢 2026-10-27 | Chinese-language local bridge for querying and editing SketchUp models with an authenticated, undoable channel. |
| [SketchUp MCP by ArchBench](https://github.com/3d-mcp/sketchup-mcp) | SketchUp | ⬜ Community | 1 | 🟢 2026-09-13 | Independent experimental-alpha SketchUp MCP connector by ArchBench. |
| [sketchup-mcp (piexl)](https://github.com/piexl/sketchup-mcp) | SketchUp | ⬜ Community | 1 | 🟡 2026-01-31 | Fork of the SketchupMCP project connecting SketchUp to Claude. |
| [sketchup-mcp-remote](https://github.com/forceki/sketchup-mcp-remote) | SketchUp | ⬜ Community | 1 | 🟢 2026-10-29 | Fork of mhyrr/sketchup-mcp that can serve MCP over HTTP so a client on another machine can drive SketchUp; the README notes it has no authentication. |
| [bim-cli Claude Code plugin](https://github.com/HelloHowAreYouHaveANiceDay/bim-cli-plugin) | Revit, AutoCAD, SketchUp, Blender | ⬜ Community | 0 | 🟢 2026-10-29 | Claude Code plugin exposing the Windows bim-cli verbs as MCP tools to drive Revit 2024-2027, check PDF drawing sets and look up US site/flood data. |
| [bunnu-sketchup-mcp2](https://github.com/Prasadpodaparthi/bunnu-sketchup-mcp2) | SketchUp | ⬜ Community | 0 | 🟢 2026-09-14 | Copy of the sketchup-mcp2 server and Ruby extension. |
| [CDT-SketchUp](https://github.com/SlncTrZ/CDT-SketchUp) | SketchUp | ⬜ Community | 0 | 🟢 2026-10-23 | Domain-neutral SketchUp MCP provider with typed Python tools dispatching to a Ruby extension; README states 68 public tools. |
| [mcp_sketchup](https://github.com/Atomnaphat/mcp_sketchup) | SketchUp | ⬜ Community | 0 | 🔴 2025-04-25 | Copy of the SketchupMCP README and code for connecting SketchUp to Claude. |
| [SketchUp MCP (lewisyusong)](https://github.com/lewisyusong/sketchup-mcp) | SketchUp | ⬜ Community | 0 | 🟢 2026-10-22 | Chinese-language SketchUp MCP that reads selections, edits geometry, sets materials, exports and runs controlled Ruby over a local TCP plugin (127.0.0.1:9876). |
| [SketchUp MCP untuk Windows](https://github.com/yonnayy/sketchup-mcp-windows) | SketchUp | ⬜ Community | 0 | 🟢 2026-10-01 | Indonesian-language SketchUp MCP for Claude Desktop on Windows that can turn floor plans into walls, openings and slabs. |
| [sketchup-mcp (CyrusStudio fork)](https://github.com/CyrusStudio/sketchup-mcp) | SketchUp | ⬜ Community | 0 | 🟢 2026-09-24 | Maintained fork of mhyrr/sketchup-mcp for creating geometry, applying materials, exporting and running Ruby in SketchUp. |
| [sketchup-mcp (nguyenduyhust)](https://github.com/nguyenduyhust/sketchup-mcp) | SketchUp | ⬜ Community | 0 | 🟢 2026-07-28 | Fork of the SketchupMCP project connecting SketchUp to Claude. |
| [sketchup-mcp (Son-The-SUN)](https://github.com/Son-The-SUN/sketchup-mcp) | SketchUp | ⬜ Community | 0 | 🟢 2026-10-28 | Repository for the same sketchup-mcp2 Python MCP server plus Ruby extension bridge. |
| [Trimble SketchUp MCP Bridge (Aaradhya)](https://github.com/Aaradhya-Dev-Tamrakar/sketchup-mcp) | SketchUp | ⬜ Community | 0 | 🟢 2026-09-20 | MCP bridge for conceptual massing and solar studies in SketchUp from Claude Desktop, Cursor and Antigravity. |

## Rhino

20 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [RhinoAI (McNeel Rhino MCP)](https://github.com/mcneel/RhinoAI) | Rhino, Grasshopper | 🟦 Official | 387 | 🟢 2026-10-29 | Free MIT-licensed plugin and MCP server from McNeel that connects Rhino and Grasshopper to Claude, Copilot, Codex, Gemini or local LLMs to create geometry, run commands, edit scripts and build Grasshopper… |
| [RhinoMCP (REER)](https://github.com/reer-ide/rhino_mcp) | Rhino, Grasshopper | 🟧 Company | 29 | 🟢 2026-04-05 | REER-published open MCP server connecting Rhino (and partial Grasshopper support) to Claude via a socket bridge. |
| [RhinoMCP (jingcheng-chen)](https://github.com/jingcheng-chen/rhinomcp) | Rhino, Grasshopper | ⬜ Community | 1.2k | 🟢 2026-10-16 | Popular community MCP server that models geometry in Rhino 8 and builds Grasshopper definitions through a Rhino plugin and TCP bridge. |
| [rhino-mcp (SerjoschDuering)](https://github.com/SerjoschDuering/rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 65 | 🔴 2025-04-08 | Rhino/Grasshopper MCP server with the same README as the sholtomaud project (socket bridge, optional Replicate rendering). |
| [GH_mcp_server](https://github.com/veoery/GH_mcp_server) | Rhino, Grasshopper | ⬜ Community | 32 | 🔴 2025-04-04 | Early MCP server letting an LLM analyse .3dm files, model in Rhino and generate GHPython in Grasshopper. |
| [LAMCP (LAmbda MCP)](https://github.com/gramaziokohler/lamcp) | Grasshopper, Rhino | ⬜ Community | 22 | 🟢 2026-08-27 | University-originated MCP server for introspecting and mutating a live Grasshopper session: inspect canvas, wire components, set sliders and run RhinoCommon calls. |
| [Rhino Grasshopper MCP (ML auto-layout)](https://github.com/dongwoosuk/rhino-grasshopper-mcp) | Rhino, Grasshopper | ⬜ Community | 17 | 🟢 2026-05-27 | Rhino/Grasshopper MCP server that adds machine-learning-based automatic layout optimisation to live Rhino and Grasshopper control. |
| [GOLEM-3DMCP](https://github.com/TheKingHippopotamus/GOLEM-3DMCP-Rhino-) | Rhino, Grasshopper | ⬜ Community | 14 | 🟢 2026-08-23 | MCP server giving AI agents programmatic control of Rhino 8 for geometry, surfaces, booleans, Grasshopper, viewport capture and script execution. |
| [RhinoMCP (fernandomaytorena)](https://github.com/fernandomaytorena/RhinoMCP) | Rhino | ⬜ Community | 13 | 🔴 2025-03-15 | MCP server connecting Rhino3D to Claude for AI-assisted modelling and analysis. |
| [rhino-mcp (EaseHee)](https://github.com/EaseHee/rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 9 | 🟢 2026-05-20 | MCP server that drives Rhino 8 and Grasshopper from Claude for geometry creation, layers, materials, Grasshopper baking and STEP/IGES/STL/OBJ export. |
| [Rhino MCP (quocvibui)](https://github.com/quocvibui/rhino3d-mcp) | Rhino | ⬜ Community | 6 | 🟡 2026-02-19 | Pure-Python MCP server for Rhino 8 whose README claims 135+ tools for geometry, surfaces, meshes, transformations and booleans. |
| [RhinoMCP (kbangaru-cyber)](https://github.com/kbangaru-cyber/Rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 3 | 🟢 2026-08-24 | MCP server for Rhino 3D with 105 tools (per repo description) for modelling, analysis, diagnostics and Grasshopper integration. |
| [Almond MCP](https://github.com/liangjunglj-cpu/almond-mcp) | Rhino, Karamba | ⬜ Community | 2 | 🟢 2026-10-05 | MCP server for Rhino 8 with a semantic scene layer, curated asset libraries, Karamba capsules and a built-in structural frame solver (pre-release). |
| [Rhino and Grasshopper MCP Bridge (Aaradhya)](https://github.com/Aaradhya-Dev-Tamrakar/rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 1 | 🟢 2026-09-20 | MCP bridge connecting AI assistants such as Claude Desktop, Cursor and Antigravity to Rhino and Grasshopper for parametric architecture. |
| [RhinoMCP (mustafaisildakcom)](https://github.com/mustafaisildakcom/rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 1 | 🔴 2025-04-08 | Blender-MCP-inspired socket bridge letting Claude drive Rhino and Grasshopper, with optional Replicate-based AI rendering of images. |
| [Rhino MCP by ArchBench](https://github.com/3d-mcp/rhino-mcp) | Rhino | ⬜ Community | 0 | 🟢 2026-09-13 | Independent, experimental-alpha Rhino MCP connector by ArchBench for Codex, Claude Code and other MCP clients. |
| [rhino-gh-spatial-mcp](https://github.com/emmaruyiyang/rhino-gh-mcp) | Rhino, Grasshopper | ⬜ Community | 0 | 🟢 2026-08-20 | Layer on top of jingcheng-chen/rhinomcp that reads scenes as a structured spatial graph and computes geometric performance reports. |
| [rhino-mcp (rokibul-mist)](https://github.com/rokibul-mist/rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 0 | 🟢 2026-09-09 | Unified Rhino 8 and Grasshopper MCP server with a native C# bridge plugin; repo description claims 540+ tools. |
| [rhino-mcp (sholtomaud)](https://github.com/sholtomaud/rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 0 | 🔴 2025-04-08 | Socket-based MCP server connecting Rhino and Grasshopper to Claude, with optional AI image rendering via a Replicate API key. |
| [speckle-mcp (Daviidro)](https://github.com/Daviidro/speckle-mcp) | Speckle, Revit, Rhino, AutoCAD, Blender | ⬜ Community | 0 | 🟢 2026-08-09 | MCP server to manage Speckle projects, models and versions in natural language and give instructions for sending/receiving via Speckle connectors; repo About says 8 tools. |

## Fusion

18 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Autodesk Fusion MCP](https://github.com/Autodesk/ai-integrations/tree/main/fusion/local-mcp-server) | Fusion | 🟦 Official | 0 | 🟢 2026-10-29 | Thin stdio bridge (MCPB bundle for Claude Desktop, or direct URL for Cursor) to the MCP server built into the Autodesk Fusion desktop app, for creating, modifying and inspecting geometry in a running Fusion session. |
| [Autodesk Product Help MCP](https://github.com/Autodesk/ai-integrations/tree/main/product-help/remote-mcp-server) | AutoCAD, Revit, Civil 3D, Maya, Fusion, Inventor | 🟦 Official | 0 | 🟢 2026-10-29 | Autodesk-hosted, read-only remote MCP server (Streamable HTTP, no authentication) that searches official Autodesk Help and Support documentation for 110+ products. |
| [Fusion-360-MCP-Server (AuraFriday)](https://github.com/AuraFriday/Fusion-360-MCP-Server) | Fusion | 🟧 Company | 127 | 🟡 2026-01-28 | Fusion add-in (listed on Autodesk App Store) connecting Fusion to the Aura Friday MCP-Link server so AI agents can drive it. |
| [fusion360-mcp-server (faust-machines)](https://github.com/faust-machines/fusion360-mcp-server) | Fusion | ⬜ Community | 138 | 🟢 2026-10-06 | Beta MCP server that forwards commands over TCP to a Fusion 360 add-in for CAD automation; on PyPI. |
| [fusion-mcp-server (Joe-Spencer)](https://github.com/Joe-Spencer/fusion-mcp-server) | Fusion | ⬜ Community | 50 | 🔴 2025-04-22 | Fusion 360 add-in implementing an MCP server with resources, tools and prompts for Claude. |
| [Fusion-MCP-Server (Joelalbon)](https://github.com/Joelalbon/Fusion-MCP-Server) | Fusion | ⬜ Community | 41 | 🔴 2025-06-12 | Client-server remote control for Fusion 360 with a Python MCP server, JSON socket communication and a Fusion add-in; last commit June 2025. |
| [autodesk-fusion-mcp (frankhommers)](https://github.com/frankhommers/autodesk-fusion-mcp) | Fusion | ⬜ Community | 34 | 🟢 2026-09-26 | MCP server that runs inside Fusion as an add-in and serves Streamable HTTP directly, with no external dependencies or bridge process. |
| [fusion-cad-mcp (Mfrostbutter)](https://github.com/Mfrostbutter/fusion-cad-mcp) | Fusion | ⬜ Community | 32 | 🟢 2026-08-18 | Beta MCP server sitting in front of Fusion's built-in MCP, with 75 typed tools for sketches, features, assemblies, joints, measurement and export. |
| [autodesk-fusion-mcp-python (sockcymbal)](https://github.com/sockcymbal/autodesk-fusion-mcp-python) | Fusion | ⬜ Community | 18 | 🔴 2025-05-22 | Demo integration with a LiveCube Fusion script exposing an HTTP endpoint and an intermediary MCP server for parametric cubes. No license file found. |
| [fusion360-mcp-server (mycelia1)](https://github.com/mycelia1/fusion360-mcp-server) | Fusion | ⬜ Community | 6 | 🔴 2025-07-23 | Fusion 360 MCP built on the latest MCP SDK that turns tool calls into Fusion Python scripts; README lists 13+ tools. |
| [fusion-mcp (prim-design)](https://github.com/prim-design/fusion-mcp) | Fusion | ⬜ Community | 4 | 🟡 2026-03-23 | Open-source stdio MCP server with a TCP Fusion 360 add-in; README mentions an execute_python escape hatch. |
| [fusion-mcp (shiguri-01)](https://github.com/shiguri-01/fusion-mcp) | Fusion | ⬜ Community | 4 | 🟢 2026-04-01 | Japanese-documented Fusion MCP with an add-in; exposes Python execution in Fusion, viewport screenshot and user-parameter tools. |
| [Ghost-MCP-Fusion360](https://github.com/thecuriousrohan/Ghost-MCP-Fusion360) | Fusion | ⬜ Community | 2 | 🟢 2026-09-18 | Zero-trust Fusion 360 MCP server requiring native human approval of each session and exposing the Fusion API for CAD generation and visual verification. |
| [Fusion-Native-MCP](https://github.com/Dawn-Of-Justice/Fusion-Native-MCP) | Fusion | ⬜ Community | 1 | 🟢 2026-09-10 | Client for Fusion's native MCP endpoint with 39 tools (README) covering modeling, assemblies, CAM toolpaths and a persistent operation journal; Windows live-tested. |
| [autodesk-cad-mcp-agent](https://github.com/MAvinash24/autodesk-cad-mcp-agent) | Fusion, Inventor, Revit, APS | ⬜ Community | 0 | 🟢 2026-09-09 | FastAPI microservice combining a C++ geometry evaluator with an MCP JSON-RPC interface and a RAG knowledge engine over Autodesk API docs. |
| [fusion-360-mcp-server (perkovicluka)](https://github.com/perkovicluka/fusion-360-mcp-server) | Fusion | ⬜ Community | 0 | 🟡 2025-12-05 | FastMCP server (stdio/HTTP) plus a Fusion Python add-in listening on local TCP to link MCP clients to Fusion 360. |
| [fusion-reconstruct-mcp](https://github.com/ab7646/fusion-reconstruct-mcp) | Fusion | ⬜ Community | 0 | 🟢 2026-08-20 | MCP server and Fusion add-in that rebuilds STL/3MF meshes or reference photos as parametric Fusion features driven by an LLM. |
| [fusion360-mcp (hellstein-dev)](https://github.com/hellstein-dev/fusion360-mcp) | Fusion | ⬜ Community | 0 | 🟢 2026-10-24 | Stdio MCP server plus a token-protected localhost Fusion add-in that runs requests on Fusion's main thread. |

## Grasshopper

18 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [RhinoAI (McNeel Rhino MCP)](https://github.com/mcneel/RhinoAI) | Rhino, Grasshopper | 🟦 Official | 387 | 🟢 2026-10-29 | Free MIT-licensed plugin and MCP server from McNeel that connects Rhino and Grasshopper to Claude, Copilot, Codex, Gemini or local LLMs to create geometry, run commands, edit scripts and build Grasshopper… |
| [RhinoMCP (REER)](https://github.com/reer-ide/rhino_mcp) | Rhino, Grasshopper | 🟧 Company | 29 | 🟢 2026-04-05 | REER-published open MCP server connecting Rhino (and partial Grasshopper support) to Claude via a socket bridge. |
| [RhinoMCP (jingcheng-chen)](https://github.com/jingcheng-chen/rhinomcp) | Rhino, Grasshopper | ⬜ Community | 1.2k | 🟢 2026-10-16 | Popular community MCP server that models geometry in Rhino 8 and builds Grasshopper definitions through a Rhino plugin and TCP bridge. |
| [rhino-mcp (SerjoschDuering)](https://github.com/SerjoschDuering/rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 65 | 🔴 2025-04-08 | Rhino/Grasshopper MCP server with the same README as the sholtomaud project (socket bridge, optional Replicate rendering). |
| [GH_mcp_server](https://github.com/veoery/GH_mcp_server) | Rhino, Grasshopper | ⬜ Community | 32 | 🔴 2025-04-04 | Early MCP server letting an LLM analyse .3dm files, model in Rhino and generate GHPython in Grasshopper. |
| [LAMCP (LAmbda MCP)](https://github.com/gramaziokohler/lamcp) | Grasshopper, Rhino | ⬜ Community | 22 | 🟢 2026-08-27 | University-originated MCP server for introspecting and mutating a live Grasshopper session: inspect canvas, wire components, set sliders and run RhinoCommon calls. |
| [Honeybee-MCP](https://github.com/LoftyTao/Honeybee-MCP) | Honeybee, Ladybug Tools, Grasshopper | ⬜ Community | 17 | 🟡 2026-03-10 | FastMCP server exposing the Ladybug Tools/Honeybee building-energy modeling ecosystem; loads HBJSON or Grasshopper shared-memory models and edits, queries and simulates them. |
| [Rhino Grasshopper MCP (ML auto-layout)](https://github.com/dongwoosuk/rhino-grasshopper-mcp) | Rhino, Grasshopper | ⬜ Community | 17 | 🟢 2026-05-27 | Rhino/Grasshopper MCP server that adds machine-learning-based automatic layout optimisation to live Rhino and Grasshopper control. |
| [GOLEM-3DMCP](https://github.com/TheKingHippopotamus/GOLEM-3DMCP-Rhino-) | Rhino, Grasshopper | ⬜ Community | 14 | 🟢 2026-08-23 | MCP server giving AI agents programmatic control of Rhino 8 for geometry, surfaces, booleans, Grasshopper, viewport capture and script execution. |
| [rhino-mcp (EaseHee)](https://github.com/EaseHee/rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 9 | 🟢 2026-05-20 | MCP server that drives Rhino 8 and Grasshopper from Claude for geometry creation, layers, materials, Grasshopper baking and STEP/IGES/STL/OBJ export. |
| [Rhino/Grasshopper MCP (rhino-gh-mcp)](https://github.com/GenEnv/rhino-gh-mcp) | Rhino 8, Grasshopper | ⬜ Community | 8 | 🟢 2026-07-17 | MCP server plus Rhino and Grasshopper plugins to read and drive a live Rhino 8 session for parametric design and architectural research, with facade-design skills. |
| [Grasshopper MCP workflow](https://github.com/AmemiyaLai/grasshopper-mcp-workflow) | Grasshopper | ⬜ Community | 4 | 🟢 2026-10-05 | Bridging server that links Grasshopper and Cursor over MCP for natural-language control of components. |
| [RhinoMCP (kbangaru-cyber)](https://github.com/kbangaru-cyber/Rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 3 | 🟢 2026-08-24 | MCP server for Rhino 3D with 105 tools (per repo description) for modelling, analysis, diagnostics and Grasshopper integration. |
| [Rhino and Grasshopper MCP Bridge (Aaradhya)](https://github.com/Aaradhya-Dev-Tamrakar/rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 1 | 🟢 2026-09-20 | MCP bridge connecting AI assistants such as Claude Desktop, Cursor and Antigravity to Rhino and Grasshopper for parametric architecture. |
| [RhinoMCP (mustafaisildakcom)](https://github.com/mustafaisildakcom/rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 1 | 🔴 2025-04-08 | Blender-MCP-inspired socket bridge letting Claude drive Rhino and Grasshopper, with optional Replicate-based AI rendering of images. |
| [rhino-gh-spatial-mcp](https://github.com/emmaruyiyang/rhino-gh-mcp) | Rhino, Grasshopper | ⬜ Community | 0 | 🟢 2026-08-20 | Layer on top of jingcheng-chen/rhinomcp that reads scenes as a structured spatial graph and computes geometric performance reports. |
| [rhino-mcp (rokibul-mist)](https://github.com/rokibul-mist/rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 0 | 🟢 2026-09-09 | Unified Rhino 8 and Grasshopper MCP server with a native C# bridge plugin; repo description claims 540+ tools. |
| [rhino-mcp (sholtomaud)](https://github.com/sholtomaud/rhino-mcp) | Rhino, Grasshopper | ⬜ Community | 0 | 🔴 2025-04-08 | Socket-based MCP server connecting Rhino and Grasshopper to Claude, with optional AI image rendering via a Replicate API key. |

## IFC

18 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [IfcMCP (ifcopenshell-mcp)](https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.9.0/src/ifcmcp) | IfcOpenShell, IFC | 🟦 Official | 2.9k | 🟢 2026-09-29 | MCP server in the IfcOpenShell monorepo that wraps ifcquery and ifcedit and keeps an IFC model in memory across calls for querying, validating, clash checking, quantifying and editing. |
| [bim.house MCP](https://bim.house/docs/mcp) | IFC, DXF | 🟧 Company | – | ⚪ – | Hosted streamable-http MCP server for AI agents (e.g. Claude) to search a building-material catalog, create a house (bim.json) with a viewer link, run Japanese building-code (houki) checks, get rough material… |
| [ifc-lite (with MCP server)](https://github.com/LTplus-AG/ifc-lite) | IFC, WebGPU viewer, TypeScript SDK | ⬜ Community | 454 | 🟢 2026-10-30 | IFC toolkit (viewer, SDK, CLI, Rust/WASM core) whose CLI can start an MCP server so agents can query and edit BIM data. |
| [ifc-bonsai-mcp (Show2Instruct)](https://github.com/Show2Instruct/ifc-bonsai-mcp) | Blender, Bonsai (BlenderBIM), IfcOpenShell, IFC | ⬜ Community | 68 | 🟢 2026-07-10 | Original MCP4IFC research server connecting LLMs to Bonsai in Blender to read, create and edit IFC elements; README says it is superseded by bonsai-mcp but kept for reproducibility. |
| [Bonsai_mcp (JotaDeRodriguez)](https://github.com/JotaDeRodriguez/Bonsai_mcp) | Blender, Bonsai (BlenderBIM), IfcOpenShell, IFC | ⬜ Community | 66 | 🟢 2026-09-06 | Fork of BlenderMCP that adds IFC-specific tools (project info, spatial structure, properties, relationships, quantities) through Bonsai plus Blender code execution. |
| [openbim-mcp (Fragment MCP Server)](https://github.com/helenkwok/openbim-mcp) | That Open / web-ifc fragments, IFC | ⬜ Community | 39 | 🔴 2025-09-18 | MCP server that converts IFC files to the fragment format, loads fragments and queries BIM elements by IFC category. |
| [ifcMCP (smartaec)](https://github.com/smartaec/ifcmcp) | IFC, IfcOpenShell | ⬜ Community | 34 | 🔴 2025-06-08 | FastMCP server that lets LLM agents query IFC files through IfcOpenShell (entities, properties, locations, spatial containment, wall openings, space boundaries). |
| [ifc-ids-mcp (IDS MCP Server)](https://github.com/vinnividivicci/ifc-ids-mcp) | IDS, IfcOpenShell (IfcTester), IFC | ⬜ Community | 28 | 🟢 2026-04-06 | MCP server that creates, validates and manages buildingSMART IDS 1.0 files deterministically using IfcOpenShell's IfcTester. |
| [bonsai-mcp (Show2Instruct)](https://github.com/Show2Instruct/bonsai-mcp) | Blender, Bonsai (BlenderBIM), IfcOpenShell, IFC | ⬜ Community | 13 | 🟢 2026-08-20 | Local MCP server that bridges MCP clients to a running Blender + Bonsai session to inspect the scene, query the loaded IFC project, capture the viewport and run guarded Python code in Blender. |
| [IFC MCP (flinker-app)](https://github.com/flinker-app/ifc-mcp) | IFC, IfcOpenShell, BCF | ⬜ Community | 13 | 🟢 2026-09-24 | Local Node MCP server that runs IfcOpenShell in a Pyodide runtime to inspect IFC files, build reports, create simple IFC files, open a local viewer and apply BCF viewpoints. |
| [IFC-MCP (ekkodale)](https://github.com/ekkodale/IFC-MCP) | IFC | ⬜ Community | 10 | 🟡 2025-12-04 | MCP server platform for automated querying and analysis of IFC files, designed for use with OpenWebUI. |
| [ifc-console](https://github.com/nbharathik/ifc-console) | IFC, IfcOpenShell | ⬜ Community | 4 | 🟢 2026-08-12 | Terminal interface that loads IFC models with IfcOpenShell and serves them over MCP so clients can inspect or edit the model, with a local three.js viewer. |
| [bSDD-mcp](https://github.com/JardiMargalefAgusti/bSDD-mcp) | buildingSMART Data Dictionary (bSDD), IFC | ⬜ Community | 3 | 🟡 2026-03-28 | MCP server over the public buildingSMART Data Dictionary API to browse dictionaries, classes, properties and relations for BIM enrichment. |
| [ifc-ruhsat](https://github.com/BerkantACUN/ifc-ruhsat) | IFC, IDS, IfcOpenShell | ⬜ Community | 3 | 🟢 2026-09-24 | CLI and MCP tool that checks building-permit IFC models against Turkiye's digital project regulation (RG 33331) and fills the EK-9 quality-control form. |
| [bim-ifc-mcp](https://github.com/zeussilver/bim-ifc-mcp) | IFC, IfcOpenShell, BCF | ⬜ Community | 0 | 🟢 2026-10-11 | MCP server for deterministic rule checks on IFC models (room areas, door widths, fire doors) with CSV and BCF export. |
| [BimCollab Community MCP](https://github.com/tanguynoumea-collab/BimCollab_Community_MCP) | BIMcollab Zoom, IFC, IfcOpenShell, BCF | ⬜ Community | 0 | 🟢 2026-10-15 | Claude Code toolkit with a bim-assistant MCP server for IFC analysis and a CLI/MCP layer that writes native BIMcollab Zoom files and drives an open Zoom session. |
| [ifc-compliance-mcp](https://github.com/meet-rehman/ifc-compliance-mcp) | IFC, IfcOpenShell, QGIS | ⬜ Community | 0 | 🟢 2026-10-09 | Prototype MCP tool that compares as-built site coverage stored in an IFC file with the site-coverage limit stated by a regulation-answering AI system (Stuttgart case). |
| [ifc-mcp (Amixx)](https://github.com/Amixx/ifc-mcp) | IFC, IfcOpenShell | ⬜ Community | 0 | 🟢 2026-09-18 | MCP server for exploring and querying IFC building models, with relationship tools and dynamic model loading during chat. |

## Civil 3D

15 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Autodesk AutoCAD and Civil 3D MCP Server (Tech Preview)](https://help.autodesk.com/view/ADSKMCP/ENU/) | AutoCAD, Civil 3D | 🟦 Official | – | ⚪ – | Autodesk's local MCP server (Tech Preview / public beta) that runs inside AutoCAD or Civil 3D (AutoCAD 2027 era, Windows) so AI assistants can query, analyze, navigate and modify objects in the open drawing, check… |
| [Autodesk Product Help MCP](https://github.com/Autodesk/ai-integrations/tree/main/product-help/remote-mcp-server) | AutoCAD, Revit, Civil 3D, Maya, Fusion, Inventor | 🟦 Official | 0 | 🟢 2026-10-29 | Autodesk-hosted, read-only remote MCP server (Streamable HTTP, no authentication) that searches official Autodesk Help and Support documentation for 110+ products. |
| [AEC Pilot MCP](https://github.com/hmertkaramann/aec-pilot-mcp) | Revit, AutoCAD, Civil 3D, Navisworks, 3ds Max | 🟧 Company | 2 | 🟢 2026-10-15 | Commercial local MCP server running inside each Autodesk app (Revit, AutoCAD, Civil 3D, Navisworks and more); README states 480+ actions. |
| [Civil3D-mcp (Sacred-G)](https://github.com/Sacred-G/Civil3D-mcp) | Civil 3D | ⬜ Community | 57 | 🟢 2026-08-16 | Node.js MCP server plus native Civil 3D plugin connecting AI clients to a live drawing, with workflow automation for grading, hydrology, plan production and QC; origin of several Civil3D-mcp forks. |
| [Civil 3D MCP (barbosaihan)](https://github.com/barbosaihan/civil3d-mcp) | Civil 3D | ⬜ Community | 46 | 🟢 2026-05-15 | MCP server plus Civil 3D plugin that lets the AI write and execute C# via a Roslyn engine through three meta-tools. |
| [civil3d-mcp (Python COM)](https://github.com/antonhofstader/Civil3D-mcp-python-COM) | Civil 3D | ⬜ Community | 10 | 🟢 2026-04-08 | FastMCP server that drives a running Civil 3D through Windows COM plus pythonnet, with no companion plugin; labelled research and not an Autodesk product. |
| [civil3d-mcp (DaniGhosy)](https://github.com/DaniGhosy/civil3d-mcp-civil3d-mcp) | Civil 3D | ⬜ Community | 3 | 🟢 2026-10-04 | Work-in-progress Civil 3D MCP: TypeScript stdio server talking over TCP/JSON-RPC to a .NET 8 Civil 3D plugin covering surfaces, alignments, points and corridors. |
| [civil3d-mcp-roslyn (nezolder)](https://github.com/nezolder/civil3d-mcp-roslyn) | Civil 3D | ⬜ Community | 3 | 🟢 2026-10-11 | Fork of barbosaihan/civil3d-mcp with a three-tool public surface, a catalog of 37 skills and a focus on reliability and safety. |
| [BURAK-BIM](https://github.com/BURAKAFRIDI92/BURAK-BIM) | Revit, AutoCAD, Civil 3D, Navisworks, Inventor, ReCap | ⬜ Community | 2 | 🟢 2026-10-25 | Single MCP connector covering the Autodesk AEC stack (Revit, AutoCAD, Civil 3D, Plant 3D, Navisworks, Inventor, ReCap, Robot) versions 2022-2027 using locally compiled bridges. |
| [mcp-to-c3d](https://github.com/SantosSjba/mcp-to-c3d) | Civil 3D | ⬜ Community | 2 | 🟢 2026-06-24 | Civil 3D MCP using a code-execution design: a few meta-tools let the AI write C# that runs inside Civil 3D through a Roslyn engine, guided by a skills library. |
| [civil3d-mcp (xuantinhnbs-rgb)](https://github.com/xuantinhnbs-rgb/civil3d-mcp) | Civil 3D | ⬜ Community | 1 | 🟢 2026-09-19 | COM-driven MCP server for Civil 3D that builds TIN surfaces from point clouds, alignments, profiles, corridors and sections. |
| [recap-mcp](https://github.com/xuantinhnbs-rgb/recap-mcp) | ReCap, Civil 3D | ⬜ Community | 1 | 🟢 2026-09-19 | MCP server for Autodesk ReCap: reads .rcp projects, runs the ReCap engine headless, analyses LAS/LAZ and measures deviation between scans and BIM models for Scan-to-BIM. |
| [civil3d-cloud-mcp (msersen)](https://github.com/msersen/civil3d-cloud-mcp) | Civil 3D | ⬜ Community | 0 | 🟡 2026-01-03 | Server side of a Civil 3D MCP integration (Node.js) that needs a separate Civil 3D plugin to create, modify and read objects. |
| [civil3d2021-mcp](https://github.com/orcosto-lab/civil3d2021-mcp) | Civil 3D | ⬜ Community | 0 | 🟢 2026-10-08 | MCP server operating Civil 3D (surfaces, alignments, COGO points, layers, profiles, sections) over COM/pywin32; tested on Civil 3D 2021. |
| [Civil3D_MCP / Autodesk MCP Platform (hjlrosales)](https://github.com/hjlrosales/Civil3D_MCP) | Civil 3D | ⬜ Community | 0 | 🟢 2026-08-09 | TypeScript MCP server and Civil 3D plugin over a Windows named pipe, with tools for alignments, surfaces, corridors, pipe networks and quantity takeoff and transaction-wrapped edits. |

## FreeCAD

15 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [freecad-mcp (neka-nat)](https://github.com/neka-nat/freecad-mcp) | FreeCAD | ⬜ Community | 3.1k | 🟢 2026-10-25 | Most-starred FreeCAD MCP: a FreeCAD addon RPC server plus uvx MCP server to create models, run scripts, inspect documents and run FEM analyses. |
| [FreeCAD Robust MCP Server](https://github.com/spkane/freecad-addon-robust-mcp-server) | FreeCAD | ⬜ Community | 261 | 🟢 2026-10-30 | MCP server plus bridge workbench for AI-assisted FreeCAD modelling, macro and workbench development with several connection modes. |
| [FreeCAD MCP (bonninr)](https://github.com/bonninr/freecad_mcp) | FreeCAD | ⬜ Community | 228 | 🔴 2025-03-20 | Early FreeCAD addon implementing MCP for Claude Desktop and Cursor. |
| [FreeCAD MCP Plugin (ATOI-Ming)](https://github.com/ATOI-Ming/FreeCAD-MCP) | FreeCAD | ⬜ Community | 102 | 🟢 2026-06-17 | FreeCAD plugin with server, GUI control panel and CLI client automating model creation, macro execution and view management for MCP clients like Claude and Cursor. |
| [freecad-mcp (blwfish)](https://github.com/blwfish/freecad-mcp) | FreeCAD | ⬜ Community | 62 | 🟢 2026-10-29 | MCP bridge to FreeCAD for parametric design, CNC toolpath generation and mesh work; repo description says 32 tools. |
| [FreeCAD MCP (sandraschi)](https://github.com/sandraschi/freecad-mcp) | FreeCAD | ⬜ Community | 33 | 🟢 2026-10-29 | FastMCP server for headless FreeCAD document and export operations with CFD extensions. |
| [MCP-FreeCAD](https://github.com/jango-blockchained/mcp-freecad) | FreeCAD | ⬜ Community | 27 | 🟡 2025-11-06 | FreeCAD integration offering multiple connection methods and specialized tool providers, with support for several AI provider models. |
| [freecad-mcp-pro](https://github.com/GadatheGod/freecad-mcp-pro) | FreeCAD | ⬜ Community | 2 | 🟢 2026-07-25 | FreeCAD MCP server for parametric 3D parts, CalculiX FEM analysis, view screenshots, parts library inserts, custom Python and remote connections. |
| [FreeCAD MCP (ahelja)](https://github.com/ahelja/FreeCAD-MCP) | FreeCAD | ⬜ Community | 1 | 🟢 2026-07-31 | MCP server for driving a live FreeCAD desktop session with 3D view screenshots. |
| [FreeCAD_MCP (Cod3Talk3r)](https://github.com/Cod3Talk3r/FreeCAD_MCP) | FreeCAD | ⬜ Community | 1 | 🟢 2026-10-24 | MCP server for creating, inspecting and validating parametric FreeCAD models from an AI coding agent. |
| [yonosoft freecad-mcp](https://github.com/yonosoft/freecad-mcp) | FreeCAD | ⬜ Community | 1 | 🟢 2026-08-30 | Experimental FreeCAD MCP exposing explicit CAD operations (not arbitrary Python) aimed at parametric, constrained and auditable AI-generated models; self-described as unfinished. |
| [DrawMCP](https://github.com/hj2018118/DrawMCP) | AutoCAD, ZWCAD, FreeCAD | ⬜ Community | 0 | 🟢 2026-10-26 | HTTP MCP server plus AutoCAD, ZWCAD and FreeCAD plugins and a desktop chat GUI to read, draw, edit and export CAD drawings across the three applications. |
| [freecad-mcp (Coben-3d)](https://github.com/Coben-3d/freecad-mcp) | FreeCAD | ⬜ Community | 0 | 🟡 2026-02-05 | Basic FreeCAD MCP server that creates primitive solids and exports STEP, STL and OBJ for Claude Desktop. |
| [freecad-mcp (knespii)](https://github.com/knespii/freecad-mcp) | FreeCAD | ⬜ Community | 0 | 🟢 2026-10-29 | MCP server over XML-RPC to a FreeCAD MCPBridge addon. |
| [mcp-freecad (headless)](https://github.com/thalisantunes/mcp-freecad) | FreeCAD | ⬜ Community | 0 | 🟢 2026-10-16 | Headless FreeCAD MCP for model inspection, STEP/STL/3MF/DXF/SVG export and 2D profile extraction. |

## Maya

15 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Autodesk Product Help MCP](https://github.com/Autodesk/ai-integrations/tree/main/product-help/remote-mcp-server) | AutoCAD, Revit, Civil 3D, Maya, Fusion, Inventor | 🟦 Official | 0 | 🟢 2026-10-29 | Autodesk-hosted, read-only remote MCP server (Streamable HTTP, no authentication) that searches official Autodesk Help and Support documentation for 110+ products. |
| [MayaMCP (PatrickPalmer)](https://github.com/PatrickPalmer/MayaMCP) | Maya | ⬜ Community | 117 | 🔴 2025-05-12 | Early-stage Python MCP server for Maya with basic tools such as list_objects_by_type, create_object and get/set_object_attributes. |
| [maya-mcp-server (chadrik)](https://github.com/chadrik/maya-mcp-server) | Maya | ⬜ Community | 42 | 🟢 2026-07-15 | MCP server for Maya with multi-session support and streaming stdout/stderr, installable via uvx. |
| [Maya MCP (GG_MayaMCP)](https://github.com/GimbalGoats/GG_MayaMCP) | Maya | ⬜ Community | 33 | 🟢 2026-07-20 | Local typed MCP server controlling Maya via commandPort (scene, nodes, modeling, shading, skinning, animation, viewport capture); unofficial. Registry description cites 71 tools. |
| [maya-mcp-server (Jeffreytsai1004)](https://github.com/Jeffreytsai1004/maya-mcp-server) | Maya | ⬜ Community | 8 | 🟢 2026-05-01 | MCP server with a Maya plug-in for Claude control of Maya including scene preview. |
| [mcp-for-maya](https://github.com/Xxx91n/mcp-for-maya) | Maya | ⬜ Community | 3 | 🟢 2026-10-30 | MCP server giving agents spatial awareness of Maya scenes (audit, rollback safety, visual loop). |
| [maya-mcp (abrahamADSK)](https://github.com/abrahamADSK/maya-mcp) | Maya | ⬜ Community | 2 | 🟢 2026-10-02 | MCP server for Maya with RAG documentation search and safety checks; README states 17 tools plus an optional Vision3D image-to-3D add-on. |
| [maya-mcp (science-animated)](https://github.com/science-animated/maya-mcp) | Maya | ⬜ Community | 2 | 🟢 2026-10-18 | MCP server that sends Python expressions to Maya's built-in commandPort on TCP 9877, needing no plugin. |
| [Autodesk-Maya-MCP](https://github.com/AYDJI/Autodesk-Maya-MCP) | Maya | ⬜ Community | 1 | 🟡 2026-02-13 | Maya MCP server with 30+ tools using Maya's built-in command port, needing no separate plugin. |
| [maya-mcp (Sarielyj)](https://github.com/Sarielyj/maya-mcp) | Maya | ⬜ Community | 1 | 🟢 2026-09-12 | Hybrid Maya MCP with semantic scene/material/animation/render tools, execute_python/execute_mel escape hatches and read-only resources; stdio or Streamable HTTP. |
| [MayaMCP (dcoes)](https://github.com/dcoes/MayaMCP) | Maya | ⬜ Community | 1 | 🔴 2025-05-12 | Minimal early-stage Maya MCP server (v0.2.0) for Claude Desktop, tested on Maya 2023 and 2025; last commit May 2025. |
| [automaya-mcp](https://github.com/CallMeParams/automaya-mcp) | Maya | ⬜ Community | 0 | 🟢 2026-09-24 | Maya 2024 MCP with 258 typed tools per README, an in-Maya console, asset libraries, AI 3D generation and a change stream for driving Unreal. |
| [maya-mcp (wang1510583)](https://github.com/wang1510583/maya-mcp) | Maya | ⬜ Community | 0 | 🟢 2026-10-29 | Chinese-language MCP bridge for Maya based on the Maya Agent 1.3.1 extension, with 10 direct tools, a 120-tool registry and custom body rigging. |
| [maya-mcp (YomenStyle)](https://github.com/YomenStyle/maya-mcp) | Maya | ⬜ Community | 0 | 🟢 2026-08-04 | Maya 2022+ MCP built around arbitrary Python execution, self-exploration and viewport capture, split into a PC-side server and a stdlib-only in-Maya bridge, with Unreal pipeline helpers. |
| [MayaMCP (isuzu-shiranui)](https://github.com/isuzu-shiranui/MayaMCP) | Maya | ⬜ Community | 0 | 🟢 2026-09-15 | Maya serves MCP itself over Streamable HTTP with only execute_python and execute_mel tools, plus a NativeAOT command-line client. |

## DXF

14 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Aspicio](https://github.com/frontsail-ai/aspicio) | DXF, vector PDF | 🟧 Company | 6 | 🟢 2026-10-23 | TypeScript DXF/vector-PDF viewer and engine usable by AI agents. |
| [CADaddy](https://github.com/AICodeForgedev/cadaddy) | DWG, DXF | 🟧 Company | 2 | 🟢 2026-10-21 | Free Rust 2D CAD app that opens and saves DWG/DXF and exposes an MCP interface for AI agents; source-available (FSL-1.1). |
| [cadlens-mcp](https://github.com/cadlens-co/cadlens-mcp) | DWG, DXF, DWF, Cadlens API | 🟧 Company | 1 | 🟢 2026-08-11 | MCP wrapper for the hosted Cadlens CAD parsing API that converts DWG/DXF/DWF drawings into structured JSON for agents. |
| [AI Architectures MCP](https://plans.ai-architectures.com/ai-assistants) | DXF, DWG, IFC (house plans) | 🟧 Company | – | ⚪ – | Remote MCP server to search free house plans and have AI-drafted CAD floor plans (DXF/DWG/PDF) created and changed. |
| [bim.house MCP](https://bim.house/docs/mcp) | IFC, DXF | 🟧 Company | – | ⚪ – | Hosted streamable-http MCP server for AI agents (e.g. Claude) to search a building-material catalog, create a house (bim.json) with a viewer link, run Japanese building-code (houki) checks, get rough material… |
| [Land Takeoffs MCP](https://github.com/landtakeoffs/land-takeoffs-mcp) | Civil plan sets, DWG, DXF, LandXML | 🟧 Company | 0 | 🟢 2026-10-16 | Hosted remote MCP that returns sitework quantities (storm, sewer, water, paving, cut/fill) from civil plan-set PDFs and CAD files with an Excel bid sheet. |
| [Skopia floor-plan layout](https://github.com/Skopia-mcp/Skopia-mcp) | DXF, AutoCAD, Revit | 🟧 Company | 0 | 🟢 2026-09-18 | Hosted MCP engine that draws a floor plan in real millimetres and projects consistent sections and elevations, exporting SVG, sheets or DXF. |
| [DWG MCP Server](https://github.com/dimitrovakulenko/dwg-mcp-server) | DWG, DXF | ⬜ Community | 21 | 🟢 2026-10-22 | Read-oriented DWG/DXF access for AI clients; source files stay read-only. |
| [QCAD MCP](https://github.com/sandraschi/qcad-mcp) | QCAD, DXF, DWG | ⬜ Community | 18 | 🟢 2026-10-24 | FastMCP server for 2D CAD automation: DXF/DWG parsing, 3D extrusion, room analysis; README says 12 MCP tools. |
| [AIBlueprint MCP](https://github.com/thebossnow/aiblueprint-mcp) | DXF, LibreCAD | ⬜ Community | 14 | 🟢 2026-10-24 | Headless DXF generation via ezdxf with LibreCAD preview for site plans and architectural drafting. |
| [ZWCAD-MCP (dalingo81)](https://github.com/dalingo81/ZWCAD-MCP) | ZWCAD, DXF | ⬜ Community | 4 | 🟢 2026-07-24 | ZWCAD MCP server adapted from puran-water/autocad-mcp with a File-IPC AutoLISP backend and a headless ezdxf backend that runs without CAD on any OS. |
| [Codemod3 CAD-MCP](https://github.com/Codemod3/CAD-MCP) | DXF, DWG, ezdxf, ODA File Converter | ⬜ Community | 1 | 🟢 2026-08-12 | Local MCP server that reads, analyses and edits DXF and DWG files with ezdxf (DWG via ODA File Converter) for drawing extraction. |
| [dxf-cad-mcp](https://github.com/xhj-cloud/dxf-cad-mcp) | DXF | ⬜ Community | 0 | 🟢 2026-10-26 | Lightweight DXF MCP that creates, inspects and exports 2D drawings (PNG/PDF) without a CAD GUI. |
| [dxf-mcp](https://github.com/OmniZenRaj/dxf-mcp) | DXF | ⬜ Community | 0 | 🟢 2026-09-06 | Read-only MCP for DXF drawings: layer inventory, block-attribute BOM and drafting-standard checks. |

## Navisworks

14 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [NavisCoord](https://github.com/HorizunGroup/naviscoord-mcp) | Navisworks | 🟧 Company | 20 | 🟢 2026-10-20 | Open-source MCP server and Navisworks add-in for clash coordination that works with ChatGPT Desktop, Claude Desktop, Claude Code and Codex. |
| [ScanBIM MCP (AI Hub for AEC)](https://github.com/ScanBIM-Labs/scanbim-mcp) | Revit, Navisworks, Autodesk Construction Cloud, Autodesk Platform Services, Twinmotion | 🟧 Company | 6 | 🟢 2026-04-21 | Hosted Cloudflare Workers hub of MCP servers for AEC; README describes 46 tools across 5 workers covering model upload/viewing, clashes, ACC, Revit, XR and RFIs. |
| [AEC Pilot MCP](https://github.com/hmertkaramann/aec-pilot-mcp) | Revit, AutoCAD, Civil 3D, Navisworks, 3ds Max | 🟧 Company | 2 | 🟢 2026-10-15 | Commercial local MCP server running inside each Autodesk app (Revit, AutoCAD, Civil 3D, Navisworks and more); README states 480+ actions. |
| [Navisworks MCP (ScanBIM Labs)](https://github.com/ScanBIM-Labs/navisworks-mcp) | Navisworks, Autodesk Platform Services | 🟧 Company | 0 | 🟢 2026-04-21 | MCP worker for multi-file coordination, clash detection and viewpoints via APS (repo About text). |
| [Navisworks_MCP (Aitology)](https://github.com/Aitology/Navisworks_MCP) | Navisworks | ⬜ Community | 17 | 🟢 2026-05-13 | Two-part bridge (.NET add-in with local HTTP server plus Python MCP server) for clash detection, clash grouping, selection/search sets, viewpoints and color overrides; README cites 30+ operations. |
| [MCP-Add-in Navisworks Manage 2026 (PoC)](https://github.com/kikki/MCP-Add-in-Autodesk_Navisworks_Manage_2026) | Navisworks | ⬜ Community | 16 | 🔴 2025-09-22 | Proof-of-concept MCP add-in evaluating how an MCP interface can be built for Navisworks Manage 2026, demonstrated with Claude; basis for later Navisworks forks. |
| [NavisworksMCP (shuotao)](https://github.com/shuotao/NAVISWORK_MCP) | Navisworks | ⬜ Community | 8 | 🟡 2026-03-26 | Node.js MCP server with a C# Navisworks add-in (WebSocket port 2233) letting Claude, Gemini and Copilot control Navisworks. |
| [nwd-mcp](https://github.com/bimwright/nwd-mcp) | Navisworks | ⬜ Community | 8 | 🟢 2026-10-10 | MCP gateway for Navisworks Manage 2022-2027 to query, inspect, navigate and script desktop sessions via a .NET 8 server and in-process plugin; Freedom/Simulate unsupported. |
| [BURAK-BIM](https://github.com/BURAKAFRIDI92/BURAK-BIM) | Revit, AutoCAD, Civil 3D, Navisworks, Inventor, ReCap | ⬜ Community | 2 | 🟢 2026-10-25 | Single MCP connector covering the Autodesk AEC stack (Revit, AutoCAD, Civil 3D, Plant 3D, Navisworks, Inventor, ReCap, Robot) versions 2022-2027 using locally compiled bridges. |
| [navisworks-mcp (xuantinhnbs-rgb)](https://github.com/xuantinhnbs-rgb/navisworks-mcp) | Navisworks | ⬜ Community | 1 | 🟢 2026-09-10 | Python MCP server driving a running Navisworks via COM: browse model tree, read IFC/Revit properties, search, select, colour, hide, isolate, zoom and capture the window. |
| [automatizacion-mcp-navisworks](https://github.com/Joseadobbato13/automatizacion-mcp-navisworks) | Navisworks | ⬜ Community | 0 | 🟢 2026-10-24 | Spanish-language MCP server and C# plugin controlling Navisworks Manage 2025/2026: federated-model inspection, search, selection sets, clash detection and 4D TimeLiner planning. |
| [Navisworks MCP (AECO MCPs)](https://aecomcps.com/navisworks) | Navisworks | ⬜ Community | – | ⚪ – | Free plug-in for Navisworks Manage: model tree and properties, sets/viewpoints, Clash Detective tests, coordination QA reports, TimeLiner/quantities and NWD/DWF exports. |
| [navisworks-mcp (dismas5)](https://github.com/dismas5/navisworks-mcp) | Navisworks | ⬜ Community | 0 | 🟢 2026-10-26 | Independent MCP server and Navisworks 2025 plug-in with a 95-tool compatibility catalog; README notes tests pass but live Autodesk behavior is not fully verified. |
| [navisworks-viewpoints-mcp (nw-exchange)](https://github.com/mikhalchankasm/navisworks-viewpoints-mcp) | Navisworks | ⬜ Community | 0 | 🟢 2026-06-04 | File-based MCP server for Navisworks viewpoint XML: merge, move, sync lists and audit; installable with uvx. |

## IfcOpenShell

12 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [IfcMCP (ifcopenshell-mcp)](https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.9.0/src/ifcmcp) | IfcOpenShell, IFC | 🟦 Official | 2.9k | 🟢 2026-09-29 | MCP server in the IfcOpenShell monorepo that wraps ifcquery and ifcedit and keeps an IFC model in memory across calls for querying, validating, clash checking, quantifying and editing. |
| [ifc-bonsai-mcp (Show2Instruct)](https://github.com/Show2Instruct/ifc-bonsai-mcp) | Blender, Bonsai (BlenderBIM), IfcOpenShell, IFC | ⬜ Community | 68 | 🟢 2026-07-10 | Original MCP4IFC research server connecting LLMs to Bonsai in Blender to read, create and edit IFC elements; README says it is superseded by bonsai-mcp but kept for reproducibility. |
| [Bonsai_mcp (JotaDeRodriguez)](https://github.com/JotaDeRodriguez/Bonsai_mcp) | Blender, Bonsai (BlenderBIM), IfcOpenShell, IFC | ⬜ Community | 66 | 🟢 2026-09-06 | Fork of BlenderMCP that adds IFC-specific tools (project info, spatial structure, properties, relationships, quantities) through Bonsai plus Blender code execution. |
| [ifcMCP (smartaec)](https://github.com/smartaec/ifcmcp) | IFC, IfcOpenShell | ⬜ Community | 34 | 🔴 2025-06-08 | FastMCP server that lets LLM agents query IFC files through IfcOpenShell (entities, properties, locations, spatial containment, wall openings, space boundaries). |
| [bonsai-mcp (Show2Instruct)](https://github.com/Show2Instruct/bonsai-mcp) | Blender, Bonsai (BlenderBIM), IfcOpenShell, IFC | ⬜ Community | 13 | 🟢 2026-08-20 | Local MCP server that bridges MCP clients to a running Blender + Bonsai session to inspect the scene, query the loaded IFC project, capture the viewport and run guarded Python code in Blender. |
| [IFC MCP (flinker-app)](https://github.com/flinker-app/ifc-mcp) | IFC, IfcOpenShell, BCF | ⬜ Community | 13 | 🟢 2026-09-24 | Local Node MCP server that runs IfcOpenShell in a Pyodide runtime to inspect IFC files, build reports, create simple IFC files, open a local viewer and apply BCF viewpoints. |
| [ifc-console](https://github.com/nbharathik/ifc-console) | IFC, IfcOpenShell | ⬜ Community | 4 | 🟢 2026-08-12 | Terminal interface that loads IFC models with IfcOpenShell and serves them over MCP so clients can inspect or edit the model, with a local three.js viewer. |
| [ifc-ruhsat](https://github.com/BerkantACUN/ifc-ruhsat) | IFC, IDS, IfcOpenShell | ⬜ Community | 3 | 🟢 2026-09-24 | CLI and MCP tool that checks building-permit IFC models against Turkiye's digital project regulation (RG 33331) and fills the EK-9 quality-control form. |
| [bim-ifc-mcp](https://github.com/zeussilver/bim-ifc-mcp) | IFC, IfcOpenShell, BCF | ⬜ Community | 0 | 🟢 2026-10-11 | MCP server for deterministic rule checks on IFC models (room areas, door widths, fire doors) with CSV and BCF export. |
| [BimCollab Community MCP](https://github.com/tanguynoumea-collab/BimCollab_Community_MCP) | BIMcollab Zoom, IFC, IfcOpenShell, BCF | ⬜ Community | 0 | 🟢 2026-10-15 | Claude Code toolkit with a bim-assistant MCP server for IFC analysis and a CLI/MCP layer that writes native BIMcollab Zoom files and drives an open Zoom session. |
| [ifc-compliance-mcp](https://github.com/meet-rehman/ifc-compliance-mcp) | IFC, IfcOpenShell, QGIS | ⬜ Community | 0 | 🟢 2026-10-09 | Prototype MCP tool that compares as-built site coverage stored in an IFC file with the site-coverage limit stated by a regulation-answering AI system (Stuttgart case). |
| [ifc-mcp (Amixx)](https://github.com/Amixx/ifc-mcp) | IFC, IfcOpenShell | ⬜ Community | 0 | 🟢 2026-09-18 | MCP server for exploring and querying IFC building models, with relationship tools and dynamic model loading during chat. |

## ZWCAD

12 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [CAD-MCP (daobataotie)](https://github.com/daobataotie/CAD-MCP) | AutoCAD, GstarCAD, ZWCAD | ⬜ Community | 654 | 🟢 2026-10-27 | MCP server controlling AutoCAD and other CAD programs through natural language; v2.0 README states 35 tools covering query, editing, layers, blocks and command passthrough. |
| [multiCAD-mcp](https://github.com/AnCode666/multiCAD-mcp) | AutoCAD, ZWCAD | ⬜ Community | 151 | 🟢 2026-06-27 | FastMCP-based server to control AutoCAD and other CAD programs from Claude Desktop or Cursor. |
| [ZWCAD-MCP (dalingo81)](https://github.com/dalingo81/ZWCAD-MCP) | ZWCAD, DXF | ⬜ Community | 4 | 🟢 2026-07-24 | ZWCAD MCP server adapted from puran-water/autocad-mcp with a File-IPC AutoLISP backend and a headless ezdxf backend that runs without CAD on any OS. |
| [CAD-MCP (piexl)](https://github.com/piexl/CAD-MCP) | AutoCAD, GstarCAD, ZWCAD | ⬜ Community | 2 | 🟡 2026-02-01 | Natural-language CAD control server for AutoCAD, GstarCAD and ZWCAD: lines, circles, arcs, polylines, text, hatches, dimensions, layers and DWG saving. |
| [ZWCAD MCP KR](https://github.com/gkdlwmzkdls-sys/zwcad-mcp-kr) | ZWCAD | ⬜ Community | 1 | 🟢 2026-09-23 | Fork of dalingo81/ZWCAD-MCP for Korean Windows, installable as a Claude Code plugin, to read and edit ZWCAD drawings (layers, entities, text, lines, blocks). |
| [@lisp MCP Server](https://github.com/atlisp-org/mcp-server) | AutoCAD, ZWCAD, GstarCAD, BricsCAD | ⬜ Community | 0 | 🟢 2026-10-29 | MCP server for @lisp package management that also exposes 340+ tools for AI control of AutoCAD-compatible CAD via COM. |
| [autocad-mcp (gabrielbsandim)](https://github.com/gabrielbsandim/autocad-mcp) | AutoCAD, BricsCAD, ZWCAD, GstarCAD | ⬜ Community | 0 | 🟢 2026-10-20 | Local MCP server that connects Claude Desktop to an open AutoCAD (or BricsCAD/ZWCAD/GstarCAD) via COM, or edits DXF/DWG files directly on Mac and AutoCAD LT. |
| [DrawMCP](https://github.com/hj2018118/DrawMCP) | AutoCAD, ZWCAD, FreeCAD | ⬜ Community | 0 | 🟢 2026-10-26 | HTTP MCP server plus AutoCAD, ZWCAD and FreeCAD plugins and a desktop chat GUI to read, draw, edit and export CAD drawings across the three applications. |
| [kenchiku-mcp](https://github.com/Sora-bluesky/kenchiku-mcp) | ZWCAD | ⬜ Community | 0 | 🟢 2026-04-13 | Architectural-workflow fork of multiCAD-mcp for ZWCAD that adds non-uniform block scaling (for example door and window blocks) and stderr-safe logging. |
| [multiCAD-MCP-Server (jmcaamanog)](https://github.com/jmcaamanog/multiCAD-mcp-server) | AutoCAD, ZWCAD, BricsCAD | ⬜ Community | 0 | 🟢 2026-10-20 | Spanish-language universal CAD control MCP with headless DXF engine and AECO standards. |
| [ZWCAD MCP (yanyoo2000)](https://github.com/yanyoo2000/ZWCAD-MCP) | ZWCAD, ZWCAD Mechanical | ⬜ Community | 0 | 🟢 2026-10-30 | MCP service driving ZWCAD and ZWCAD Mechanical through Windows COM via a Node launcher; README states 40 tools covering drawing, annotation, layers, title blocks and BOM. |
| [ZWCAD MCP Server (Jerri-Z)](https://github.com/Jerri-Z/ZWCAD-MCP) | ZWCAD, ZWCAD Mechanical | ⬜ Community | 0 | 🟢 2026-09-09 | ZWCAD automation MCP server with 26 platform tools plus ZWCAD Mechanical tools for drawing, dimensions, layers, blocks and document management. |

## Autodesk Construction Cloud

11 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [APS MCP Server (aps-mcp-server-nodejs)](https://github.com/autodesk-platform-services/aps-mcp-server-nodejs) | Autodesk Construction Cloud, Autodesk Platform Services | 🟦 Official | 25 | 🟢 2026-05-07 | Sample MCP server from Autodesk Platform Services that gives AI clients access to ACC project data through the Data Management and ACC APIs, authenticated with Secure Service Accounts. |
| [aps-mcp-app-example](https://github.com/autodesk-platform-services/aps-mcp-app-example) | Autodesk Construction Cloud, APS Viewer, MCP Apps | 🟦 Official | 21 | 🟢 2026-04-21 | Example MCP server with MCP Apps support that browses ACC projects and designs and shows an interactive APS Viewer preview; a live demo is hosted by Autodesk. |
| [aps-mcp-auth-examples](https://github.com/autodesk-platform-services/aps-mcp-auth-examples) | APS, Autodesk Construction Cloud | 🟦 Official | 9 | 🟢 2026-09-25 | Reference MCP servers for Autodesk Platform Services showing 2LO, 3LO, PKCE and Secure Service Account auth, with STDIO or HTTP client authentication targeting the 2026-07-28 MCP spec. |
| [ScanBIM MCP (AI Hub for AEC)](https://github.com/ScanBIM-Labs/scanbim-mcp) | Revit, Navisworks, Autodesk Construction Cloud, Autodesk Platform Services, Twinmotion | 🟧 Company | 6 | 🟢 2026-04-21 | Hosted Cloudflare Workers hub of MCP servers for AEC; README describes 46 tools across 5 workers covering model upload/viewing, clashes, ACC, Revit, XR and RFIs. |
| [ACC MCP (ScanBIM Labs)](https://github.com/ScanBIM-Labs/acc-mcp) | Autodesk Construction Cloud, BIM 360 | 🟧 Company | 0 | 🟢 2026-04-21 | Hosted MCP worker for Autodesk Construction Cloud issues, RFIs and document search via APS (9 tools). |
| [Contech-AI](https://github.com/entech-labs/Contech-AI) | Autodesk Construction Cloud | 🟧 Company | 0 | 🟢 2026-09-25 | Read-only Claude Desktop connector (local acc_mcp.py) that answers questions about ACC RFIs, issues, submittals, cost, members and documents using the user's Autodesk login. |
| [aps-mcp-server (petrbroz, moved)](https://github.com/petrbroz/aps-mcp-server) | Autodesk Construction Cloud, BIM 360 | ⬜ Community | 41 | 🟡 2025-10-29 | Earlier experimental APS MCP server using Secure Service Accounts; README says the project moved to autodesk-platform-services/aps-mcp-server-nodejs. |
| [autodesk-forma-mcp-apac-trial](https://github.com/yueyinglong-cmd/autodesk-forma-mcp-apac-trial) | Autodesk Construction Cloud, Autodesk Forma | ⬜ Community | 4 | 🟢 2026-04-26 | MCP server for Claude Code against ACC/Forma APIs; README states 408 tools across 22 modules (issues, RFIs, submittals, cost, sheets, takeoff and more). |
| [Unofficial Autodesk Forma Remote MCP Server](https://github.com/yueyinglong-cmd/unofficial-autodesk-forma-remote-mcp-server) | Autodesk Construction Cloud, Forma | ⬜ Community | 2 | 🟢 2026-08-11 | Self-hosted multi-user remote MCP server exposing 413 ACC/Forma API tools with per-user Autodesk OAuth; README states it is not an Autodesk product. |
| [APS-ACC-MCP-server (pranjalbishtadsk)](https://github.com/pranjalbishtadsk/APS-ACC-MCP-server) | Autodesk Construction Cloud | ⬜ Community | 1 | 🟡 2026-01-14 | Derivative of the Autodesk sample server that lets assistants query ACC projects, browse files and analyze issues. |
| [forma-mcp](https://github.com/nhantruong96/forma-mcp) | Autodesk Construction Cloud, Autodesk Forma | ⬜ Community | 1 | 🟢 2026-10-22 | MCP server for managing an ISO 19650 / TCVN 14177 Common Data Environment on ACC: projects, folder trees, permissions, files, naming compliance and the Content Catalog; formerly acc-mcp. |

## 3ds Max

10 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [AEC Pilot MCP](https://github.com/hmertkaramann/aec-pilot-mcp) | Revit, AutoCAD, Civil 3D, Navisworks, 3ds Max | 🟧 Company | 2 | 🟢 2026-10-15 | Commercial local MCP server running inside each Autodesk app (Revit, AutoCAD, Civil 3D, Navisworks and more); README states 480+ actions. |
| [3dsmax-mcp (cl0nazepamm)](https://github.com/cl0nazepamm/3dsmax-mcp) | 3ds Max | ⬜ Community | 352 | 🟢 2026-10-21 | MCP server with a native bridge for 3ds Max; README states 161 tools for scene reads, modeling, materials, modifiers, controllers, viewport capture and procedural graphs. |
| [3dsMaxMCP (317431629)](https://github.com/317431629/3dsMaxMCP) | 3ds Max | ⬜ Community | 18 | 🟡 2026-03-12 | Chinese-language MCP server bridging Claude Desktop/Cursor to 3ds Max over a TCP socket listener script. |
| [dcc-mcp-3dsmax](https://github.com/dcc-mcp/dcc-mcp-3dsmax) | 3ds Max | ⬜ Community | 9 | 🟢 2026-10-29 | 3ds Max adapter in the DCC-MCP ecosystem (48 host adapters), with a host-side bridge and sidecar support. |
| [Codex_MCP_3DSMAX](https://github.com/Zhangyoupeng1996/Codex_MCP_3DSMAX) | 3ds Max | ⬜ Community | 1 | 🟢 2026-06-01 | 3ds Max MCP with installer for Cursor, Claude, Codex and Gemini; README states 115 tools (79 in the core profile) and a native bridge for 2023-2027. |
| [3dsmax-mcp (Geddart)](https://github.com/Geddart/3dsmax-mcp) | 3ds Max | ⬜ Community | 0 | 🟢 2026-04-17 | Fork of cl0nazepamm/3dsmax-mcp adding a native C++ GUP-plugin bridge (76 handlers per README), multi-view capture and controller/wiring tools. |
| [3dsmax-mcp (vino3dx)](https://github.com/vino3dx/3dsmax-mcp) | 3ds Max | ⬜ Community | 0 | 🟢 2026-10-20 | Chinese-language stdlib-only Python MCP server for 3ds Max over local TCP and MAXScript; README states 384 tools. |
| [3dsmax-mcp-LxX](https://github.com/LxXStudio2025/3dsmax-mcp-LxX) | 3ds Max | ⬜ Community | 0 | 🟢 2026-10-29 | MCP server plus CLI for a running 3ds Max (2016 onward, tested on 2016 and 2025) using a pure-MAXScript bridge with no pymxs or PySide dependency. |
| [max-mcp (Kafkavari)](https://github.com/Kafkavari/max-mcp) | 3ds Max | ⬜ Community | 0 | 🟢 2026-10-27 | MCP server for a live 3ds Max session where every request is logged, each scene change is a named undo record and the AI can undo only its own steps; runs MAXScript or pymxs. |
| [MAX_MCP](https://github.com/sinushawa/MAX_MCP) | 3ds Max | ⬜ Community | 0 | 🟢 2026-09-12 | Personal fork of cl0nazepamm/3dsmax-mcp adding a per-module tool filter with an in-Max settings window, a MAXScript docs search tool and a V-Ray 7 reference. |

## Inventor

10 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Autodesk Product Help MCP](https://github.com/Autodesk/ai-integrations/tree/main/product-help/remote-mcp-server) | AutoCAD, Revit, Civil 3D, Maya, Fusion, Inventor | 🟦 Official | 0 | 🟢 2026-10-29 | Autodesk-hosted, read-only remote MCP server (Streamable HTTP, no authentication) that searches official Autodesk Help and Support documentation for 110+ products. |
| [inventor-mcp (NeonGlay)](https://github.com/NeonGlay/inventor-mcp) | Inventor | ⬜ Community | 50 | 🟢 2026-06-10 | MCP server wrapping Inventor's COM API with millimeter-based high-level tools for parametric parts and sheet metal; original of the cenitu continuation, no activity since June 2026. |
| [ipt-mcp](https://github.com/bimwright/ipt-mcp) | Inventor | ⬜ Community | 17 | 🟢 2026-10-05 | Apache-2.0 MCP gateway for Inventor 2022-2027 covering parts, sketches, features, parameters, iProperties and export via a per-version in-process add-in. |
| [inventor-mcp (hsavas)](https://github.com/hsavas/inventor-mcp) | Inventor | ⬜ Community | 7 | 🟢 2026-10-20 | COM-automation MCP server for Inventor covering sketches, part features, assemblies, drawings and document control. |
| [BURAK-BIM](https://github.com/BURAKAFRIDI92/BURAK-BIM) | Revit, AutoCAD, Civil 3D, Navisworks, Inventor, ReCap | ⬜ Community | 2 | 🟢 2026-10-25 | Single MCP connector covering the Autodesk AEC stack (Revit, AutoCAD, Civil 3D, Plant 3D, Navisworks, Inventor, ReCap, Robot) versions 2022-2027 using locally compiled bridges. |
| [autodesk-cad-mcp-agent](https://github.com/MAvinash24/autodesk-cad-mcp-agent) | Fusion, Inventor, Revit, APS | ⬜ Community | 0 | 🟢 2026-09-09 | FastAPI microservice combining a C++ geometry evaluator with an MCP JSON-RPC interface and a RAG knowledge engine over Autodesk API docs. |
| [autodesk-inventor-mcp (xtylerai2026-oss)](https://github.com/xtylerai2026-oss/autodesk-inventor-mcp) | Inventor | ⬜ Community | 0 | 🟢 2026-08-06 | Alpha MCP server for parametric part modeling, assemblies and inspection in Inventor, developed against Inventor 2027. |
| [inventor-mcp](https://github.com/effectustasi/autodesk-inventor-mcp) | Inventor | ⬜ Community | 0 | 🟢 2026-10-03 | MCP server giving agents a live COM connection to a running Autodesk Inventor, including a PowerShell script tool. |
| [inventor-mcp (allen2123231)](https://github.com/allen2123231/inventor-mcp) | Inventor | ⬜ Community | 0 | 🟢 2026-09-16 | Inventor MCP with 36 tools (README) for parametric parts, sketches, holes and sheet metal plus modeling skills and API notes; Traditional Chinese docs. |
| [inventor-mcp-server (cenitu)](https://github.com/cenitu/inventor-mcp-server) | Inventor | ⬜ Community | 0 | 🟢 2026-10-27 | Maintained continuation of NeonGlay/inventor-mcp with MCP SDK 2.x support, Inventor 2027 and assembly features. |

## Onshape

9 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Onshape MCP (hedless)](https://github.com/hedless/onshape-mcp) | Onshape | ⬜ Community | 159 | 🟢 2026-09-10 | Onshape REST MCP; README lists 45 core tools. |
| [Onshape MCP (altendky)](https://github.com/altendky/onshape-mcp) | Onshape | ⬜ Community | 20 | 🟢 2026-10-20 | Early-development local Onshape MCP using OAuth. |
| [Onshape MCP (gpambrozio)](https://github.com/gpambrozio/onshape-mcp) | Onshape | ⬜ Community | 4 | 🟢 2026-10-28 | MCP server for Onshape with browser sign-in; README states 93 tools (repo description 87). |
| [cadkit (Onshape)](https://github.com/saltyeg/cadkit-mcp) | Onshape | ⬜ Community | 1 | 🟢 2026-06-25 | Two MCP servers for variable-driven parametric part modelling in Onshape. |
| [ARES Onshape Local](https://github.com/ARES-23247/ares-onshape-local) | Onshape | ⬜ Community | 0 | 🟢 2026-10-09 | Local MCP tools and skills for native Onshape CAD that prepare feature JSON and track recipes while the agent executes via a signed-in browser session, avoiding API-call allowance. |
| [Onshape MCP (gilfoyle19)](https://github.com/gilfoyle19/onshapemcp) | Onshape | ⬜ Community | 0 | 🟡 2026-03-13 | Onshape MCP server for parametric sketching, extrudes, fillets, chamfers, feature trees, variable tables and gear creation. |
| [onshape-cad MCP](https://github.com/Checkmate321/Onshape-MCP) | Onshape | ⬜ Community | 0 | 🟢 2026-10-18 | Local Onshape MCP with constrained sketches, solid features, Variable Studios and configurations. |
| [onshape-mcp (kyle-nelson-berkeley)](https://github.com/kyle-nelson-berkeley/onshape-mcp) | Onshape | ⬜ Community | 0 | 🟢 2026-08-24 | Onshape MCP for parametric modelling and FeatureScript queries from Claude Code. |
| [onshape-mcp-codex](https://github.com/dsh18235538266-crypto/onshape-mcp-codex) | Onshape | ⬜ Community | 0 | 🟢 2026-09-07 | Codex-targeted fork of jarvis-onshape-mcp exposing about 69 tools for sketches, features, assemblies, variable studios, FeatureScript, rendering and STEP/STL/glTF export. |

## DWG

8 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [CADaddy](https://github.com/AICodeForgedev/cadaddy) | DWG, DXF | 🟧 Company | 2 | 🟢 2026-10-21 | Free Rust 2D CAD app that opens and saves DWG/DXF and exposes an MCP interface for AI agents; source-available (FSL-1.1). |
| [cadlens-mcp](https://github.com/cadlens-co/cadlens-mcp) | DWG, DXF, DWF, Cadlens API | 🟧 Company | 1 | 🟢 2026-08-11 | MCP wrapper for the hosted Cadlens CAD parsing API that converts DWG/DXF/DWF drawings into structured JSON for agents. |
| [AI Architectures MCP](https://plans.ai-architectures.com/ai-assistants) | DXF, DWG, IFC (house plans) | 🟧 Company | – | ⚪ – | Remote MCP server to search free house plans and have AI-drafted CAD floor plans (DXF/DWG/PDF) created and changed. |
| [Land Takeoffs MCP](https://github.com/landtakeoffs/land-takeoffs-mcp) | Civil plan sets, DWG, DXF, LandXML | 🟧 Company | 0 | 🟢 2026-10-16 | Hosted remote MCP that returns sitework quantities (storm, sewer, water, paving, cut/fill) from civil plan-set PDFs and CAD files with an Excel bid sheet. |
| [DWG MCP Server](https://github.com/dimitrovakulenko/dwg-mcp-server) | DWG, DXF | ⬜ Community | 21 | 🟢 2026-10-22 | Read-oriented DWG/DXF access for AI clients; source files stay read-only. |
| [QCAD MCP](https://github.com/sandraschi/qcad-mcp) | QCAD, DXF, DWG | ⬜ Community | 18 | 🟢 2026-10-24 | FastMCP server for 2D CAD automation: DXF/DWG parsing, 3D extrusion, room analysis; README says 12 MCP tools. |
| [Codemod3 CAD-MCP](https://github.com/Codemod3/CAD-MCP) | DXF, DWG, ezdxf, ODA File Converter | ⬜ Community | 1 | 🟢 2026-08-12 | Local MCP server that reads, analyses and edits DXF and DWG files with ezdxf (DWG via ODA File Converter) for drawing extraction. |
| [MCP_Dialux](https://github.com/MarcosCastanedaVentura/MCP_Dialux) | DIALux evo, DWG | ⬜ Community | 0 | 🟢 2026-10-14 | MCP server converting a DWG lighting floor plan into a DIALux evo building. |

## QGIS

8 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [QGISMCP (jjsantos01)](https://github.com/jjsantos01/qgis_mcp) | QGIS | ⬜ Community | 1.1k | 🟡 2025-10-01 | Original QGIS-to-Claude MCP bridge based on BlenderMCP; socket plugin in QGIS plus MCP server for projects, layers and PyQGIS execution. Many forks derive from it. |
| [qgis-mcp (nkarasiak)](https://github.com/nkarasiak/qgis-mcp) | QGIS | ⬜ Community | 400 | 🟢 2026-10-17 | QGIS plugin plus FastMCP server where agents drive QGIS: layers, feature editing, Processing, styling, layouts/atlas, cross-layer SQL; README states 125 tools. |
| [QGIS2OllamaMCP](https://github.com/anitagraser/QGIS2OllamaMCP) | QGIS, Ollama | ⬜ Community | 7 | 🟡 2026-01-03 | Fork of QGIS MCP that lets Ollama-hosted LLMs drive QGIS Desktop via a plugin socket server. |
| [CAD2GIS (cad2gis-agent)](https://github.com/Mola-maker/CAD2GIS) | AutoCAD DWG/DXF, QGIS | ⬜ Community | 2 | 🟢 2026-10-24 | Evidence-first DWG/DXF to GIS conversion with QGIS project delivery and a cad2gis-agent MCP plugin for agents. |
| [gis-agent-bridges](https://github.com/YUYU20061107/gis-agent-bridges) | SuperMap, ArcGIS Pro, QGIS, MapGIS, ENVI, FME | ⬜ Community | 1 | 🟢 2026-10-29 | Safety-gated MCP bridges for desktop GIS products with localhost-only access, confirm-gated writes and read-only originals. |
| [ifc-compliance-mcp](https://github.com/meet-rehman/ifc-compliance-mcp) | IFC, IfcOpenShell, QGIS | ⬜ Community | 0 | 🟢 2026-10-09 | Prototype MCP tool that compares as-built site coverage stored in an IFC file with the site-coverage limit stated by a regulation-answering AI system (Stuttgart case). |
| [QGIS-MCP (oopsboogaloo)](https://github.com/oopsboogaloo/QGIS-MCP) | QGIS | ⬜ Community | 0 | 🟢 2026-10-12 | Early-build QGIS MCP server with a live path to a plugin in a running QGIS session and a headless qgis_process path; spec is complete, README says early build. |
| [qgis-mcp (piatkowski)](https://github.com/piatkowski/qgis-mcp) | QGIS | ⬜ Community | 0 | 🟢 2026-07-28 | Local MCP server and QGIS plugin to inspect and transform layers in the open QGIS project from Claude Desktop (English and Polish docs). |

## Unity

8 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Unity MCP Server (official, AI Assistant package)](https://docs.unity3d.com/Packages/com.unity.ai.assistant@2.19/manual/integration/unity-mcp-overview.html) | Unity | 🟦 Official | – | ⚪ – | Unity Editor acts as an MCP server (relay binary plus editor bridge) exposing scene, asset, script and console tools; DEPRECATED by Unity in favour of the Unity CLI (`unity mcp`), see Unity's migration page. |
| [MCP for Unity](https://github.com/CoplayDev/unity-mcp) | Unity | 🟧 Company | 15.6k | 🟢 2026-10-19 | Most-starred Unity MCP bridge; manage assets, control scenes, edit scripts and run tests from an MCP client, not affiliated with Unity Technologies. |
| [AnkleBreaker Unity MCP](https://github.com/AnkleBreaker-Studio/unity-mcp-server) | Unity | 🟧 Company | 531 | 🟢 2026-10-23 | Unity MCP server and editor plugin for scene authoring, tests and builds; README cites 80 exposed tools plus advanced on-demand tools. |
| [Unity-MCP (AI Game Developer)](https://github.com/IvanMurzak/Unity-MCP) | Unity | ⬜ Community | 4.6k | 🟢 2026-10-30 | Unity MCP tools, skills and CLI that also work inside compiled games at runtime; any C# method can be exposed as a tool. |
| [mcp-unity](https://github.com/CoderGamester/mcp-unity) | Unity | ⬜ Community | 2k | 🟢 2026-10-11 | MCP plugin connecting the Unity Editor to Cursor, Claude Code, Codex, Windsurf and other IDE clients. |
| [isuzu-shiranui UnityMCP](https://github.com/isuzu-shiranui/UnityMCP) | Unity | ⬜ Community | 338 | 🟢 2026-10-08 | Unity Editor serves MCP itself over local Streamable HTTP, with a companion native CLI; tools are C# static methods marked [McpTool]. |
| [Funplay MCP for Unity](https://github.com/FunplayAI/funplay-unity-mcp) | Unity | ⬜ Community | 276 | 🟢 2026-10-28 | MIT-licensed Unity Editor MCP with execute_code, prompts/resources, input simulation, screenshots and play-mode automation. |
| [Unity AI Bridge](https://github.com/butterlatte-zhang/unity-ai-bridge) | Unity | ⬜ Community | 23 | 🟡 2026-03-25 | Remote-controls the Unity Editor from AI IDEs through file-based IPC with a pure-stdlib Python MCP server and a C# Unity package; README lists 65 tools. |

## Unreal Engine

8 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Flopperam Unreal Engine MCP](https://github.com/flopperam/unreal-engine-mcp) | Unreal Engine | 🟧 Company | 1.1k | 🟢 2026-06-26 | Unreal Editor MCP with a hosted version and an open-source local Python version (50+ tools across 9 domains per README); README says the project is now owned by Aura. |
| [EngineWire / Unreal Engine MCP](https://github.com/ChiR24/Unreal_mcp) | Unreal Engine | 🟧 Company | 997 | 🟢 2026-10-30 | MCP server plus native C++ Automation Bridge plugin to drive a live Unreal Editor (levels, Blueprints, UI, materials, effects); README says Unreal 5.0-5.8 and a single tool with over 400 capabilities in 0.6.0. |
| [chongdashu unreal-mcp](https://github.com/chongdashu/unreal-mcp) | Unreal Engine | ⬜ Community | 2.1k | 🔴 2025-04-22 | Widely-starred early Unreal Engine MCP; README marks it experimental and last commit is April 2025. |
| [runreal unreal-mcp](https://github.com/runreal/unreal-mcp) | Unreal Engine | ⬜ Community | 117 | 🔴 2025-06-06 | Unreal Engine MCP built on the built-in Python Remote Execution protocol, so no UE plugin is needed. |
| [unreal-mcp (runeape-sats)](https://github.com/runeape-sats/unreal-mcp) | Unreal Engine | ⬜ Community | 47 | 🟡 2026-03-31 | Pure-Python MCP server for Unreal Engine 5.3 via the Remote Control API: arrange assets, inspect actors, call arbitrary Remote Control functions and save levels. |
| [UnrealMCP community edition](https://github.com/aadeshrao123/Unreal-MCP) | Unreal Engine | ⬜ Community | 39 | 🟢 2026-08-06 | Community edition of CodeFizz Editor Agent with 288 commands across 15 categories (materials, Blueprint graphs, Niagara, actors); README says new work goes to the commercial build. |
| [Funplay MCP for Unreal](https://github.com/FunplayAI/funplay-unreal-mcp) | Unreal Engine | ⬜ Community | 8 | 🟢 2026-06-23 | Pure-Python Unreal Editor plugin exposing a local MCP server (execute_python, API discovery, screenshots, PIE automation) with a Node stdio bridge. |
| [UEAgent](https://github.com/CarlxsMG/UEAgent) | Unreal Engine | ⬜ Community | 1 | 🟢 2026-10-27 | Unreal Engine 5.7/5.8 editor plugin that serves MCP over Streamable HTTP from inside the editor; README claims 1,500+ tools for Blueprints, levels, lighting and more. |

## Figma

7 servers · [↑ back to the list](#servers-by-software)

| Server | Works with | Type | ★ | Updated | What it does |
| :-- | :-- | :-- | --: | :-- | :-- |
| [Figma MCP Server (official)](https://github.com/figma/mcp-server-guide) | Figma | 🟦 Official | 2.1k | 🟢 2026-10-28 | Figma's official remote MCP server (https://mcp.figma.com/mcp) giving agents design context and canvas write access; this repo is its guide. |
| [Framelink MCP for Figma](https://github.com/GLips/Figma-Context-MCP) | Figma | 🟧 Company | 16.1k | 🟢 2026-06-24 | Popular MCP that feeds Figma layout data to coding agents such as Cursor to implement designs. |
| [Figma Console MCP](https://github.com/southleft/figma-console-mcp) | Figma | ⬜ Community | 2.6k | 🟢 2026-10-29 | Design-system-focused bidirectional Figma MCP with design-code parity, accessibility checks and write access. |
| [figma-use](https://github.com/dannote/figma-use) | Figma | ⬜ Community | 614 | 🟢 2026-07-03 | CLI and MCP server (90+ tools per README) giving agents read/write control of Figma: create frames, set layout, styles and export; README warns Figma 126+ needs daemon pipe mode. |
| [figma-ui-mcp](https://github.com/TranHoaiHung/figma-ui-mcp) | Figma | ⬜ Community | 266 | 🟢 2026-10-26 | Bidirectional Figma bridge letting AI draw UI on the canvas and read designs back, no API key. |
| [figma-mcp-rust](https://github.com/alvinindra/figma-mcp-rust) | Figma | ⬜ Community | 74 | 🟢 2026-10-12 | Rust port of figma-mcp-go with a plugin bridge, no API token or rate limits, 73 tools per description. |
| [figmanage](https://github.com/dannykeane/figmanage) | Figma | ⬜ Community | 8 | 🟢 2026-10-12 | Local MCP server and CLI for managing a Figma workspace: find files, organize projects, review access and manage teams and seats. |

