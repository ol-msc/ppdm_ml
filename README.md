# Applied Research on Privacy preserving and Data mining techniques

### Last update: 20.06.2021

This is a link for instalation tutorial for Syft 0.2.9 which 
actually is deprecated by the time of writing , but still installation steps are the same. 
https://blog.openmined.org/how-to-setup-pysyft-on-windows-10/

## For Windows users:

Enable WSL in you system and install Ubuntu distro 
from Windows store. 

## Configuring environment for runnig the project

### 1. Anaconda setup
- **Dowload Anaconda distro**
    > $ cd $HOME \
    > $ wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh

    *also you can dowload latest version of anaconda*
- **Install Anaconda**\
    Run the installation process with next commands:  
    > $ chmod +x Anaconda3-2021.05-Linux-x86_64.sh \
    > $ ./Anaconda3-2021.05-Linux-x86_64.sh

    Follow the installation instruction

    Once the installation procedure completes, we just need to close the Ubuntu subsystem and re-open it, or run the following command to activate conda:

    > $ source ~/.bashrc

    To test installation run following commant to view available environments. By default, just the base environment is available:
     
    > $ conda info --envs

- **Create Conda env** \
    Create conda envronment with following command:

    > $ conda create --name pysyft python=3.8.8

    *for now __python 3.9__ and later is not supported by develpoers of PySyft, hope the will fix this*

    Activate the environment
    > $ conda activate pysyft

    Althou pip should be installed, but to be sure run the nex command:

    > $ pip --version

### 2. Install  PySyft and other libraries
- **Install PySyft**

    To install PySyft run the following command:

    > $ pip install syft==0.5.0rc1

    git: https://github.com/OpenMined/PySyft

    However to install the next libraries you need to install PySyft in eather way.

- **Install PyDP**
    To install PyDP run the following command:
    >  $ pip install python-dp

    git: https://github.com/OpenMined/PyDP

- **Install TenSeal**
    To install TenSeal run the following command:
    >  $ pip install tenseal
    
    git: https://github.com/OpenMined/TenSEAL

- **Install SyMPC**
    To install SyMPC run the following command:

    > $ pip install git+https://github.com/OpenMined/SyMPC@0.5.0

    Experiments with SyMPC should work with 0.5.0rc1 version of Syft, and exactly 1.8.0 version of torch (got an error with 1.8.1 version of torch)





