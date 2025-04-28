import random

def analyze_profile(link):
    keywords=["e-sports", "furia", "cs:go", "valorant", "lol", "gaming", "pro player"]

    #Simulação:sorteia uma "relevância"

    relevance_score=random.randint(60, 100)

    return{
        "profile_link": link,
        "relevance_score": relevance_score,
        "keywords_detected": random.sample(keywords, 3) #simula detecção
    }