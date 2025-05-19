#!/bin/bash
#SBATCH --job-name=ProjetLuca
#SBATCH --partition=dayCPU
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2GB
#SBATCH --time=00:15:00
#module load intel/intel.2025.0
#module load mpi/mpi.2021.14 
#module load mkl/mkl.2025.0
#module hdf5
#source /opt/intel/oneapi/setvars.sh

# Set CUDA_VISIBLE_DEVICES to the allocated GPU
#export CUDA_VISIBLE_DEVICES=0

# Run the CUDA application
#julia --project=. scripts/00-test-1D.jl


python3 script.py

