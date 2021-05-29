

Single cell and single nuclei dataset analysis.
===
Parkinson’s disease (PD) is the most common neurodegenerative disorder, characterized by slow progressive loss of 
dopamine (DA) neurons in midbrain. Although the relatively focal degeneration in PD makes it a good candidate for 
cell-based therapies, obtaining cell source on large scale clinical application remains a challenge. It has now been 
shown that functional dopamine neurons can be generated using stem cells and these cells are both safe and functional 
when transplanted in animal models of Parkinson’s disease. Intensive research efforts have been made in recent years to 
understand the molecular mechanisms controlling the developmental program and differentiation of DA neurons using 
advanced technologies like single cell RNA sequencing. Transcriptional profiling of these cells will provide a complete 
cellular composition of human midbrain. It will also help in determining the diversity of dopaminergic neurons, which is
so far largely unknown due to the absence of molecular markers. Altogether these findings will help us understanding 
cell identity and molecular mechanisms underlying cell fate decisions of ventral midbrain neuron sub type during stem 
cell differentiation. However, fast paced growth in generation of these datasets also requires better optimization and 
development of bioinformatics algorithms. 

Here in this thesis, we focus on analyzing and integrating single cell and single nuclei datasets obtained from grafted 
cells obtained after different time points of transplantation in rat model of PD. We developed a machine learning based 
model to integrate these large-scale datasets, which can be further trained and easily distributed and replicated to other 
similar studies in the field.

Please note that code for the other subprojects in this thesis can be found on different repositories:
- [Analysis of long non coding and non coding genes](https://github.com/davhg96/SC_lncRNA.git)
- [Serotoninergic progenitor analysis](https://github.com/davhg96/SerotinergicProgenitors.git)


Host cell population analysis and label transfer using a machine learning approach.
===
Data availability
---
For data availability please refer to the next references:
- [Analysis of long non coding and non coding genes](https://doi.org/10.3390/cells10010137)
- [Serotoninergic progenitor analysis](https://doi.org/10.1101/2020.10.01.322495)
- [Host cell analysis](https://doi.org/10.1038/s41467-020-16225-5)
- Single Nuclei data: Data not available.


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
In the case of our single cell dataset we got provided .fastq files that needed to be preprocessed into .mtx files for 
downstream analysis. This is performed using the scripts found in [preprocessing](./src/preprocessing). Take into account
that paths have been deleted. 
#### Analysis
The files under the [analysis folder](./src/analysis) contain the scripts used to perform all analyses and plotting.
Due to a mistake during library preparation prior sequencing, the sample was split ans sequenced separately, to fix this
the [merge](./src/analysis/merge.ipynb) script was built. This script opens the affected samples and adds the counts from 
both count files by their barcodes.

Once the sequencing error was solved we proceeded to perform the different analyses on our datasets:
- [Single cell dataset analysis](./src/analysis/PP_QC_Cluster_RAT_SC.ipynb): Contains the code used to preprocess, quality
control and cluster our single cell dataset, as well as related plots. This script also saves a copies of the analysis object 
in .h5ad format both after complete analysis containing all different annotations (multispecies_RATclust.h5ad) and a 
preprocessed file containing only cell type and sample annotations (multispecies_RATpp.h5ad).
- [Single nuclei dataset analysis](./src/analysis/PP_QC_Cluster_RAT_SN.ipynb): Contains the code used to preprocess, quality
control and cluster our single nuclei dataset, as well as related plots.This script also saves a copies of the analysis object 
in .h5ad format both after complete analysis containing all different annotations (multispecies_RAT_SN_clust.h5ad) and a 
preprocessed file containing only cell type and sample annotations (multispecies_RAT_SN_pp.h5ad).

Once the datasets were analysed we proceeded to perform the machine learning analyses and model creation, in all cases
neuronal subtypes found on single nuclei data were labeled as neurons, so they were comparable to single cell data:
- [Technology based learning](./src/analysis/celltypes_SCSN_autoenc.ipynb): Was used to build a model based on the sequence
 technology used. Single cell is used to pre train our model and predict cell types on single nuclei data. This script 
 was used twice, the first time with 300 surgery epochs and the second with 600, both with diminishing results in accuracy.
- [Sample based learning](./src/analysis/celltypes_SCSN_sample_separated.ipynb): Was used to build a model based on the 
 sample tags. Single cell data is used to pre train our model providing the sample annotations as a source of variability.
- [Combined technology sample based learning](./src/analysis/celltypes_SCSN_sample_combined_training.ipynb): Was used
 to build a model based on the sample labels but in this cases samples from both sequencing technologies were provided for 
 pre training. This model was the best performer in accuracy and integration.
- [Supplementary plotting](./src/analysis/combined%20plotting.ipynb): Contains the code used to produce extra plots outside 
standard workflows.
  
