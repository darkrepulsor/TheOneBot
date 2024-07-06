def format_quote(quote):
    return f"|Quote| -> {quote}"

def format_character(character):
    return f"\õ\\õ//õ/ -> {character}"

def format_spf_character(data):
    if isinstance(data, list) and len(data) > 0:
        character = data[0]
        return f"""Nome: {character.get("name", "N/A")}
Wiki: {character.get("wikiUrl", "N/A")}
Raça: {character.get("race", "N/A")}
Nascimento: {character.get("birth", "N/A")}
Morte: {character.get("death", "N/A")}
Gênero: {character.get("gender", "N/A")}
Cabelo: {character.get("hair", "N/A")}
Altura: {character.get("height", "N/A")}
Reino: {character.get("realm", "N/A")}
Esposa: {character.get("spouse", "N/A")}"""
    elif 'Erro' in data:
        return f"Erro: {data['Erro']}"
    else:
        return 'Sorry, nothing here!'