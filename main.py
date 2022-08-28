from improvedcaesar import ImprovedCaesar

if __name__ == '__main__':
    test = "Привет WoRld!1"

    caesar = ImprovedCaesar()
    print(test)
    print(caesar.encoder(text=test, step=1))
