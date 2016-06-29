import numpy as np
import matplotlib.pyplot as plt



def graph_plot(x,y,title,xlabel,ylabel,fname):
	plt.figure(figsize=(20,6),facecolor='w')
	plt.grid(True)
	plt.plot(x,y)
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.savefig(fname,bbox_inches='tight')
	plt.close()

def load_csv(fname):
	time = []
	util = []
	with open(fname,"r") as f:
		for line in f:
			line=line.split(',')
			time.append(float(line[0]))
			util.append(float(line[2]))
		return [time,util]	
	
		
if __name__=="__main__":
	
	#fnames=["LJF/hostTotalUtil_LJF.csv","FirstFit/hostTotalUtil_FirstFit.csv","BestFit/hostTotalUtil_BestFit.csv","BalancedFit/hostTotalUtil_BalancedFit.csv"]
	#algo=["LJF","First Fit","Best Fit","Balanced Fit"]
	#save_name=["LJF_Ram","BestFit_Ram","FirstFit_Ram","BalancedFit_Ram"]	
	fnames=["SubsetFit/10L/hostTotalUtil.csv"]
	algo=["SubsetFit"]
	save_name=["SubsetFit"]
	for ind in range(len(fnames)):
		fname="/home/dhvanan/IISc/Utilization/"+fnames[ind]
		time,util=load_csv(fname)
		graph_plot(time,util,"Ram Util -"+algo[ind],"TimeStamp","Ram Utilization",save_name[ind	])