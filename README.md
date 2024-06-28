# Padlock validation
Code for checking padlock specificity

## Installation
First, clone the repository:
```
git clone https://github.com/AlexBecalick/padlock_validation.git
```

Next, navigate to the repo directory and create a conda environment and install dependencies by running:
```
conda create --name padlock-validation python
```

Finally, activate the new environment and install the package itself:
```
conda activate padlock-validation
pip install -e .
```

You'll need to also:
+ Install blast+, add to path
+ Install clustalW, add to path
+ Follow the instructions from https://github.com/Moldia/multi_padlock_design to download and setup refseq mouse / human mRNA sequences from ftp.ncbi.nlm.nih.gov (run probedesign.py to perform initial setup)

To test your padlocks, provide a .csv file with the column format:
["target", "gene_name", "padlock_name"]
Where target is the sequence of the padlock arms in the order they bind to the gene, gene_name is the gene acroynm as annotated in your refseq acronym file and padlock name is any unique name you want to call each padlock.

Use padlocks_to_fasta.ipynb to generate a folder full of fasta files per gene. 

If you are running on a slurm cluster then run parallel_blast_query.sh to start blast jobs for each gene's padlocks.
Otherwise use python_blast.py to run the blast locally (currently untested).

 Finally, use read_blast_queries.ipynb to collate the blast output for all padlocks and filter it to find relevant non-specific hits.
