#!/bin/bash
#SBATCH --account=def-jlalonde # Sponsor account
#SBATCH --nodes=1 # Number of node
#SBATCH --gres=gpu:1 # GPU type and number per node
#SBATCH --cpus-per-task=6 # Number of core per node
#SBATCH --mem=32000M # Memory per node
#SBATCH --time=1-00:00 # Running time (DD-HH:MM)
#SBATCH --output=1195_floor_02_complete_room_01_partial_room_10_pano_50_layout.out

module load cudacore/.11.7.0
nohup  python run_nerf.py --config /root/codes/360FusionNeRF/configs/1195_floor_02_complete_room_01_partial_room_10_pano_50_layout.txt