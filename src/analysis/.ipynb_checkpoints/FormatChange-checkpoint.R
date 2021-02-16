

library(Seurat)
if (!requireNamespace("remotes", quietly = TRUE)) {
  install.packages("remotes")
}
remotes::install_github("mojaveazure/seurat-disk")
library(SeuratDisk)

data <- readRDS("../../data/publishedData/NatureComdata.rds")

data <- UpdateSeuratObject(data)#update the data
SaveH5Seurat(data, filename = "../../data/publishedData/NatureCom.h5Seurat")#write it
Convert("../../data/publishedData/NatureCom.h5Seurat", dest = "h5ad")#transform it



