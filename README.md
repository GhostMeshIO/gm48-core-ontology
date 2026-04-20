# GhostMesh48 Interactive Dashboard

**Dynamic 3D exploration of the 12-Ontology Semantic Curvature Stack**

---

## Overview

GhostMesh48 is a federated framework that models meaning, knowledge, consciousness, causality, and geometry as interacting fields. This repository provides:

1. **Ontology Registry** — 7 core + 5 supporting ontologies with typed contracts and formal equations.
2. **Simulation Engine** — A discrete dynamical system on an N-cube lattice, ported from the MOS-HOR-QNVM v16 `SemanticCurvatureSimulator`.
3. **Interactive Dashboard** — Real-time 3D visualizations, parameter exploration, and measurable-proxy metrics via a Next.js + Three.js web application.

### Repository Identity

> *"Where fractal Einstein equations meet non-Hermitian consciousness operators and holographic thermodynamics — rendered live in 3D."*

---

## The Surviving Ontology Stack

After consolidation from the GhostMesh48 corpus, the following ontologies are preserved with **active simulation support** (colour-coded by layer in the dashboard):

| # | Code  | Full Name                              | Layer | Status              |
|---|-------|----------------------------------------|-------|---------------------|
| 1 | **GSG**  | Generalised Semantic Gravity              | Core  | Full simulation + rendering |
| 2 | **NHKO** | Non-Hermitian Knowledge Operator         | Core  | Eigenvalue trajectories |
| 3 | **SC**   | Semantic Criticality                    | Core  | Phase-transition detection |
| 4 | Z3-OT  | Triadic Ontology Transform               | Core  | Gauge-rotation overlay |
| 5 | **HS**   | Holographic Screen                       | Core  | Boundary extraction |
| 6 | **WWQG** | Wave-Function Well-Being QG              | Core  | Coherence-time maps |
| 7 | **CRF**  | Causal Recursion Field                   | Core  | Vector-field rendering |
| 8 | CPGO   | Computational Proof Governance           | Support | Oracle markers |
| 9 | **RSSO** | Recursive Self-Similar Ontology          | Support | Multi-scale RG flow |
|10 | **STTO** | Semantic-Thermodynamic Transport Ont.    | Support | Belief-density currents |
|11 | FAS    | Fractal Autopoietic System               | Support | D_f texture overlay |
|12 | **QNHGO**| Quantum Non-Hermitian Gödel Ontology     | Support | Spectrum-shift viz |

**Bold** = strongest ontologies with validated measurable proxies. The remaining are formal templates or proxy models — not yet validated physics.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Browser (Frontend)                           │
│  ┌─────────────────┐  ┌─────────────────┐  ┌────────────────────┐  │
│  │ React Dashboard  │  │  Three.js 3D    │  │  Recharts Metrics  │  │
│  │ (controls,       │  │  renderer       │  │  (entropy, overlap,│  │
│  │  ontology panel) │  │  (lattice pts)  │  │   D_f, etc.)       │  │
│  └────────┬─────────┘  └────────┬────────┘  └─────────┬──────────┘  │
│           └────────────────────┼──────────────────────┘             │
│                                │ WebSocket                          │
└────────────────────────────────┼────────────────────────────────────┘
                                 │
