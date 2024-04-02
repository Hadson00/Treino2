class DadosFuncionario:
    def __init__(self):
        self._nome = None
        self._cpf = 0
        self._idade = 0
        self._cargo = {
            'Gerente Regional': 10,
            'Assistente do gerente regional': 5,
            'Minion': 2,
            'Contabilidade': 1}
        self._horas_trabalho = 0.0
    
    def mostrarSalario(self, horas):    
        self._horas_trabalho = horas
        
        salario = self._cargo * horas

        return salario