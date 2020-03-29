import pandas as pd

#dict1 = {"Time": [], "IN": [], "FN": [], "Cured/Di/M": [] ,"Dead":[], '"Total"': [] }
dict1 = {"Time": [], "Confirmed": [], "Cured/Di/M": [] ,"Dead":[], '"Total"': [] }
data = pd.DataFrame(dict1, index = None)
print(data.head)
#data.to_csv("enter_name_here.csv", index = False)