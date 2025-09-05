# Pseudomonas_Serotyping_Pipeline
series of scripts to assign O-antigen serotypes to isolates of Pseudomonas aeruginosa

# Steps
1.) Run blast_run.sh via terminal
  Run these commands in the terminal:
    chmod +x blast_run.sh
    ./blast_run.sh
2.) Add headers to outfmt6 files from BLAST search
  Run adding_headers_outfmt6.py
    **make sure to change file directories
3.) Run move_headers.py to create a cleaner output
4.) Run serotyping_hits.py to create clean output file with serotype for each strain/sequence

# Disclaimers:
  - OSAdb from https://github.com/Sandramses/PAst (DOI:) 
