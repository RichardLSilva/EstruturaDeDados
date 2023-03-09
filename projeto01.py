nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
nota03 = float(input('Digite a terceira nota: '))


def media(nota01, nota02, nota03):
    if nota01 < 0 or nota01 > 10:
        print('Nota 01 inválida')

    else:
        if nota02 < 0 or nota02 > 10:
            print('Nota 02 inválida')

        else:
            if nota03 < 0 or nota03 > 10:
                print('Nota 03 inválida')

            else:
                total = ((nota01 * 4) + (nota02 * 4) + (nota03 * 2)) / 10
                print('A média ponderada é {:.2f}'.format(total))

                return total

media_notas = media(nota01, nota02, nota03)

def validar_media(media_notas):
    if media_notas < 0 or media_notas > 10:
        print('Media invalida')
    else:
        if media_notas > 5.9:
            print('Aprovado')
        else:
            print('Reprovado')


def maior_nota(nota01, nota02, nota03):
    if nota01 > nota02 and nota01 > nota03:
        print('Sua maior nota foi a nota 01: {}'.format(nota01))
    else:
        if nota02 > nota01 and nota02 > nota03:
            print('Sua maior nota foi a nota 02: {}'.format(nota02))
        else:
            print('Sua maior nota foi a nota 03: {}'.format(nota03))




validar_media(media_notas)
maior_nota(nota01, nota02, nota03)


