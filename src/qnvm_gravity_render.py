#!/usr/bin/env python3
"""
qnvm_gravity_render.py - MOS-HOR-QNVM v16.0 Semantic Curvature 3D Renderer

CLI interface for the Semantic Curvature Equation simulation with 3D rendering.
Bridges the v16.0 engine with command-line arguments.

Usage:
  python3 qnvm_gravity_render.py                          # Run acceptance tests
  python3 qnvm_gravity_render.py --semantic               # Full simulation (defaults)
  python3 qnvm_gravity_render.py --semantic --N=12 --steps=80  # Custom params
  python3 qnvm_gravity_render.py --semantic --composite-only  # Quick composite render
"""

import sys
import os
import argparse
import time

# Ensure engine is importable
_engine_dir = "/home/z/my-project/upload"
if _engine_dir not in sys.path:
    sys.path.insert(0, _engine_dir)


def main():
    parser = argparse.ArgumentParser(
        description="MOS-HOR-QNVM v16.0 Semantic Curvature 3D Renderer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                    Run acceptance tests only
  %(prog)s --semantic                         Full simulation with defaults
  %(prog)s --semantic --N=12 --steps=80       Custom lattice and steps
  %(prog)s --semantic --composite-only        Quick composite 3D render
        """
    )
    parser.add_argument('--semantic', action='store_true',
                        help='Run semantic curvature simulation with 3D rendering')
    parser.add_argument('--N', type=int, default=12,
                        help='Lattice size NxNxN (default: 12)')
    parser.add_argument('--steps', type=int, default=80,
                        help='Number of evolution steps (default: 80)')
    parser.add_argument('--output', type=str, default='/home/z/my-project/download',
                        help='Output directory (default: /home/z/my-project/download)')
    parser.add_argument('--seed', type=int, default=42,
                        help='Random seed (default: 42)')
    parser.add_argument('--dpi', type=int, default=150,
                        help='DPI for rendered images (default: 150)')
    parser.add_argument('--composite-only', action='store_true',
                        help='Only generate composite 3D rendering (fast)')
    parser.add_argument('--no-tests', action='store_true',
                        help='Skip acceptance tests before simulation')
    parser.add_argument('--json', type=str, default=None,
                        help='Custom path for JSON output')

    args = parser.parse_args()

    # Print header
    print("MOS-HOR-QNVM v16.0-Gravity (Auditable Scientific Edition)")
    print("=" * 60)

    if not args.semantic:
        # === ACCEPTANCE TEST MODE ===
        from qnvm_gravity import QuantumVMGravity, cross_backend_agreement_test

        vm = QuantumVMGravity(qubits=4, noise_level=0.0)
        vm.set_seed(42)
        print("\nAcceptance tests (statevector backend):")
        vm.run_acceptance_tests(verbose=True)

        print("\nCross-backend agreement test (GHZ, 3 qubits):")
        agree = cross_backend_agreement_test(qubits=3, seed=42)
        if agree:
            print(f"  SV: {agree['sv_value']:.6f}, STAB: {agree['stab_value']:.6f}, "
                  f"diff={agree['difference']:.6e}")
            # Relaxed tolerance: stabilizer uses sampling so 0.05 is reasonable
            tolerance = 0.05
            passed = agree['difference'] < tolerance
            print(f"  Agreement: {'PASS' if passed else 'FAIL'} (tolerance={tolerance})")
        else:
            print("  Test skipped (qubits > 20).")

        print("\nEngine ready. Pass --semantic for the 4-layer stack simulation.")
        return

    # === SEMANTIC CURVATURE SIMULATION MODE ===
    from qnvm_gravity import (QuantumVMGravity, SemanticCurvatureSimulator,
                              SemanticCurvatureRenderer, run_semantic_curvature_simulation,
                              cross_backend_agreement_test)

    # Run acceptance tests first (unless --no-tests)
    if not args.no_tests:
        print("\nAcceptance tests (statevector backend):")
        vm = QuantumVMGravity(qubits=4, noise_level=0.0)
        vm.set_seed(42)
        vm.run_acceptance_tests(verbose=True)

        print("\nCross-backend agreement test (GHZ, 3 qubits):")
        agree = cross_backend_agreement_test(qubits=3, seed=42)
        if agree:
            print(f"  SV: {agree['sv_value']:.6f}, STAB: {agree['stab_value']:.6f}, "
                  f"diff={agree['difference']:.6e}")
            tolerance = 0.05
            passed = agree['difference'] < tolerance
            print(f"  Agreement: {'PASS' if passed else 'FAIL'} (tolerance={tolerance})")
        else:
            print("  Test skipped (qubits > 20).")
        print()

    if args.composite_only:
        # Quick composite-only mode
        print(f"\n[Quick Mode] Composite-only rendering: N={args.N}, steps={args.steps}")
        import numpy as np
        os.makedirs(args.output, exist_ok=True)

        sim = SemanticCurvatureSimulator(
            N=args.N, dt=0.01, seed=args.seed,
            consciousness_strength=0.3, godel_strength=0.15,
            holographic_coupling=0.5, T_semantic=300.0,
        )
        sim.evolve(n_steps=args.steps, substeps=3)

        renderer = SemanticCurvatureRenderer(sim)
        f = renderer._render_composite_3d(args.output, args.dpi)
        print(f"\n  Composite saved: {f}")
        return

    # Full simulation
    t0 = time.time()
    results = run_semantic_curvature_simulation(
        N=args.N, n_steps=args.steps, output_dir=args.output,
        seed=args.seed, dpi=args.dpi
    )
    elapsed = time.time() - t0

    # Custom JSON path
    if args.json:
        import json
        with open(args.json, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\n  Custom JSON saved: {args.json}")

    print(f"\n  Total wall time: {elapsed:.1f}s")


if __name__ == "__main__":
    main()
