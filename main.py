import sys, csv
from convertor.temperature import covert_temperature
from convertor.distance import covert_distance

def write_file(name_file, data):
  with open(name_file, 'w') as file:
    fieldnames = [] 
    for key in data[0].keys():
        fieldnames.append(key)
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
    print('Output file written: ' + name_file)

if __name__ == '__main__':

  try:

    if len(sys.argv) == 4:   

      with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        list_data = list(reader)

      if len(list_data) > 0:

        if sys.argv[2].lower() == 'm':
          distTO = 'm'
          distFROM = 'ft'
        elif sys.argv[2].lower() == 'ft':
          distTO = 'ft'
          distFROM = 'm'

        if sys.argv[3].upper() == 'C':
          tempTO = '°C'
          tempFROM = '°F'
        elif sys.argv[3].upper() == 'F':
          tempTO = '°F'
          tempFROM = '°C'

        for row in list_data:
          if distFROM in row['Distance']:
            row['Distance'] = covert_distance(row['Distance'].replace(distFROM, ''), distTO)
          if tempFROM in row['Reading']:
            row['Reading'] = covert_temperature(row['Reading'].replace(tempFROM, ''), tempTO)

        write_file('result_file.csv', list_data)    

    else:
       raise NameError('Enter 4 parameters: program name, data-file name, m/ft, C/F')    

  except Exception as err:
    print(err)