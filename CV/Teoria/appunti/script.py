import datetime

#Dizionari
days = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
names = {1: "Gennaio", 2:"Febbraio", 3:"Marzo", 4:"Aprile", 5:"Maggio", 6:"Giugno", 7:"Luglio", 8:"Agosto", 9:"Settembre", 10:"Ottobre", 11:"Novembre", 12:"Dicembre"}


def isBisestile(year):
    return year % 4 == 0 and year & 400 == 0


def printDays(month, year):
    #Per printare correttamente l'ultimo del mese
    if month == 2:
        return 29 if isBisestile(year) else 28
    return days[month] # se non è febbraio allora sono tranquillo e accedo al dizionario con la chiave "mese"

start_d = datetime.datetime(2023, 1, 12)
final_d = datetime.datetime(2023, 9, 18)

i_date = final_d
output = []

while (start_d.year <= i_date.year):
    if (start_d.year == i_date.year) and (start_d.month == i_date.month):
        if (start_d.month == final_d.month) and (start_d.year == final_d.year):
            if start_d.day == 1 and final_d.day == printDays(final_d.month, final_d.year):
                #Inizio e fine mese
                output.append(f"{names[start_d.month]}")
            elif start_d.day == 1 and final_d.day != printDays(final_d.month, final_d.year):
                output.append(f"{start_d.day} {names[start_d.month]} {start_d.year} - {final_d.day} {names[final_d.month]} {final_d.year}")
            break
        
        if start_d.day == 1:
            #Sono in tutto il mese
            output.append(f"{names[start_d.month]} {start_d.year}")
        else:
            output.append(f"{start_d.day} {names[start_d.month]} {start_d.year} - {printDays(month=i_date.month, year=i_date.year)} {names[start_d.month]} {start_d.year}")
        break
    else:
        if i_date.day != printDays(i_date.month, i_date.year):
            output.append(f"{i_date.day} {names[i_date.month]} {i_date.year} - {printDays(month=i_date.month, year=i_date.month)} {names[i_date.month]} {i_date.year}")
        else:
            output.append(f"{names[i_date.month]} {i_date.year}")
    if i_date.month == 1:
        i_date = datetime.datetime(i_date.year-1, 12, printDays(i_date.month-1, i_date.year))
    else:
        i_date = datetime.datetime(i_date.year, i_date.month-1, printDays(i_date.month-1, i_date.year))


#print(output, end="\n")
print (f" <<< Starting date: {start_d} >>> \n <<< Final date: {final_d} >>> \n \n")
output.reverse() # Inverto la lista perche parto dal dalla fine e vado verso l'inizio
for value in output:
    print(f"{value}")