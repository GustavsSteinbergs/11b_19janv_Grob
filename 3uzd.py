def lasit_treso_rindu(janvaris):
    try:
        with open(janvaris, 'r', encoding='utf-8') as fails:
            rindas = fails.readlines()
            if len(rindas) >= 3:
                tresa_rinda = rindas[2]
                print("Trešās rindas saturs:")
                print(tresa_rinda)
            else:
                print("Failā nav pietiekami daudz rindu.")
    except FileNotFoundError:
        print(f"Faila '{janvaris}' nav atrasts.")
    except Exception as e:
        print(f"Radās kļūda: {e}")

janvaris = 'piemers.txt'

lasit_treso_rindu(janvaris)
