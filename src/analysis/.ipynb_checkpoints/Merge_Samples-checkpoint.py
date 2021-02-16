import scanpy as sc
import pandas as pd
import seaborn as sns

sc.settings.verbosity = 1             # verbosity: errors (0), warnings (1), info (2), hints (3)
sc.logging.print_versions()
sc.settings.set_figure_params(dpi=80, frameon=False, figsize=(3, 3), facecolor='white')

results_file = 'data/merged_preprocessed.h5ad'  # the file that will store the analysis results

adata1 = sc.read_10x_mtx(
    'data/matrixes/Rat11_1A/',# the directory with the `.mtx` file
    var_names='gene_symbols', # use gene symbols for the variable names (variables-axis index)
    cache=True)
adata2 = sc.read_10x_mtx('data/matrixes/Rat11_2A/',var_names='gene_symbols',cache=True)
adata3 = sc.read_10x_mtx('data/matrixes/Rat11_2B/',var_names='gene_symbols',cache=True)
adata4 = sc.read_10x_mtx('data/matrixes/Rat39_3A/',var_names='gene_symbols',cache=True)
adata5 = sc.read_10x_mtx('data/matrixes/Rat39_3B/',var_names='gene_symbols',cache=True)
adata6 = sc.read_10x_mtx('data/matrixes/Rat39_3C/',var_names='gene_symbols',cache=True)


adata = adata1.concatenate(adata2, adata3, adata4, adata5, adata6, index_unique=None) #Merge the data
adata.var_names_make_unique()#clean repeated gene
adata.obs_names_make_unique()
del adata1, adata2, adata3, adata4, adata5, adata6 #Clean

sc.pl.highest_expr_genes(adata, n_top=20, )
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=5)
adata.var['mt'] = adata.var_names.str.startswith('MT-')  # annotate the group of mitochondrial genes as 'mt'
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)


sc.pl.violin(adata, ['n_genes_by_counts', 'total_counts', 'pct_counts_mt'], jitter=0.4, multi_panel=True)
sc.pl.scatter(adata, x='total_counts', y='pct_counts_mt') #Cut under 10% mit
sc.pl.scatter(adata, x='total_counts', y='n_genes_by_counts') # cut under 5000 genes by counts

adata = adata[adata.obs.n_genes_by_counts < 5000, :]
adata = adata[adata.obs.pct_counts_mt < 5, :]
sc.pp.normalize_total(adata, target_sum=1e4)

sc.pp.log1p(adata) #log normalize data

sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
sc.pl.highly_variable_genes(adata)

#Set the .raw attribute of AnnData object to the normalized and logarithmized raw gene expression for
# later use in differential testing and visualizations of gene expression. This simply freezes the state
# of the AnnData object.
#You can get back an AnnData of the object in .raw by calling .raw.to_adata()
#If you don’t proceed below with correcting the data with sc.pp.regress_out and scaling it via sc.pp.scale,
# you can also get away without using .raw at all.
adata.raw = adata

#actually fikltering
adata = adata[:, adata.var.highly_variable]

sc.pp.regress_out(adata, ['total_counts', 'pct_counts_mt'])
sc.pp.scale(adata, max_value=10) #max std deviation =10

#PCA
sc.tl.pca(adata, svd_solver='arpack')
sc.pl.pca(adata,color='GNB1') # color and add marker name or var name for a feature plot like map
sc.pl.pca_variance_ratio(adata, log=True) #Select 10

adata.write(results_file) # save the file

