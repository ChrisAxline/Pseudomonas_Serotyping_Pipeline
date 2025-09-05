import os
import shutil

# Path to your folder with BLAST outfmt6 files
folder = "/Users/chrisaxline/Desktop/PASP_serotype_blast_results"

# New folder for files with headers
dest_folder = os.path.join(folder, "/Users/chrisaxline/Desktop/PASP_serotype_blast_results/PASP_with_headers")
os.makedirs(dest_folder, exist_ok=True)

moved_count = 0
skipped_count = 0

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    # Skip directories
    if not os.path.isfile(filepath):
        continue

    # Check only text-like files
    if filename.endswith(".txt") or filename.endswith(".out") or filename.endswith(".tsv"):
        with open(filepath, "r") as f:
            first_line = f.readline()

        if first_line.startswith("qseqid"):
            shutil.move(filepath, os.path.join(dest_folder, filename))
            print(f"Moved: {filename}")
            moved_count += 1
        else:
            skipped_count += 1

print("\nSummary:")
print(f"  Moved files:   {moved_count}")
print(f"  Left in place: {skipped_count}")