┌────────────────────────────────┼────────────────────────────────────┐
│                        Backend Services                             │
│  ┌─────────────────────────────▼──────────────────────────────┐    │
│  │  Simulation Mini-Service (Bun, port 3004)                  │    │
│  │  - SemanticCurvatureEngine (pure TypeScript)               │    │
│  │  - 12-ontology metric pipeline                             │    │
│  │  - Frame streaming via Socket.IO                           │    │
│  └───────────────────────────────────────────────────────────┘    │
│  ┌───────────────────────────────────────────────────────────┐    │
│  │  Next.js API Routes (port 3000)                           │    │
│  │  - Ontology metadata & presets                             │    │
│  │  - Export / snapshot endpoints                             │    │
│  └───────────────────────────────────────────────────────────┘    │
└───────────────────────────────────────────────────────────────────┘
```

---

## The Enhanced Four-Layer Stack Equation

The dashboard simulates this discrete dynamical system on an N x N x N lattice:

```
G_{mu,nu}^{(fractal)}(l) = 8*pi*G(l) * [
  Layer 1:  T_{mu,nu}^{(semantic)} + (i / tau_collapse) * C_{mu,nu}
  Layer 2:  rho_bit(l) * (1 + A_gamma / (4*G(l))) * g_{mu,nu}
  Layer 3:  W_{mu,nu}^{(Godel)}(l)
]
```

### Measurable Proxies (v16 "Truelist")

| Proxy                    | Computation                                   | Rigour     |
|--------------------------|-----------------------------------------------|------------|
| delta_S_epistemic        | Shannon entropy of \|psi\|^2 distribution      | Validated  |
| <semantic\|self>        | Complex inner product with initial state       | Validated  |
| T_semantic               | \|Re(psi)\|^2 knowledge density                | Validated  |
| C_magnitude              | \|Im(psi)\|^2 mystery / affect                 | Validated  |
| tau_collapse             | 1 / \|dC_mag/dt\| consciousness coherence    | Validated  |
| rho_bit                  | S * k_B * T / c^2  (Landauer bit mass)         | Physical   |
| A_gamma                  | Boundary face count of high-information region | Proxy      |
| W_Godel                  | Phase-gradient anomaly detection               | Proxy      |
| D_fractal                | 3D box-counting on curvature field             | Proxy      |
| G(l)                     | RG-flow effective coupling                     | Proxy      |

---

## Quick Start

### Prerequisites

- Node.js 18+ and Bun
- A modern browser with WebGL support

### Installation

```bash
git clone https://github.com/GhostMeshIO/gm48-interactive-dashboard.git
cd gm48-interactive-dashboard
bun install
```

### Running the Dashboard

```bash
# Start the simulation mini-service
cd mini-services/simulation-service && bun install && bun --hot index.ts &

# Start the Next.js dev server
cd ../.. && bun run dev
```

Open the dashboard at `http://localhost:3000`.

### Default Simulation

The dashboard loads with N=10, 60 steps, seed=42, and standard parameters. Adjust sliders in real-time and observe immediate changes in the 3D lattice and metrics charts.

---

## Project Layout

```
gm48-interactive-dashboard/
├── README.md                          # This file
├── IMPLEMENTATION_BLUEPRINT.md        # Architecture & roadmap
├── package.json
├── next.config.ts
├── tailwind.config.ts
├── prisma/
├── public/
│   └── logo.svg
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx                   # Main dashboard entry
│   │   ├── globals.css
│   │   └── api/
│   │       ├── ontology-info/route.ts # Ontology metadata endpoint
│   │       └── presets/route.ts       # Parameter presets endpoint
│   ├── components/
│   │   ├── ui/                        # shadcn/ui components
│   │   ├── dashboard/
│   │   │   ├── OntologyPanel.tsx      # Layer toggles & spotlight
│   │   │   ├── ParameterSliders.tsx   # Consciousness, Godel, etc.
│   │   │   ├── TimeControls.tsx       # Play/Pause/Scrub
│   │   │   └── PresetSelector.tsx     # Predefined parameter sets
│   │   ├── renderer/
│   │   │   ├── LatticeScene.tsx       # Three.js 3D scene
│   │   │   ├── PointCloud.tsx         # Instanced lattice points
│   │   │   └── OntologyColors.ts      # Color mapping per ontology
│   │   └── charts/
│   │       ├── EntropyChart.tsx
│   │       ├── OverlapChart.tsx
│   │       ├── FractalDimChart.tsx
│   │       └── MetricsPanel.tsx       # Combined metrics view
│   ├── lib/
│   │   ├── simulation.ts             # Core simulation engine (TS port)
│   │   ├── ontologies.ts             # 12-ontology metric definitions
│   │   ├── store.ts                  # Zustand state management
│   │   ├── use-simulation-socket.ts  # WebSocket hook
│   │   └── utils.ts
│   └── hooks/
├── mini-services/
│   └── simulation-service/
│       ├── index.ts                  # Socket.IO simulation server
│       └── package.json
├── upload/                           # Reference: original Python engine
│   ├── qnvm_gravity.py               # MOS-HOR-QNVM v16 (Python)
│   └── GhostMesh48 - Consolidated Ontology Registry (v1.0).md
└── download/                         # Generated artefacts
    ├── semantic_curvature_results.json
    ├── semantic_3d_manifold.png
    ├── proxy_time_evolution.png
    └── semantic_curvature_project.zip
```

---

## Test Results Snapshot

