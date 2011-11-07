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

    equiplistload('airside.csv')
    pointlistload('ahupointlist.csv')