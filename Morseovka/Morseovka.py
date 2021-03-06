#Definování morseovky
MORSE_CODE_DICT = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
}


def zakodovani(text): #funkce pro zakodovani
    zakodovany_text = "" #zakodovany text = string
    for pismena in text: 
        if pismena != " ": #kontrola mista
            zakodovany_text = zakodovany_text + MORSE_CODE_DICT.get(pismena) + " " #vyhleda slovnik a prida odpovidajici znak + mezeru
        else:
            zakododvany_text += " " #pridani mezery
    print(zakodovany_text) #vypis zakodovany text


def dekodovani(text): #funkce pro dekodovani
    text += " " #pridani mezery
    key_list = list(MORSE_CODE_DICT.keys()) #pro pristup ke klicum
    val_list = list(MORSE_CODE_DICT.values())
    kod = "" 
    normal = ""
    for pismena in text:
        if pismena != " ": #kontrola mista
            kod += pismena #ukladani morseovky po znaku
            prostor = 0 #prostor
        else:
            prostor += 1 #pokud je rovno 1 oznacuje pismeno
            if prostor == 2: #pokud je rovno 2 oznacuje nove slovo
                normal += " " #pridani mezery
            else:
                normal = normal + key_list[val_list.index(kod)] #pristup ke klicum pomoci jejich hodnot
                kod = ""
    print(normal) #vypis dekodovanz text


print("\n\n\n\t\tMorse Code Generator")
ch = input("Stiskni E k zakodovani nebo D k Dekodovani : ")
if ch == 'E' or ch == 'e': #stiskni "e" a muzes zakodovat svoji vetu,slovo nebo pismeno
    text_k_zakodovani = input("Vlož text k zakodovani : ").upper()
    zakodovani(text_k_zakodovani)
else:
    text_k_dekodovani = input("Vlož text k dekodovani : ") #stiskni jakoukoli jinou klavesu a muzes dekodovat svoji vetu,slovo nebo pismeno
    dekodovani(text_k_dekodovani)


