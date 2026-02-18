def reuniao():
    nmrProfessores = int(input())
    tempo = int(input())
    if nmrProfessores>1:
        tempomax= tempo-nmrProfessores
        tempomax = int(tempomax/nmrProfessores)
    elif nmrProfessores==1:
        tempomax = int(tempo/nmrProfessores)
    print(tempomax)

reuniao()