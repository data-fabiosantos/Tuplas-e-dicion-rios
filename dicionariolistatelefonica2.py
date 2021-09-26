# Adicionar contato no dicionário agenda, caso já exista é possivel alterar
# linha 4 a 18

agenda = {}
print("*** Cadastro de telefones ***")
while True:
    contato = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    if contato in agenda:
        if input(f"Contato já cadastrado com o número {agenda[contato]}. Deseja alterar? (s/n) ") == "n":
            continue
    if telefone in agenda.values():
        print("Telefone já cadastrado para outro contato")
        continue
    agenda[contato] = telefone
    if input("Deseja cadastrar um novo contato (s/n): ") == "n":
        break
print(agenda)

# Para remoção algum dado da agenda da linha 22 a 29

# Metodo del
del agenda[“Nome”]

# Metodo pop
agenda = {"Maria": "(41) 98765-4321", "João": "(11) 12345-6789"}
print(agenda.pop("Maria", "Contato com nome Maria localizado"))
print(agenda.pop("José", "Contato com nome José não localizado"))
print(agenda)


