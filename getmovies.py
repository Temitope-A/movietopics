def fill_from_dir(raw_list, path):
    import os

    names=os.listdir(path)
    for name in names:
        v1=name.split('(')
        v2=v1[0].split('[')
        v3=v2[0].replace('.',' ')
        raw_list.append(v3)
        
def fill_from_file(raw_list, path):

    f=open(path,'r')
    for line in f:
        data=line.rstrip().split(',')
        n=len(data)
        for i in range (0,n):
            data[i]=data[i].strip()
        raw_list.append(data)
    f.close()
