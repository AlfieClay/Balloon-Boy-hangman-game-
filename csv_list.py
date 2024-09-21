def csv_list(file):
    csv_file=open(file)
    csv_list=[]
    for item in csv_file:
        csv_list.append(item)
    return csv_list
