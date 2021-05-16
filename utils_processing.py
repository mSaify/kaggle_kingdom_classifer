import numpy as np
import pandas as pd


def get_kingdom_dict():

    kingdom=dict()

    with open('kingdom_lookup.txt') as f:
        val = f.readlines()

        for v in val:

            key_pair = v.split(',')
            val= str(key_pair[0].strip())
            key = float(key_pair[1].strip())

            kingdom[val]=key

    return kingdom


def convert_kingdom_to_float(label):

    kingdom = get_kingdom_dict()

    for i,val in enumerate(label.values):
        if val[0] in kingdom:
            val[0] = kingdom[val[0]]

    return label

def convert_and_label_to_float_and_store_back(dataset,filename):

    if "Kingdom" in dataset:

        label = convert_kingdom_to_float(dataset[['Kingdom']])
        label = label.rename(columns={'Kingdom': 'Kingdom_float'})
        df = pd.concat([pd.DataFrame(dataset), pd.DataFrame(label)], axis=1)

        print(df)

        df.to_csv(filename, index=False)



def convert_preds_float_to_str(preds):

    kingdom = get_kingdom_dict()
    rev_kingdom_dic =dict()

    for k,v in kingdom.items():

        rev_kingdom_dic[v]=k

    print(preds.shape)
    new_preds = np.empty(preds.shape,dtype=object)

    print(new_preds.size)

    for i, val in enumerate(preds):
        if val in rev_kingdom_dic:
            new_preds[i] = rev_kingdom_dic[val]

    print(new_preds)

    return new_preds

if  __name__ == "__main__":

    #convert classification string values to floats

    dataset = pd.read_csv("Train.csv")

    convert_and_label_to_float_and_store_back(dataset,"new_train.csv")