import sys
filep = sys.argv[1]

print(filep.split('/')[-1])

if not filep.split('/')[-1] in ['Dmitry_Table.html', 'Dmitry_Shop.html']:
    file = open(filep, mode='r', encoding='UTF-8')
    data = file.read().replace('\n', '').replace('\t', '').replace(' ', '')
    file.close()
    file = open(filep, mode='w', encoding='UTF-8')
    file.write(data)
    file.close()
