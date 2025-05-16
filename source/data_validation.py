import re
def validation():
    print("Observação: O nome não pode conter números ou caracteres especiais.")
    print("Se houver serão removidos.")
    name = input("Informe se nome: ")
    clean_name = re.sub(r'[^A-Za-zÀ-ÿ\s]', '', name)
    newName = ''.join(clean_name)
    removed_chars = [char for char in name if char not in clean_name]
    del clean_name
    if(removed_chars):
        print(f"Items removidos: {removed_chars}")
    else:
        print("Nenhum caractere inválido foi encontrado")
    if(newName == ''):
        print("Nome vázio")
        del newName
    else:
        print(f"Nome: {newName}")

validation()