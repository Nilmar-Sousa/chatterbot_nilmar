from chatterbot import ChatBot
from chatterbot.response_selection import get_first_response
from difflib import SequenceMatcher

def comparar_mensagens(mensagem_digitada, mensagem_provavel):
    confianca = 0.0
    digitada = mensagem_digitada.text
    provavel = mensagem_provavel.text
    if digitada and provavel:
        confianca = SequenceMatcher(None, 
            digitada,
            provavel)
        confianca = round(confianca.ratio(), 2)
    return confianca

def executar_robo():
    robo = ChatBot("Robô de Atendimento da Locadora de Carros",
        read_only = True,
        statement_comparisson_function = comparar_mensagens,
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
                "response_selection_method": get_first_response
            }
        ])
    
    while True:
        entrada = input("Olá, Como posso lhe ajudar?.........\n")
        resposta = robo.get_response(entrada)
        if resposta.confidence > 0.70:
            print(resposta.text)
        else:
            print("Ainda não sei como responder essa pergunta")
            print("Posso lhe ajudar em algo mais?...........")
            
if __name__ == "__main__":
    executar_robo()