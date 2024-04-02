import nltk
from nltk.chat.util import Chat, reflections


# padrão de resposta do chat bot em mensagens
pares = [
    [
        r"oi|olá|e ai",
        ["Oi, tudo bem?", "Olá como posso ajudar você?"]
    ],
    [
        r"qual é o seu nome?",
        ["Meu nome é ChatBot. E o seu?",]
    ],
    [
        r"qual é o seu nome?",
        ["Meu nome é ChatBot e o seu?",]
    ],
    [
        r"como você está?",
        ["Estou bem, obrigado por perguntar.", ]
    ],
    [
        r"adeus",
        ["Adeus! Volte logo."]
    ],
]

# criando o chatbot

def chatbot():
    print("Olá! Eu sou um chatbot. Como posso ajudar você hoje? Digite 'adeus' para sair.")
    chat = Chat(pares, reflections)
    chat.converse()


if __name__ == "__main__":
    chatbot()





