

dummy = input("Qual a temperatura da carne? ")

if "F" in dummy:
    dummy1 = dummy.split("º")
    dummyGraus = (int(dummy1[0]) - 32)*5/9
else:
    dummy1 = dummy.split("º")
    dummyGraus = int(dummy1[0])

if dummyGraus >= 48 and dummyGraus <= 53:
    print("Selada")
elif dummyGraus >= 54 and dummyGraus <= 59:
    print("Ao ponto para mal")
elif dummyGraus >= 60 and dummyGraus <= 64:
    print("Ao ponto")
elif dummyGraus >= 65 and dummyGraus <= 70:
    print("Ao ponto para mais")
elif dummyGraus >= 71:
    print("Mal passada")
else:
    print("Nem esquentou")
