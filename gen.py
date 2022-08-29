from random import gauss

file = open ('gen.txt','r')
buf = file.readline()
a,b = buf.split('\t')
# модель полива с измерением раз в 15 мин
emodel_water = [float(a)]*1
# модель шторки с измерением раз в 15 мин
emodel_shutter = [float(b)]*1


# for name in name_protocol:
data = []
for i in range(1):
    comb = (abs(gauss(emodel_water[i], 2)), abs(gauss(
        emodel_shutter[i], 3)))
    data.append(comb)

with open('gen.txt', 'w') as fw:
    # записываем
    for i in range(1):
        fw.write(f'{data[i][0]}\t{data[i][1]}\n')