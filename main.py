from arabic_to_roman import conversion_arabe_romain
from roman_to_arabic import conversion_romain_arabe, is_roman_number

def main():
    print("=== Conversion Chiffres Arabes <-> Chiffres Romains ===")
    print("1 - Arabe -> Romain")
    print("2 - Romain -> Arabe")
    
    choix = input("Choisissez une option (1 ou 2) : ").strip()
    
    if choix == "1":
        while True:
            try:
                nb = int(input("Entrez un nombre arabe entier > 0 : "))
                if nb <= 0:
                    print("Le nombre doit être supérieur à 0")
                else:
                    break
            except ValueError:
                print("Entrée invalide : veuillez entrer un entier")
        print("Résultat :", conversion_arabe_romain(nb))
    
    elif choix == "2":
        rom = input("Entrez un chiffre romain : ").upper()
        if not is_roman_number(rom):
            print("Chiffre romain invalide")
        else:
            conversion_romain_arabe(rom)
    
    else:
        print("Option invalide. Choisissez 1 ou 2.")

if __name__ == "__main__":
    main()
