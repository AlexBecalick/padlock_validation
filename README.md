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

To test your padlocks, provide a .csv file with the column format:
["target", "gene_name", "padlock_name"]
Where target is the sequence of the padlock arms in the order they bind to the gene, gene_name is the gene acroynm as annotated in your refseq acronym file and padlock name is any unique name you want to call each padlock.

Use padlocks_to_fasta.ipynb to generate a folder full of fasta files per gene. Then run parallel_blast_query.sh to start blast jobs for each gene's padlocks. Finally, use read_blast_queries.ipynb to collate this output for all padlocks and filter it to find relevant non-specific hits.
