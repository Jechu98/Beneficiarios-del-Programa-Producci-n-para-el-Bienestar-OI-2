def get_municipio(data):
  result = {item['NOMBRE DEL MUNICIPIO']:item['CULTIVO'] for item in data}
  municipio = result.keys()
  cultivo =  result.values()
  return municipio, cultivo