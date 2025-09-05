import os

# Path to your folder with BLAST outfmt6 files
folder = "/Users/chrisaxline/Desktop/PASP_serotype_blast_results"

# BLAST outfmt6 headers
headers = "qseqid\tsseqid\tpident\tlength\tmismatch\tgapopen\tqstart\tqend\tsstart\tsend\tevalue\tbitscore\n"

processed_count = 0
skipped_count = 0

for filename in os.listdir(folder):
    if filename.endswith(".txt") or filename.endswith(".out") or filename.endswith(".tsv"):
        filepath = os.path.join(folder, filename)

        # Read the file
        with open(filepath, "r") as f:
            lines = f.readlines()

        # Skip if it already has a header
        if lines and lines[0].startswith("qseqid"):
            print(f"Skipping (already has header): {filename}")
            skipped_count += 1
            continue

        # Create new filename
        base, ext = os.path.splitext(filename)
        new_filename = f"{base}_with_headers{ext}"
        new_filepath = os.path.join(folder, new_filename)

        # Write new file with header
        with open(new_filepath, "w") as f:
            f.write(headers)
            f.writelines(lines)

        print(f"Finished writing: {new_filename}")
        processed_count += 1

print("\nSummary:")
print(f"  Processed files: {processed_count}")
print(f"  Skipped files:   {skipped_count}")
