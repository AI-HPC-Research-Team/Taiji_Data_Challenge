#!/bin/bash

# python -m pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ --upgrade pip
# pip config set global.index-url https://pypi.mirrors.ustc.edu.cn/simple/ 

pip install bidict bezier
pip install cupy-cuda114
pip install tqdm h5py requests astropy h5py lisaconstants xarray

# EMRI Waveform
git clone https://github.com/BlackHolePerturbationToolkit/FastEMRIWaveforms.git 
cd FastEMRIWaveforms 
python setup.py install 
cd ../
# Detector response and TDI
git clone https://github.com/mikekatz04/lisa-on-gpu.git
cd lisa-on-gpu
python setup.py install
cd ../
# LDC code
git clone https://gitlab.in2p3.fr/LISA/LDC
cd LDC
python setup.py install --with-fastAK --with-fastGB --with-imrphenomD