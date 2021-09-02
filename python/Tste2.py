n1 = float(input())
n2 = float(input())
n3 = float(input())
freq = float(input())

media = round(((n1*2 + n2*2 + n3*3)/7), 1)
freq_format = freq * 100

print("Frequencia:  %.f%%" % freq_format)
print("Media: %.1f" % media)

if freq < 0.75:
    print("Aluno  reprovado por faltas!")
elif media > 9:
    print ("Aluno aprovado com louvor!")
elif media >= 6:
    print("Aluno aprovado!")
elif media >= 4:
    print("Aluno de rec!")
else:
    print("Aluno de reprovado!")