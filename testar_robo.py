import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):
    def setUp(self):
        self.robo = ChatBot("Robô de Atendimento da Locadora de Carros",
                read_only=True,
                statement_comparison_function = comparar_mensagens,
                response_selection_method= get_first_response,
                logic_adapters=[
                    {
                        "import_path": "chatterbot.logic.BestMatch",
                    }  
            ])
        
class TesteInformacoes(unittest.TestCase):
    def setUp(self):
        self.robo = ChatBot("Robô de Atendimento da Locadora de Carros",
                read_only=True,
                statement_comparison_function = comparar_mensagens,
                response_comparison_function = get_first_response,
                # response_selection_method= get_first_response,
                logic_adapters=[
                    {
                        "import_path": "chatterbot.logic.BestMatch",
                    }  
            ])
        
    def testar_oi(self):
        saudacoes = ["oi", "olá"]
        for saudacao in saudacoes:
            print(f"Testando: {saudacao}")
            resposta = self.robo.get_response(saudacao)
            self.assertIn("Olá, sou o robô de atendimento da Locadora de Carros. Como posso te ajudar?", resposta.text)
    
    def testar_localizacao(self):
        print("Testando a informação 'Localização'")
        informacoes = ["Onde a locadora está localizada?", "Onde a locadora fica?", "Onde fica a locadora?", "Onde é a locadora?", "Onde fica?"]
        for informacao in informacoes:
            print(f"Testando: {informacao}")
            resposta = self.robo.get_response(informacao)
            self.assertIn("A locadora está localizada na Avenida Airton Sena, número: 7, Bairro: Cruzeiro", resposta.text)
            
    def testar_horario(self):
        print("Testando a informação 'Horário'")
        informacoes = ["Qual é o horário de funcionamento da locadora?", "Até que horas funciona?", "Que horas abre?", "Que horas fecha?", "Abre aos sábados?", "Abre no domingo?", "Abre aos domingos?", "Abre no sábado?"]
        for informacao in informacoes:
            print(f"Testando: {informacao}")
            resposta = self.robo.get_response(informacao)
            self.assertIn("A locadora funciona nos seguintes horários: Segunda a Sexta (08:00 até 18:00) e sábado (08:00 até 12:00).", resposta.text)
            
    def testar_categorias(self):
        print("Testando a informação 'Categorias'")
        informacoes = ["Quais são as categorias de carro que a locadora oferece?", "Quais categorias de carro a locadora possuí?", "Quais são as categorias?"]
        for informacao in informacoes:
            print(f"Testando: {informacao}")
            resposta = self.robo.get_response(informacao)
            self.assertIn("A locadora possuí as seguintes categorias de carros: Grupo A - Compacto, Grupo B - Compacto Com Ar, Grupo C - Econômico Com Ar, Grupo F - Intermediário, Grupo G - Suv, Grupo L - Executivo, Grupo V - Pick-up Com Ar.", resposta.text)
            
    def testar_alugar(self):
        print("Testando a informação 'Alugar'")
        informacoes = ["Como alugar um carro?", "Como posso alugar um carro?", "Como fazer para alugar um carro", "Como alugar um carro?", "o que fazer para alugar um carro?"]
        for informacao in informacoes:
            print(f"Testando: {informacao}")
            resposta = self.robo.get_response(informacao)
            self.assertIn("Para alugar um carro basta escolher a categoria e o carro, em seguida escolher a data e a hora de retirada e de devolução, após isso pagar o valor do total das diárias e retirar o carro no dia e horário selecionado.", resposta.text)
            
    def testar_pagamento(self):
        print("Testando a informação 'Pagamento'")
        informacoes = ["Quais as formas de pagamento?", "Quais são as condições de pagamento?", "Formas de pagamento aceitas?"]
        for informacao in informacoes:
            print(f"Testando: {informacao}")
            resposta = self.robo.get_response(informacao)
            self.assertIn("As formas de pagamento disponíveis são: Dinheiro, Pix, Cartão de Débito, Cartão de Crédito (até 12 vezes s/ juros).", resposta.text)
            
    def testar_furto_roubo(self):
        print("Testando a informação 'Furto e Roubo'")
        informacoes = ["O que devo fazer em casos de acidente, furto ou roubo do carro alugado?", "O que fazer em caso de acidente?", "O que fazer em caso de furto ou roubo?"]
        for informacao in informacoes:
            print(f"Testando: {informacao}")
            resposta = self.robo.get_response(informacao)
            self.assertIn("Em ambos os casos é necessário registrar um boletim de ocorrência e levar até a nossa locadora para dar sequência aos procedimentos necessários.", resposta.text)
                        
    def testar_periodo(self):
        print("Testando a informação 'Período'")
        informacoes = ["Qual o período máximo que posso ficar com um carro alugado?", "Qual o máximo de tempo que posso ficar com o carro alugado", "Quanto tempo posso ficar com o carro alugado?", "Quantos dias posso ficar com o carro?"]
        for informacao in informacoes:
            print(f"Testando: {informacao}")
            resposta = self.robo.get_response(informacao)
            self.assertIn("O período máximo para locações é de 30 dias", resposta.text)

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()
    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))
    testes.addTest(carregador.loadTestsFromTestCase(TesteInformacoes))
    executor = unittest.TextTestRunner()
    executor.run(testes)