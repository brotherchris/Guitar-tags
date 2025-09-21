🎸 Guitar Case Tag Generator

This project generates 3D-printable case tags for your guitars.
Each tag is the same physical shape, but with custom text (Year, Make, Model, Color) embossed (or engraved) on it.
You can print in one color, or use your slicer’s “paint” feature to color the letters differently.

📦 Requirements
Software you need to install:

OpenSCAD 2021+

Required to generate .stl models from the template.

On Windows: make sure openscad.exe is on your PATH, or edit app.py to point to it.

On macOS/Linux: you can usually install from your package manager or download from the website.

Python 3.8+

Required to run the generator script.

Windows users: during install, check “Add Python to PATH.”

📂 File Structure
Guitar tags/
├── app.py                # Python script (generator)
├── tag_template.scad     # Tag design template
├── guitar_inventory.csv  # Your guitar list
└── tags/                 # Output folder (auto-created for SCAD + STL files)

📝 CSV Format

Your guitar inventory is kept in a CSV file called guitar_inventory.csv.
The script expects four columns:

Year,Make,Model,Color
2013,Fender,Sonoran,Black
2007,Rickenbacker,Dakota,Wood grain
2010,Gibson,SG,Cherry
2006,Gibson,Les Paul,TV Yellow
1995,Fender,Jagstang,Blue


Column headers must be present (Year, Make, Model, Color).

Case doesn’t matter (Color or colour both work).

Extra columns will be ignored.

Empty fields are allowed (the tag will still generate).

▶️ Usage

Open a terminal (PowerShell on Windows, Terminal on macOS/Linux).

Navigate to the Guitar tags folder.

Run the script:

python app.py


The script will:

Read guitar_inventory.csv.

Create a .scad file for each guitar in tags/.

Call OpenSCAD to export one .stl file per tag.

Skip any tags that already have an .stl file (so you don’t regenerate them every run).

🖥️ Example Console Output
===================================
🎸 Guitar Case Tag Generator
===================================
Reading inventory from: guitar_inventory.csv
Template: tag_template.scad
Output folder: tags

[1] Building tag for: 2013 Fender Sonoran Black
   ✅ Success → tag_2013_Fender_Sonoran_Black.stl
[2] Building tag for: 2007 Rickenbacker Dakota Wood grain
   ⏩ Skipping (already exists) → tag_2007_Rickenbacker_Dakota_Wood_grain.stl
[3] Building tag for: 2010 Gibson SG Cherry
   ❌ FAIL → tag_2010_Gibson_SG_Cherry.scad
      OpenSCAD error: Parser error: syntax error ...

===================================
Generation complete.
Total tags processed: 3
   ✅ Success: 1
   ⏩ Skipped: 1
   ❌ Failed:  1
===================================

⚙️ Customizing the Tag

Open tag_template.scad in OpenSCAD to change:

Tag size (default 100 × 50 mm, fits the longest “Rickenbacker”).

Text size and spacing (base_text_size, line_spacing).

Embossed vs. Engraved text → set raise_text = true or false.

Hole diameter and flange size.

Border height and thickness.

After editing, re-run python app.py to generate updated .stl files.

🖨️ Printing Tips

Recommended layer height: 0.2 mm or finer.

Text looks best with 0.15 mm layers.

Use at least 3 perimeters for strong borders and flange.

PLA and PETG both work well.

To add color, use your slicer’s color painting tool to paint the letters.

🔧 Troubleshooting

“Ignoring unknown module ‘guitar_tag’”
→ Make sure tag_template.scad has the guitar_tag(...) module (not the split base/text version).

“openscad not found”
→ Add OpenSCAD to your PATH or update the OPENSCAD_BIN variable in app.py with the full path to openscad.exe.

Want to regenerate all tags?
→ Delete the existing .stl files in tags/ before re-running the script.