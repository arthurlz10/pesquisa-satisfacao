excelente = 0 
bom = 0
ruim = 0
for i in range (50):
    print("\nEntrevistado", i+1)
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opiniao = int(input("Digite sua opiniao (1-excelente, 2-bom, 3-ruim): "))
    
    if opiniao == 1: 
       excelente +=1 
    elif opiniao == 3: 
        ruim +=1 
    elif opiniao == 2: 
         bom +=1

print("\nRESULTADO FINAL:")
print("Quantidade de excelente:", excelente)
print("Quantidade de bom", bom)
print("Quantidade de ruim", ruim)