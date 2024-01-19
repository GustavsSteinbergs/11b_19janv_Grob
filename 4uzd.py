def lasit_failu(janvaris):
    try:
        with open(janvaris, 'r', encoding='utf-8') as fails:
            saturs = fails.read()
            print(f"Faila '{janvaris}' saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Faila '{janvaris}' nav atrasts.")
    except Exception as e:
        print(f"Radās kļūda: {e}")

janvaris = input("Ievadiet faila nosaukumu: ")
faila_formats = input("Ievadiet faila formātu (paplašinājumu, piemēram, txt): ")

if not faila_formats.startswith('.'):
    faila_formats = '.' + faila_formats

pilns_faila_nosaukums = janvaris + faila_formats

lasit_failu(pilns_faila_nosaukums)
