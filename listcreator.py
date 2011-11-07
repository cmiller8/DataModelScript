__author__ = 'claytonmiller'

import csv

def equiplistload(elcsv):

    """
    Loads the equip list csv according to the type
    """
    with open(elcsv, 'rb') as f:
        reader = csv.reader(f)

        equiplist = []
        for line in reader:
            equiplist.append(tuple(line))

#        for equip in equiplist:
#            print equip

    return equiplist

def pointlistload(plcsv):
        with open(plcsv, 'rb') as f:
            reader = csv.reader(f)

            pointlist = []
            for line in reader:
                pointlist.append(tuple(line))

#            for point in pointlist:
#                print point

            return pointlist



if __name__ == '__main__':

    equiplist = equiplistload('airside.csv')
    ahutemplate = pointlistload('ahupointtemplate.csv')

    totalpointlist = []

    for equip in equiplist:
        if equip[2]=='ahu':
            for templatepoint in ahutemplate:
                pointname = equip[0]+' '+equip[1]+' '+templatepoint[0]
                totalpointlist.append(pointname)

    f = open('results.txt','w')
    for point in totalpointlist:
        print point
        f.write(point+'\n')
        

    
