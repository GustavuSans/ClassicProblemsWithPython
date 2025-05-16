def validation():
    text = input("Informe um texto: ")
    hasNumber = False
    for char in text:
        if char.isdigit():
            hasNumber = True
            break
    if hasNumber:
        print("A string contém pelo menos um número.")
    else:
        print("A string não contém números.")
validation()