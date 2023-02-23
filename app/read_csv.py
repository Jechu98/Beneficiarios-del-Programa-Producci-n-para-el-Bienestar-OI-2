import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      prog_bienestar = {key:value for key, value in iterable}
      data.append(prog_bienestar)
    return data

if __name__ == '__main__':
  read_csv()  