From `semantic_curvature_results.json` (N=12, 80 steps, seed=42):

| Proxy                    | Initial     | Final       |
|--------------------------|-------------|-------------|
| delta_S_epistemic        | 13.238      | 13.249      |
| <semantic\|self> (Re)   | 1.000       | 0.990       |
| <semantic\|self> (Im)   | 0.000       | -0.025      |
| T_semantic_avg           | 0.0351      | 0.0356      |
| C_mystery_avg            | 0.0275      | 0.0288      |
| tau_collapse             | inf         | 0.050       |
| rho_bit_total            | 1.90e-22    | 1.91e-22    |
| A_gamma                  | 1856        | 1856        |
| W_godel_count            | 0           | 0           |
| D_fractal                | 2.981       | 2.976       |
| G_effective              | 1.000       | 1.001       |

Cross-backend agreement (statevector vs stabilizer): PASS (diff < 0.05).

---

## Rigorous vs Speculative Boundaries

| Category                    | Examples                                      |
|-----------------------------|-----------------------------------------------|
| **Rigorous (validated)**    | Shannon entropy, inner products, box-counting |
| **Physical proxies**        | Landauer bit mass, Planck-scale constants     |
| **Computational proxies**   | Holographic area, phase-gradient anomalies     |
| **Speculative / formal**    | CPGO oracle decisions, FAS autopoietic loops  |
| **Symbolic / exploratory**  | Information pressure, amplification efficiency |

The dashboard labels each metric with its rigour level in the metrics panel.

---

## Ontology Visualisation Modes

| Ontology | 3D Representation                                | 2D Panel                    |
|----------|-------------------------------------------------|-----------------------------|
| GSG      | Curvature colour field (hot=positive, cold=neg) | Stress-energy components    |
| NHKO     | Complex eigenvalue map (hue=Re, sat=Im)         | Eigenvalue scatter plot     |
| SC       | Insight-event highlights (dC/dt threshold)       | Phase diagram (C vs J/h)    |
| Z3-OT    | 3-colour cyclic gauge rotation                  | Gauge angle meter           |
| HS       | Transparent boundary isosurface                  | Entropy vs area plot        |
| WWQG     | Coherence-time colouring with thermal threshold  | Coherence vs temperature    |
| CRF      | Vector-field arrows (causal circulation)         | Loop integral over time     |
| CPGO     | Oracle intervention markers (stars)              | Intervention count          |
| RSSO     | 2x2 multi-scale RG sub-grid                     | Beta-function plot          |
| STTO     | Belief-density volume + knowledge flow lines     | Entropy production rate     |
| FAS      | Fractal-dimension texture pattern                | Box-counting plot           |
| QNHGO    | NHKO colours + Godel anomaly sparkles            | Eigenvalue histogram        |

---

## Keyboard Shortcuts

| Key       | Action             |
|-----------|--------------------|
| Space     | Play / Pause       |
| Right     | Step forward       |
| Left      | Step backward      |
| R         | Reset simulation   |
| 1-9, 0    | Toggle ontology 1-10 |
| H         | Toggle all layers  |

---

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/my-ontology`).
3. Add your ontology module under `src/lib/ontologies.ts`.
4. Submit a pull request with a description of the measurable proxies.

---

## References

- [GhostMesh48 Consolidated Ontology Registry (v1.0)](https://github.com/GhostMeshIO/gm48-core-ontology/blob/main/docs/GhostMesh48%20-%20Consolidated%20Ontology%20Registry%20(v1.0).md)
- [Extended Supporting Mathematics](https://github.com/GhostMeshIO/docs/gm48-core-ontology/blob/main/GhostMesh48%20%E2%80%94%20Extended%20Supporting%20Mathematics.md)
- [3D Rendering Engine Details](https://github.com/GhostMeshIO/gm48-core-ontology/blob/main/docs/RENDERING_ENGINE.md) / [Rendering Script](https://github.com/GhostMeshIO/gm48-core-ontology/blob/main/src/qnvm_gravity_render.py)
- [QNVM - MOS-HOR Quantum Physics Lab](https://github.com/GhostMeshIO/gm48-core-ontology/blob/main/src/qnvm_gravity.py) 
- [3D Render Test Results (Folder)](https://github.com/GhostMeshIO/gm48-core-ontology/tree/main/test_results) 

---

## Licence

MIT
