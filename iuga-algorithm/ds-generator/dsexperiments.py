import csv
def rangeAmmount(filename):
    similarity = [0,0,0,0,0,0,0,0,0,0]
    distance = [0,0,0,0,0,0,0,0,0,0]
    rowammount = 0
    arquivos = []
    for val in range(0, 10):
        strfile = 'dspoints/' + str(val) + '_' + str(val+1)
        arquivos.append(csv.writer(open(strfile, 'wb')))
        arquivos[val].writerow(['p1', 'p2', 'distance', 'similarity'])
    with open(filename) as f1:
        for row in csv.reader(iter(f1.readline, '')):
            row[2] = float(row[2])
            row[3] = float(row[3])
            rowammount += 1
            if((row[2] >= 0.0) and (row[2] < 0.1)):
                distance[0] += 1
            elif((row[2] >= 0.1) and (row[2] < 0.2)):
                distance[1] += 1
            elif((row[2] >= 0.2) and (row[2] < 0.3)):
                distance[2] += 1
            elif((row[2] >= 0.3) and (row[2] < 0.4)):
                distance[3] += 1
            elif((row[2] >= 0.4) and (row[2] < 0.5)):
                distance[4] += 1
            elif((row[2] >= 0.5) and (row[2] < 0.6)):
                distance[5] += 1
            elif((row[2] >= 0.6) and (row[2] < 0.7)):
                distance[6] += 1
            elif((row[2] >= 0.7) and (row[2] < 0.8)):
                distance[7] += 1
            elif((row[2] >= 0.8) and (row[2] < 0.9)):
                distance[8] += 1
            elif((row[2] >= 0.9) and (row[2] <= 1)):
                distance[9] += 1


            if((row[3] >= 0.0) and (row[3] < 0.1)):
                similarity[0] += 1
                arquivos[0].writerow([row[0],row[1], row[2], row[3]])
            elif((row[3] >= 0.1) and (row[3] < 0.2)):
                similarity[1] += 1
                arquivos[1].writerow([row[0],row[1], row[2], row[3]])
            elif((row[3] >= 0.2) and (row[3] < 0.3)):
                similarity[2] += 1
                arquivos[2].writerow([row[0],row[1], row[2], row[3]])
            elif((row[3] >= 0.3) and (row[3] < 0.4)):
                similarity[3] += 1
                arquivos[3].writerow([row[0],row[1], row[2], row[3]])
            elif((row[3] >= 0.4) and (row[3] < 0.5)):
                similarity[4] += 1
                arquivos[4].writerow([row[0],row[1], row[2], row[3]])
            elif((row[3] >= 0.5) and (row[3] < 0.6)):
                similarity[5] += 1
                arquivos[5].writerow([row[0],row[1], row[2], row[3]])
            elif((row[3] >= 0.6) and (row[3] < 0.7)):
                similarity[6] += 1
                arquivos[6].writerow([row[0],row[1], row[2], row[3]])
            elif((row[3] >= 0.7) and (row[3] < 0.8)):
                similarity[7] += 1
                arquivos[7].writerow([row[0],row[1], row[2], row[3]])
            elif((row[3] >= 0.8) and (row[3] < 0.9)):
                similarity[8] += 1
                arquivos[8].writerow([row[0],row[1], row[2], row[3]])
            elif((row[3] >= 0.9) and (row[3] <= 1)):
                similarity[9] += 1
                arquivos[9].writerow([row[0],row[1], row[2], row[3]])
    print("Distance: \n")
    for indice, x in enumerate(distance):
        output = str(float(indice)/10) + " ~ " + str((float(indice)/10) + 0.1) + ": " + str(x)
        print(output)

    print("\nSimilarity: \n")
    for indice, x in enumerate(similarity):
        output = str(float(indice)/10) + " ~ " + str((float(indice)/10) + 0.1) + ": " + str(x)
        print(output)


        #Write the result in dscount.csv
    dscount = csv.writer(open("dscount.csv", "wb"))
    dscount.writerow(['Value','All', '0.0 ~ 0.1','0.1 ~ 0.2','0.2 ~ 0.3', '0.3 ~ 0.4', '0.4 ~ 0.5', '0.5 ~ 0.6', '0.6 ~ 0.7','0.7 ~ 0.8','0.8 ~ 0.9','0.9 ~ 1.0'])
    dscount.writerow(['Similarity',rowammount, similarity[0], similarity[1], similarity[2], similarity[3], similarity[4], similarity[5], similarity[6], similarity[7], similarity[8], similarity[9]])
    dscount.writerow(['Distance',rowammount, distance[0], distance[1], distance[2], distance[3], distance[4], distance[5], distance[6], distance[7], distance[8], distance[9]])
    print("Information about all point is locate in dscount.csv\n\nInside dspoints folder have 10 files, each to 0.1 range")






rangeAmmount('ds.csv')
