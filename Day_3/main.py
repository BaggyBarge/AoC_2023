# Day 3
import re
infile = open('input_d3.txt','r')
# readlines() crea un vettore contenente il contenuto di ogni riga del file infile
schematic = infile.readlines()
line = 0
t = 0
# Definizione regex ricerca numeri e simboli
regex_num = '(\d+)'
regex_sym = '([^.\d])'



for item in schematic:
    print('contenuto riga: '+item.rstrip())
    # finditer() crea un oggetto contenente i match della regex regex_num e le relative informazioni (inizio, fine, contenuto, etc.)
    print('line: ' + str(line))
    for match in re.finditer(regex_num,schematic[line]):
        print('Numero matchato: ' + match.group())

        # Controllo se il valore si trova a inizio riga
        if match.start() == 0:
            num_start = match.start()
        else:
            num_start = match.start()-1
        
        # o a fine riga
        if match.end() == int(len(schematic[line]))-1:
            num_end = match.end()
        else:
            num_end = match.end()+1
        
        findings = []
        # Skippo il controllo della linea precedente alla prima riga
        if line > 0:
            print('intorno precedente: ' + schematic[line-1][num_start:num_end])
            findings = findings + re.findall(regex_sym,schematic[line-1][num_start:num_end])
        # Effettuo il controllo nella riga corrente
        print('intorno corrente:   ' + schematic[line][num_start:num_end])
        findings = findings + re.findall(regex_sym,schematic[line][num_start:num_end])
        # Skippo il controllo della linea successiva all'ultima riga
        if line <= int(len(schematic)-2):
            print('intorno successivo: ' + schematic[line+1][num_start:num_end])
            findings = findings + (re.findall(regex_sym,schematic[line+1][num_start:num_end]))



        if findings != []:
            print('🟢 ' + match.group() + ' is a part number!')
            t += int(match.group())
        else:
            print('🛑 Numero parte non trovato')
        print()


    line += 1
    print()
print('Soluzione parte 1: ' + str(t) + '\n\n////////////Inizio seconda parte\\\\\\\\\\\\\\\\\\\\\\')


infile.close()