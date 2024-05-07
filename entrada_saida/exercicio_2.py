def converter_para_centimetros(altura_metros):
    altura_centimetros = altura_metros * 100
    return altura_centimetros

altura_metros = float(input("Digite sua altura em metros: "))
altura_centimetros = converter_para_centimetros(altura_metros)
print("Sua altura em centímetros é:", altura_centimetros, "cm")