import pandas as pd
import glob
import os

# Input/output
input_dir = "/Users/chrisaxline/Desktop/Serotyping/PASP_serotype_blast_results/PASP_with_headers" 
output_csv = "/Users/chrisaxline/Desktop/Serotyping/PASP_serotype_blast_results/PASP_with_headers/PASP_hits.csv"

# Collect results
all_best_hits = []

# Iterate through files
for file in glob.glob(os.path.join(input_dir, "*.txt")) + \
            glob.glob(os.path.join(input_dir, "*.out")) + \
            glob.glob(os.path.join(input_dir, "*.tsv")):
    
    print(f"Processing: {os.path.basename(file)}")
    fname = os.path.basename(file)
    try:
        # Read BLAST outfmt 6 with headers
        df = pd.read_csv(file, sep="\t", dtype=str)  # read as strings
    except Exception as e:
        print(f"⚠️ Skipping {file}: could not read ({e})")
        continue
    
    if "bitscore" not in df.columns or df.empty:
        print(f"⚠️ Skipping {file}: no valid bitscore column")
        continue
    
    # Convert numeric columns
    numeric_cols = ["pident","length","mismatch","gapopen",
                    "qstart","qend","sstart","send",
                    "evalue","bitscore"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    
    # Drop rows without bitscore
    df = df.dropna(subset=["bitscore"])
    if df.empty:
        print(f"⚠️ Skipping {file}: all bitscore values missing")
        continue
    
    # Get row(s) with max bitscore
    max_bitscore = df["bitscore"].max()
    best_hits = df[df["bitscore"] == max_bitscore].copy()
    
    # Add filename column and strain name
    best_hits["file"] = os.path.basename(file)
    best_hits["Strain"] = fname.split("_",1)[0]
    all_best_hits.append(best_hits)

# Combine all results
if all_best_hits:
    result_df = pd.concat(all_best_hits, ignore_index=True)
    result_df.to_csv(output_csv, index=False)
    print(f"✅ Done! Results saved to {output_csv}")
else:
    print("⚠️ No results found.")
