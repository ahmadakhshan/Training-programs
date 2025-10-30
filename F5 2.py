import csv 
import statistics
with open('b.CSV') as f:
    r=csv.reader(f)
    for i in r:
        name=i[0]
        nomre=[]
        for z in i[1:]:
            nomre.append(int(z))
        moadel=statistics.mean(nomre)
        print('nore %s shode %f'%(name,moadel))
        