import scanpy as sc
import pandas as pd
import seaborn as sns

sc.settings.verbosity = 1             # verbosity: errors (0), warnings (1), info (2), hints (3)
sc.logging.print_versions()
sc.settings.set_figure_params(dpi=80, frameon=False, figsize=(3, 3), facecolor='white')

results_file = 'data/merged_preprocessed.h5ad'  # the file that will store the analysis results

adata = sc.read('data/merged_preprocessed.h5ad')

sc.pp.neighbors(adata)

sc.tl.umap(adata)
sc.pl.umap(adata, color=['batch']) #Nice integration

sc.tl.leiden(adata, resolution=0.3)
sc.pl.umap(adata, color=['leiden', 'batch'])

sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False)

adata.write(results_file)
