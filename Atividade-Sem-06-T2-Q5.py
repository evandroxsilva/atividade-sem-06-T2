def caractere(x):
    if x in ('a', 'e', 'i', 'o', 'u'):
        return print('vogal')
    if x in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
        return print('consoante')
    if x in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return print('número')
    else:
        print('símbolo')


def main():
    letra=input().lower()
    vcns=caractere(letra)


if __name__=='__main__':
    main()
