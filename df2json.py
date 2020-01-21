DATA = []
for i in range(icd_file.shape[0]):
    row_data = icd_file.iloc[i]
    data_dict = {}
    for name in list(icd_file.columns):
        data_dict.update({name:str(row_data[name])})
    DATA.append(data_dict)
