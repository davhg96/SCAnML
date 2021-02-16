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