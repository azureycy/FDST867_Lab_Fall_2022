#!/bin/sh
#SBATCH --time=7-00:00:00
#SBATCH --mem=50gb
#SBATCH --job-name=dbcan
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=10
#SBATCH --error=/work/yourgroup/yourusername/job.%J.err
#SBATCH --output=/work/yourgroup/yourusername/job.%J.out
#SBATCH --partition=batch,tmp_anvil,guest

# module load anaconda and activate run_dbcan

ml anaconda
conda activate run_dbcan

# create dbcan output folder
mkdir dbcan_out

# run dbCAN for the 44 genomes

for i in ../44_origin_faa_gff/*faa;
do s=${i##*/};
run_dbcan $i protein -c ${i%.*}.gff --out_dir dbcan_out/${s%.*} --db_dir db;
done

