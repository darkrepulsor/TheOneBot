def format_quote(quote):
    return f"|Quote| -> {quote}"

def format_character(character):
    return f"\õ\\õ//õ/ -> {character}"

def format_spf_character(data):
    if isinstance(data, list) and len(data) > 0:
        character = data[0]
        return f"""Nome: {character.get("name", "Anonymous")}
Wiki: {character.get("wikiUrl", "Not known")}
Raça: {character.get("race", "Cabra da Peste")}
Nascimento: {character.get("birth", "???")}
Morte: {character.get("death", "???")}
Gênero: {character.get("gender", "XX ou XY")}
Cabelo: {character.get("hair", "???")}
Altura: {character.get("height", "N/A")}
Reino: {character.get("realm", "N/A")}
Esposa: {character.get("spouse", "N/A")}"""
    elif 'Erro' in data:
        return f"Erro: {data['Erro']}"
    else:
        return 'Sorry, nothing here!'
    
def format_books(book):
    if isinstance(book,list) and len(book) > 0:
        m1 = book[0]["name"]
        m2 = book[1]["name"]
        m3 = book[2]["name"]
        message = f"""\U0001F4DC {m1}        
\U0001F4DC {m2}
\U0001F4DC {m3}"""
        return message 