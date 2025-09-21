🎸 Guitar Case Tag Generator

Make personalized 3D-printed case tags for your guitars!
Each tag has custom text (Year, Make, Model, Color) pulled from a simple CSV file.

📦 Requirements
Software you need to install:

OpenSCAD 2021+
 – generates STL files.

Python 3.8+
 – runs the generator script.

📂 File Structure
Guitar tags/
├── app.py                       # Python script (generator)
├── tag_template.scad            # Tag design template
├── guitar_inventory_example.csv # Example guitar list (safe to share)
├── .gitignore                   # Prevents your real CSV & tags from uploading
└── tags/                        # Output folder (auto-created for SCAD + STL files)

📝 CSV Format

Your real inventory should be saved as guitar_inventory.csv (this file is ignored by Git so it stays private).
For reference, an example file guitar_inventory_example.csv is included:

Year,Make,Model,Color
2013,Fender,Stratocaster,Sunburst
2007,Gibson,SG,Cherry
1995,Ibanez,Roadstar II,Black
2010,Danelectro,U2,Yellow
2020,PRS,Custom 24,Blue Fade


Column headers must be present (Year, Make, Model, Color).

Case doesn’t matter (Color or colour both work).

Extra columns are ignored.

Empty fields are allowed.

👉 To use: make a copy of guitar_inventory_example.csv, rename it to guitar_inventory.csv, and fill it with your own guitars.

▶️ Usage

Open a terminal in the Guitar tags folder.

Run the script:

python app.py


STLs will be created in the tags/ folder.

The script will skip files that already exist, so you don’t rebuild everything each time.

⚙️ Customizing the Tag

Open tag_template.scad in OpenSCAD to tweak:

Tag size (default: 100 × 50 mm, fits longest name “Rickenbacker”).

Text size & spacing.

Hole diameter & flange size.

Raised vs. engraved text → toggle raise_text.

🖨️ Printing

0.2 mm layers work fine, 0.15 mm makes sharper text.

Use at least 3 perimeters for strength.

PLA and PETG both work well.

Use your slicer’s color painting tool to make the letters a second color.

🔒 Privacy

guitar_inventory.csv (your real data) is ignored by Git thanks to .gitignore.

Only guitar_inventory_example.csv is shared.