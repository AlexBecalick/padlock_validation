#!/bin/bash
#SBATCH --job-name=par_blast_queries
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=1:00:00
#SBATCH --mem=16G
#SBATCH --partition=ncpu

# Exit on any error
set -e

# Load modules
module purge
module load Anaconda3
module load BLAST+

# Activate conda environment
source /camp/apps/eb/software/Anaconda/conda.env.sh
conda activate iss-preprocess || { echo "Failed to activate conda environment"; exit 1; }

# Navigate to working directory
cd /example/path/to/padlock_validation || { echo "Failed to change directory"; exit 1; }

# Set directory variables
FASTA_LIST=/example/path/to/output_dir/fasta_list.txt

# Check if FASTA_LIST is set and not empty
if [ -z "$FASTA_LIST" ]; then
  echo "FASTA_LIST variable is not set or empty"
  exit 1
fi

# Launch jobs for each FASTA file in the list
cat "$FASTA_LIST" | while read -r line
do
   echo "Launching job for ${line}"
   sbatch --export=INPUT="${line}" blast_query.sh || { echo "Failed to submit job for ${line}"; exit 1; }
done
