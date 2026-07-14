import pickle
with open('sample.pkl','rb') as f:
    load_num=pickle.load(f)
    print(load_num)
