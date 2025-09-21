import csv
import re
import subprocess
from pathlib import Path

# ---- Config ----
OPENSCAD_BIN  = "openscad"
TEMPLATE_SCAD = "tag_template.scad"
CSV_FILE      = "guitar_inventory.csv"
OUTPUT_DIR    = "tags"
FORCE_UPPER   = False

# ---- Helpers ----
def slugify(s: str) -> str:
    s = (s or "").strip()
    s = re.sub(r"\s+", "_", s)
    s = re.sub(r"[^A-Za-z0-9_\-\.]", "", s)
    return s

def get_field(row, *names, default=""):
    for n in names:
        if n in row and row[n] is not None:
            return row[n]
    lower_map = {k.lower(): k for k in row.keys()}
    for n in names:
        k = lower_map.get(n.lower())
        if k:
            return row[k]
    return default

def line_text(v: str) -> str:
    v = (v or "").strip()
    return v.upper() if FORCE_UPPER else v

def scad_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')

def posix_path(p: Path) -> str:
    return p.as_posix()

# ---- Main ----
def main():
    script_dir = Path(__file__).resolve().parent
    template_path = (script_dir / TEMPLATE_SCAD).resolve()
    if not template_path.exists():
        print(f"ERROR: Template not found: {template_path}")
        return

    template_for_scad = posix_path(template_path)
    outdir = (script_dir / OUTPUT_DIR)
    outdir.mkdir(parents=True, exist_ok=True)

    print("===================================")
    print("🎸 Guitar Case Tag Generator")
    print("===================================")
    print(f"Reading inventory from: {CSV_FILE}")
    print(f"Template: {template_path}")
    print(f"Output folder: {outdir}")
    print("")

    total = 0
    success = 0
    fail = 0
    skipped = 0

    with open(script_dir / CSV_FILE, newline='', encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            year  = line_text(get_field(row, "Year"))
            make  = line_text(get_field(row, "Make"))
            model = line_text(get_field(row, "Model"))
            color = line_text(get_field(row, "Color", "Colour"))

            l1 = scad_escape(year)
            l2 = scad_escape(make)
            l3 = scad_escape(model)
            l4 = scad_escape(color)

            stem = "tag_" + "_".join([x for x in [year, make, model, color] if x])
            stem = slugify(stem) or "tag"

            scad_path = outdir / f"{stem}.scad"
            stl_path  = outdir / f"{stem}.stl"

            total += 1
            print(f"[{total}] Building tag for: {year} {make} {model} {color}")

            if stl_path.exists():
                print(f"   ⏩ Skipping (already exists) → {stl_path.name}")
                skipped += 1
                continue

            scad_src = (
                f'use <{template_for_scad}>;\n'
                f'guitar_tag("{l1}", "{l2}", "{l3}", "{l4}");\n'
            )
            scad_path.write_text(scad_src, encoding="utf-8")

            try:
                subprocess.run([OPENSCAD_BIN, "-o", str(stl_path), str(scad_path)],
                               check=True, capture_output=True, text=True)
                print(f"   ✅ Success → {stl_path.name}")
                success += 1
            except subprocess.CalledProcessError as e:
                print(f"   ❌ FAIL → {scad_path.name}")
                if e.stderr:
                    print("      OpenSCAD error:", e.stderr.strip())
                fail += 1

    print("\n===================================")
    print("Generation complete.")
    print(f"Total tags processed: {total}")
    print(f"   ✅ Success: {success}")
    print(f"   ⏩ Skipped: {skipped}")
    print(f"   ❌ Failed:  {fail}")
    print("===================================")

if __name__ == "__main__":
    main()
