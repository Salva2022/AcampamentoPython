Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import locale

locale.setlocale(loocale.LC_ALL,  'pt_BR') # diz ao python que estamos no Brazil

val = locale.atof(input("Digite o valor da compra:")) #aceota decimal com vírgula
n50 = int(input("Digite a qtd de notas R$50:"))
n20 = int(input("Digite a qtd de notas R$20:"))
n10 = int(input("Digite a qtd de notas R$10:"))
n5 = int(input("Digite a qtd de notas R$5:"))
dinheiro = n50*50 + n20*20 + n10*10 + n5*5
troco = dinheiro - val
print(locale.formnat("Sua compra de foi de R$%f",val} locale.format("o cliente forneceu R$%f",dinheiro))