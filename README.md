# Taiji Data Challenge
---
![Taiji|500](images/tj-small-white-logo.png)
This is the official Taiji Data Challenge code repository for data generation.

## Getting Started
1. Clone the repo
	```
	git clone https://github.com/AI-HPC-Research-Team/taiji_data_challenge.git
	cd taiji_data_challenge
	```

2. Setup the environment:
	```
	conda create -n taiji_env -c conda-forge gcc_linux-64 gxx_linux-64 wget gsl fftw lapack=3.6.1 hdf5 numpy Cython scipy jupyter ipython  matplotlib python=3.7 --yes
	conda activate taiji_env
	```
4. To run install:
	```
	bash setup.sh
	```
## Reference
- [FastEMRIWaveforms](https://github.com/BlackHolePerturbationToolkit/FastEMRIWaveforms)
-  [lisa-on-gpu](https://github.com/mikekatz04/lisa-on-gpu)
-  https://gitlab.in2p3.fr/LISA/lisa-verification-binaries
-  [LDC-tutorial](https://github.com/mikekatz04/LDC-waveform-generation-tutorial)


