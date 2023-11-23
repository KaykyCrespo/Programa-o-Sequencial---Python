dias = int(input("Digite os dias: "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos =  int(input("Digite os segundos: "))
res_dia = dias*86400
res_horas = horas*3600
res_minutos = minutos*60
res_total = res_dia + res_horas + res_minutos + segundos
print(res_total)