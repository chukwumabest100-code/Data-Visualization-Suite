"""
Data Visualization Suite
Runs all chart scripts and saves outputs to the /output folder.
"""

import os
import sys
import importlib.util
import traceback

CHARTS_DIR = os.path.join(os.path.dirname(__file__), "charts")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.chdir(OUTPUT_DIR)

chart_scripts = sorted([
    f for f in os.listdir(CHARTS_DIR) if f.endswith(".py")
])

print(f"Found {len(chart_scripts)} chart scripts.\n")

success = []
failed = []

for script in chart_scripts:
    script_path = os.path.join(CHARTS_DIR, script)
    print(f"  Generating: {script} ...", end=" ")
    try:
        spec = importlib.util.spec_from_file_location("chart_module", script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print("✓")
        success.append(script)
    except Exception as e:
        print(f"✗ FAILED")
        traceback.print_exc()
        failed.append(script)

print(f"\n✅ {len(success)} charts generated successfully in /output")
if failed:
    print(f"❌ {len(failed)} chart(s) failed: {', '.join(failed)}")
print("Done.")
