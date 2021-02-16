library(Seurat)
library(SeuratDisk)
data1 <- Read10X(data.dir = "./data/matrixes/mtxmultispecies/rat11_1a")
data1 <- CreateSeuratObject(counts = data1, project = "rat11_1a")
data2 <- Read10X(data.dir = "./data/matrixes/mtxmultispecies/rat11_2a")
data3 <- Read10X(data.dir = "./data/matrixes/mtxmultispecies/rat11_2b")
data4 <- Read10X(data.dir = "./data/matrixes/mtxmultispecies/rat39_3a_1a")
data5 <- Read10X(data.dir = "./data/matrixes/mtxmultispecies/rat39_3b")
data6 <- Read10X(data.dir = "./data/matrixes/mtxmultispecies/rat39_3c")

samples <- c(data2,data3,data4,data5,data6)


alldata <- merge

list.files("./data/matrixes/mtxmultispecies/rat11_1a")

mA <- alldata$`rat39_3a`
mC <- alldata$`rat39_3c`
both <- intersect(colnames(mA),colnames(mC))
mBoth <- mA[,both] + mC[,both]
colnames(mBoth) <- both
# add unique entries.
uniqueA <- setdiff(colnames(mA),both)
mBoth <- cbind(mBoth,mA[,uniqueA])
uniqueC <- setdiff(colnames(mC),both)
mBoth <- cbind(mBoth,mC[,uniqueC])
alldata[["rat39_3ac"]] <- mBoth
alldata$`rat39_3a` <- NULL
alldata$`rat39_3c` <- NULL
unlist(lapply(alldata, ncol))
##  rat45_1a  rat45_1b  rat11_1a  rat11_2a  rat11_2b  rat39_3b rat39_3ac 
##      3496      2732       752       470       443      1292      1304



ata <- UpdateSeuratObject(data)#update the data
SaveH5Seurat(data, filename = "../../data/publishedData/NatureCom.h5Seurat")#write it
Convert("../../data/publishedData/NatureCom.h5Seurat", dest = "h5ad")#transform it