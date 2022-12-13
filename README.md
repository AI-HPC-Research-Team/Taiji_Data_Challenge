# Taiji Data Challenge for Exploring Gravitational Wave Universe
![Taiji|300](images/tj-small-white-logo.png)

This is the official Taiji Data Challenge code repository for data generation.

## Introduction
Taiji is a proposed detection mission for gravitational waves that will be launched in the 2030s. Due to the overlapping sources and instrumental configurations, analyzing Taiji's data is difficult. With Taiji Data Challenge, we hope to create a community of researchers who can contribute collaboratively to the development of Taiji's data analysis pipelines and join the Taiji Scientific Collaboration's journey of exploring the universe, which will aid in achieving the scientific goals for space-based GW detections.

## Getting Started
1. Clone the repo
	```
	git clone https://github.com/AI-HPC-Research-Team/taiji_data_challenge.git
	cd taiji_data_challenge
	```

2. Setup the conda environment:
	```
	conda create -n taiji -c conda-forge gcc_linux-64 gxx_linux-64 wget gsl fftw lapack=3.6.1 hdf5 numpy Cython scipy jupyter ipython  matplotlib python=3.7 --yes
	conda activate taiji
	```
3. Install all dependencies:
	```
	bash install.sh
	```
## Reference
- [FastEMRIWaveforms](https://github.com/BlackHolePerturbationToolkit/FastEMRIWaveforms)
-  [lisa-on-gpu](https://github.com/mikekatz04/lisa-on-gpu)
-  [LISA Verification Binaries](https://gitlab.in2p3.fr/LISA/lisa-verification-binaries)
-  [LDC-tutorial](https://github.com/mikekatz04/LDC-waveform-generation-tutorial)


