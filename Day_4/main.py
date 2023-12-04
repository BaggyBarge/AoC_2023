# Day 4
import re
infile = open('input_d4.txt', 'r')

scratchcard = infile.readlines()
print()
regex_num = '(\d\d?)'
t = 0

# itero tra gli elementi di stcratchcard e creo due array con le giocate e i numeri vincenti
for i, item in enumerate(scratchcard):
    # Cerco e memorizzo la posizione dei due punti e del pipe in due variabili
    pos_pipe = item.find('|')
    pos_coln = item.find(':')
    # Creo e stampo la lista dei numeri gioocati e dei numeri vincenti della giocata corrente
    num_giocati = re.findall(regex_num, item[pos_pipe + 1:len(item.rstrip())])
    num_fortunati = re.findall(regex_num, item[pos_coln + 1:pos_pipe - 1])
    print('Numeri giocata:  ' + str(i) + ' : ' + str(num_giocati))
    print('Numeri vincenti: ' + str(i) + ' : ' + str(num_fortunati))
    # Calcolo l'intersezione delle due liste (trattandole come insiemi) per recuperare le giocate vincenti
    num_vincenti = list(set(num_giocati).intersection(set(num_fortunati)))
    # Calcolo i punti della singola scheda e li sommo al contatore t
    print('Punti scheda: ' + str(int(pow(2,len(num_vincenti)-1))))
    t += int(pow(2,len(num_vincenti)-1))
    print()
print ('Punti totali= ' + str(t))

infile.close()