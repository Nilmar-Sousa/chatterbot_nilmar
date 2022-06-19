from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONFIGURACAO_CONVERSA = [
    "D:\Desenvolvimento\chatterbot_nilmar\conversas\informacoes.json",
    "D:\Desenvolvimento\chatterbot_nilmar\conversas\saudacoes.json"
] 

def iniciar():
    global robo
    global treinador 
    
    robo = ChatBot("Robô de Atendimento da Locadora de Carros")
    treinador = ListTrainer(robo)
    
def carregar_conversas():
    conversas = []
    for arquivo_configuracao in CONFIGURACAO_CONVERSA:
        with open(arquivo_configuracao, "r") as arquivo:
            conversas_configuradas = json.load(arquivo)
            conversas.append(conversas_configuradas["conversas"])
            arquivo.close()
    return conversas

def treinar_robo(treinador, conversas):
    for conversa in conversas:
        for mensagens_resposta in conversa:
            mensagem = mensagens_resposta["mensagem"]
            resposta = mensagens_resposta["resposta"]
            
            print(f"Treinando o robô para responder a: ", mensagem, " com a resposta: ", resposta)
            for mensagem in mensagem:
                treinador.train([mensagem, resposta])

if __name__ == "__main__":
    iniciar()
    
    conversas = carregar_conversas()
    if conversas:
        treinar_robo(treinador, conversas)