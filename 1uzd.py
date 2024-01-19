def lasit_un_drukait_failu(janvaris):
    try:
        with open(janvaris, 'r', encoding='utf-8') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Faila '{janvaris}' nav atrasts.")
    except Exception as e:
        print(f"Radās kļūda: {e}")
        
janvaris = 'piemers.txt'

lasit_un_drukait_failu(janvaris)
