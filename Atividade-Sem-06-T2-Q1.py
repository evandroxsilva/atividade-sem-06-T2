def vogal(x):
    if x in ('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False

def main():
    letra=input().lower()
    vog=vogal(letra)
    print(vog)

if __name__=='__main__':
    main()
