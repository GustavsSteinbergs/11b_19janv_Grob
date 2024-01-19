def ierakstit_faila(lietotaja_vards):
    try:
        with open("lietotajs.txt", 'a', encoding='utf-8') as fails:
            fails.write(lietotaja_vards + '\n')
        print(f"Vārds '{lietotaja_vards}' veiksmīgi ierakstīts failā.")
    except IOError as e:
        print(f"Rakstīšanas kļūda: {e}")
    except Exception as e:
        print(f"Radās kļūda: {e}")

lietotaja_vards = input("Ievadiet savu vārdu: ")

ierakstit_faila(lietotaja_vards)
