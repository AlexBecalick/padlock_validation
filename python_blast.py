import os
import subprocess
from multiprocessing import Pool

# Function to run a BLAST query
def run_blast(input_file):
    try:
        refseq_dir = "/example/path/to/refseq_location"
        output_file = f"{os.path.splitext(input_file)[0]}_blast.out"
        blast_command = [
            "blastn",
            "-query", input_file,
            "-db", os.path.join(refseq_dir, "mouse.transcriptome"),
            "-outfmt", "10 std qseq sseq",
            "-out", output_file,
            "-word_size", "7",
            "-strand", "plus"
        ]
        subprocess.run(blast_command, check=True)
        print(f"Completed BLAST for {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run BLAST for {input_file}: {e}")
        raise

def main():
    # Read the list of FASTA files
    fasta_list_file = "/example/path/to/output_dir/fasta_list.txt"
    with open(fasta_list_file, "r") as f:
        fasta_files = [line.strip() for line in f if line.strip()]

    # Check if FASTA_LIST is set and not empty
    if not fasta_files:
        print("Fasta list is empty or doesn't exist. Exiting...")
        return

    # Use multiprocessing to run BLAST queries in parallel
    with Pool(processes=8) as pool:  # Adjust the number of processes as needed
        pool.map(run_blast, fasta_files)

if __name__ == "__main__":
    main()
