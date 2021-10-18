def consoante(z):
    if z in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
        return True
    else:
        return False


def main():
    letra=input().lower()
    con=consoante(letra)
    print(con)


if __name__=='__main__':
    main()
