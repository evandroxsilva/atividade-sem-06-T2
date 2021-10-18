def vogecon(z):
    if z in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'):
        return True
    else:
        return False


def main():
    letra=input().lower()
    vc=vogecon(letra)
    print(vc)

if __name__=='__main__':
    main()
