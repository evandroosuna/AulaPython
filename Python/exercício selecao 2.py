diaDaSemana = input("Informe o dia da semana: ")
match diaDaSemana.strip().lower():
    case "segunda":
        mensagem = ("Trabalho")
    case "terça":
        mensagem = ("Trabalho")
    case "quarta":
        mensagem = ("Trabalho")
    case "quinta":
        mensagem = ("Trabalho")
    case "sexta":
        mensagem = ("Trabalho")
    case "sabado":
        mensagem = ("Casa")
    case "domingo":
        mensagem = ("Casa")
    case _:
        mensagem = ("Dia inexistente")
print (mensagem)
