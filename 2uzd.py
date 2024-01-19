import csv

def lasit_otro_kolonnu(janvaris):
    try:
        with open(janvaris, 'r', newline='', encoding='utf-8') as fails:
            lasitajs = csv.reader(fails)
            
            print("Otrās kolonnas dati:")
            for rinda in lasitajs:
                if len(rinda) > 1:
                    print(rinda[1])
                else:
                    print("Nepietiekami daudz kolonnu rindā.")
    except FileNotFoundError:
        print(f"Faila '{janvaris}' nav atrasts.")
    except Exception as e:
        print(f"Radās kļūda: {e}")

janvaris = 'piemers.csv'

lasit_otro_kolonnu(janvaris)
