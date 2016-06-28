count_algo = {0:0,1:0,2:0}
val_algo = {0:0,1:0,2:0}
with open("/home/dhvanan/IISc/Utilization/count_no_occurances.csv","r") as f:
	for d in f:
		d = [float(i) for i in d.split(',')]
		ind = d.index(max(d))
		count_algo[ind]+=1
		for j in range(len(d)):
			val_algo[j]+=d[j]	
print count_algo
print val_algo
