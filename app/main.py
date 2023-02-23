import utils
import charts
import read_csv

def run():
  data = read_csv.read_csv('./app/data.csv')
  data = list(filter(lambda item: item['NOMBRE DEL DDR'] == 'VALLE DE BRAVO', data))
  Municipio = list(map(lambda x: x['NOMBRE DEL MUNICIPIO'], data))
  Monto = list(map(lambda x: x['MONTO APOYADO'], data))
  charts.generate_pie_chart(Municipio, Monto)

if __name__ == '__main__':
  run()