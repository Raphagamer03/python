# Criar variáveis para Nome (str) , Idade (int) OK
# Altura(float) e Peso (float) de uma pessoa    OK
# Criar variável com o ano atual (int)          OK
# Obter o ano de nascimento da pessoa (baseado na idade e no ano atual) OK/TALVEZ USAR Observação : datetime.now().year → Obtém o ano atual automaticamente. 
# Obter o IMC da pessoa com 2 casas decimais ( Peso e na Altura da Pessoa) OK
# Exibir um texto com todos os valores na tela usando F-String (com as chaves) OK

Nome = input('Escreva seu nome: ') 
Idade = int(input('Escreva sua Idade: '))
Altura = float(input('Escreva sua Altura: '))
Peso = int(input('Escreva o seu Peso: '))
AnoAtual = int(input('Escreva o Ano Atual: '))
AnoDeNascimento = AnoAtual - Idade # Calcula o Ano de nascimento
IMC = Peso / (Altura*2)


print(f"Seu nome é : {Nome}") 
print(f"Sua Idade é: {Idade} anos")
print(f"Sua Altura é: {Altura:.2f} metros") #Exibe com duas casas decimais
print(f"Seu Peso é: {Peso} kg")
print(f"O Ano Atual é:  {AnoAtual}")
print(f"Você nasceu no ano de {AnoDeNascimento}. ") #formatação usando f-string
print(f"Seu IMC é: {IMC:.2f}") # calculo IMC com duas casas decimais

