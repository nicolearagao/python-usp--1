segundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))

if segundos >= 86400:
    dias = segundos // 86400
    if (segundos % 86400) >= 3600:
        horas = (segundos % 86400) // 3600
        if (segundos % 86400) % 3600 >= 60:
            minutos = ((segundos % 86400) % 3600) // 60
            segundo = ((segundos % 86400) % 3600) % 60
        else:
            minutos = 0
            segundo = 0
    else:
        horas = 0
        minutos = 0
        segundo = 0

elif segundos >= 3600:
    dias = 0
    horas = segundos // 3600
    if segundos % 3600 >= 60:
        minutos = (segundos % 3600) // 60
        segundo = (segundos % 3600) % 60
    else:
        minutos = 0
        segundo = 0

elif segundos >= 60:
    dias = 0
    horas = 0
    minutos = segundos // 60
    segundo = segundos % 60
else:
    dias = 0
    horas = 0
    minutos = 0
    segundo = segundos

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundo} segundos.")
