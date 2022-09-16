base_name = "raw_data"
input_file = "data/"+base_name+".csv"
output_file = "data/"+base_name+"_new.csv"

feature_file = "data/direct_features.csv"

import csv 
import numpy as np 
from tqdm import tqdm 
nctid2feature = dict()


##### new features ####
with open(feature_file, newline = '') as csvfile:
	lines = list(csv.reader(csvfile, delimiter = ','))[1:]
default_value = []
for i in range(8):
	value_lst = [float(line[i+1]) for line in lines if line[i+1]!='']
	default_value.append(np.median(value_lst))
print(default_value)

for row in tqdm(lines):
	nctid = row[0]
	feature = row[1:]
	for idx,value in enumerate(feature):
		if value == '':
			feature[idx] = default_value[idx] 
		else:
			feature[idx] = float(feature[idx])	
	# feature = np.array(feature) ### np.arr 
	feature = [str(i) for i in feature]
	feature = '_'.join(feature)
	nctid2feature[nctid] = feature #### "2.0_1.0_1.0_18.0_65.0_55.0_1.0_60.0"

##### feature ##### 
# nctid,status,why_stop,label,phase,diseases,icdcodes,drugs,smiless,criteria 
with open(input_file, newline = '') as csvfile:
	lines = list(csv.reader(csvfile, delimiter = ','))
	header = lines[0]
	lines = lines[1:]
print(header)

for line in lines: 
	nctid = line[0] 
	feature = nctid2feature[nctid]
	line.append(feature)



##### write csv ##### 
with open(output_file, 'w') as csvfile:
	writer = csv.writer(csvfile)
	header.append('additional_feature')
	writer.writerow(header)
	for line in lines:
		writer.writerow(line) 


