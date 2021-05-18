SCAnML
===
This project contains the analysis files for my thesis


Data preprocessing
=== 

Check the files to add the different necessary paths


Study reproducibility using a Singularity VM
===
Data avaiability
---

Singularity setup and usage
---
Contact me at [da4206hi-s@student.lu.se](da4206hi-s@student.lu.se) to share the singularity image used for the analysis.
### Installing singularity
The program runs natively on linux, in case you are a windows or MacOS user please follow their
 [installation](https://sylabs.io/guides/3.0/user-guide/installation.html#) guide.

Once installation was completed our VM was created in a sandbox form from a [definition](./src/Singularity/image.def) 
file using the [build_sandbox.sh](./src/Singularity/build_sandbox.sh). The sandbox image was then modified using the 
[Tinker_image.sh](./src/Singularity/tinker_image.sh) script and required programs and packages were installed. Once 
everything was installed the singularity image file (.sif) was built using the [build_sif.sh](./src/Singularity/build_sif.sh) 
script.

Once the singularity image was built it was moved to our data processing server, for you looking to use this image, take 
into account that the computer on which you wish to run your analyses needs to have singularity also installed.

Once everything was in the correct place we can launch our image using the 
[jupyter_service.sbatch](./src/Singularity/jupyter_service.sbatch) script, this is needed in our case since we are using
a [SLURM](https://slurm.schedmd.com/documentation.html) server, this script will launch a jupyter lab instance and will 
bind the local folder of choice to a /workspace folder located inside the singularity image. 
In our case we used the [open_server.sh](./src/Singularity/open_server.sh)
script. This script opens the .log file created by the process manager and extracts the URL to the created jupyter lab instance and opens it on the firefox browser.
An alternative to this is manually fetching the link to the jupyter lab instance and opening it on your desired browser.

### Analysis files descriptions
#### Preprocessing
In the case of our single cell dataset we got provided .fasta files that needed to be preperocessed into .mtx files for 
downstream analysis. This is performed using the scripts found in [preprocessign](./src/preprocessing). Take into account
that paths have been deleted. 
#### Analysis
The files under the [analysis folder](./src/analysis) contain the scripts used to perform all analyses and plotting.


# Once set up
Analysis description