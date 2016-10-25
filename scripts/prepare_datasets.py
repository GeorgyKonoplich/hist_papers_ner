import os
import zipfile
from sklearn.cross_validation import KFold
import numpy as np

def list_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory)]


def read_zip_file(filepath):
    zfile = zipfile.ZipFile(filepath)
    combined_file = open("../datasets/processed/combined_data.bio", 'w+')
    for finfo in zfile.infolist():
        ifile = zfile.open(finfo)
        line_list = ifile.readlines()
        combined_file.writelines(line_list)

read_zip_file("../datasets/raw/eunews_nl.bio.zip")
all_data = open("../datasets/processed/combined_data.bio", 'r')

data = all_data.readlines()
data = np.array(data)
kf = KFold(len(data), n_folds=4)
count = 0

for train_index, test_index in kf:
    print("Prepare train and test sets #%d" % (count + 1))
    data_train, data_test = data[train_index], data[test_index]
    count = count + 1
    ftrain = open("../datasets/processed/data_train" + str(count) + ".bio", 'w+')
    ftest = open("../datasets/processed/data_test" + str(count) + ".bio", 'w+')
    ftrain.writelines(data_train)
    ftest.writelines(data_test)
    ftrain.close()
    ftest.close()


