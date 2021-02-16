import scarches as sca
import scanpy as sc


data = sc.read_h5ad("./data/publishedData/NatureCom.h5ad")
sc.pl.umap(data, color=['CelltypeI'])
condition_key = 'CelltypeI'


network = sca.models.scArches(task_name='SC_VM', # create the network and tell it wich data to get
                              x_dimension=data.shape[1],
                              z_dimension=10,
                              architecture=[128, 128],
                              gene_names=data.var_names.tolist(),
                              conditions=data.obs[condition_key].unique().tolist(),
                              alpha=0.001,
                              loss_fn='nb',
                              model_path="./models/scArches_cells_1/",
                              )

network.train(data, # train the model
              condition_key=condition_key,
              n_epochs=30,
              batch_size=128,
              save=True,
              retrain=True)

latent_adata = network.get_latent(adata, condition_key)

sc.pp.neighbors(latent_adata)
sc.tl.umap(latent_adata)
sc.pl.umap(latent_adata, color=[condition_key, "cell_type"],
           frameon=False, wspace=0.6)




# oroject query data on referenece data
new_network = sca.operate(network,
                          new_task_name="Neu_query",
                          new_conditions=target_conditions)