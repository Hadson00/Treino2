from dados_funcionario import DadosFuncionario
import json 

class Raphael(DadosFuncionario):
    def __init__(self):
        super().__init__()
    def mostrarSalario(self, horas):
        return super().mostrarSalario(horas)

func1 = Raphael()

func1._nome = str(input('Digite seu nome: '))
func1._cpf = int(input('Digite seu cpf: '))
func1._idade = int(input('Digite seu idade: '))
horas = float(input('Digite suas horas de trabalho: '))