# Numpy 
Attributi importanti degli oggetti **ndarray**:
* ``ndim``: Il numero di dimensioni, "assi".
* ``shape``: Una tupla di interi che indica il nuimeri di elementi lungo ciascuna dimensione, (righe, colonne)
* ``size``: Il numero totale di elementi
* ``dtype``: Tipo degli elementi
* ``itemsize``: La dimensione di ogni elemento
## Creare un array
* ``a1 = np.array([x1, x2, x3, ..])``
* ``a2 = np.array([x1, x2, x3, ..], dtype=np.uint8)``
* ``f = np.full_like(a1, x)``: Imposto una matrice f, con le stesse dimensioni di a1 ma con tutti i valori uguali a *x*
* ``H = np.tile(np.arange(255, -1, -15), dtype=np.uint8, (x, y))``: Ricopio il mio vettore creando una matrice di x righe e y colonne.
* ``v = np.tile(np.arange(255, -1, -15), dtype=np.uint8)[:, np.newaxis], (x, y))``: Creo una matrice con colonne i valori di np.arange
* ``m = np.array([[x11, x12], [x21, x22], [x31, x32]])``
* ``e = np.empty((2,7), dtype=np.uint16)``
* ``e2 = np.empty_like(a1)``: Creo una matrice vuota con la stessa dimensione di a1
* ``z = np.zeros(5)``: Matrice 5x5
* ``z2 = np.zeros_like(a1)``: Matrice di zeri con la stessa dimensione di a1
* ``on = np.ones(3, dtype=np.int)``
* ``z2 = np.zeros((2,3))``
* ``rnd = np.random.random((2,3))``
* ``rnd2 = np.random.randint(min=0, max=255, (x, y, z), dtype=np.uint8)``: Mi permette di creare un array di random da *min* a *max*, di dimensioni *x, y* con *z* canali.
* ``m = np.clip(a1, 0,255)``: Forzo il range di matrice *a1* nei valori *0* e *255*
* ``ar = np.arange(start=100, end=110, passo=2)``
* ``id = np.identity(3)``: Matrice con tutti "1" sulla diagonale principale
## Operazioni di Base
* ``c = m1 - m2``: Differenza tra valori
* ``c = m1 ** 2``: Elevo tutti gli elementi alla seconda
* ``c = np.sqrt(m1)``: Radice quadrata di ogni elemento
* ``c = m1 > X``: Matrice booleana in cui avrò **True** nel caso in cui il valore sia maggiore di X, **False** altrimenti
* ``c = m1 == m2``: Matrice booleana in cui avrò **True** nel caso in cui i due valori siano uguali, **False** altrimenti
* ``c = m1 * m2``: Prodotto elemento per elemento
* ``c = m1 @ m2``: Prodotto matriciale
* ``m1 *= m2``: Non creo un nuovo oggetto
* ``m1 = m1 * m2``: *m1* verrà creato, creo un nuovo oggetto
* ``m1.astype(np.uint64)``: Cambio il tipo degli elementi contenuti in *m1*
* ``a.min()``: Ritorna il valore **minimo**
* ``a.max()``: Ritorna il valore **massimo**
* ``a.sum()``: Ritorna la **somma** di tutti i valori
* ``a.sum(axis=1)``: Ritorna la **somma di tutte le righe**
* ``a.sum(axis=0)``: Ritorna la **somma di tutte le colonne**
* ``t = a.T``: Trasposta
* ``t = a.transpose()``: Trasposta
* ``sq = a.squeeze()``: Rimuove eventuali dimensioni a 1
* ``p1 = np.percentile(m, x)``: Prendo il percentile *x*
* ``diff = np.abs(m1 - m2)``: Differenza in valore assoluto tra i due vettori
* ``a = np.isin(m1, [1, 2, 3])``: Ottengo una maschera di booleani, i cui valori sono quelli passati come secondo argomento
* ``i_max = np.argmax(m1) | m1.argmax()``: Ottengo l'indice in cui ho il valore masimo
* ``i_min = np.argmin(m2) | m2.argmin()``: Ottengo l'indice in cui ho il valore minimo
* ``max_cols = np.argmax(m1, axis=1)``: Ottengo una lista in cui ho tutti i valori massimi in ogni riga
* ``max_rows = np.argmax(m1, axis=0)``: Ottengo una lista in cui ho tutti i valori massimi di ogni colonna
* ``min_cols = np.argmin(m1, axis=1)``: Ottengo una lista in cui ho tutti i valori minimi in ogni riga
* ``min_rows = np.argmin(m1, axis=0)``: Ottengo una lista in cui ho tutti i valori minimi in ogni riga
* ``index = np.unravel_index(np.argmax(m), m.shape)``: Ottengo *row, col* in cui ho il valore massimo
* ``np.where(condition= m1 > 10, m1, m1*10)``: In questo caso se la condizione è rispettata lascio il valore originale altrimenti il valore viene moltiplicato per 10
* ``np.histogram(img, v_max=255, [0, 256])[0]``: Calcolo istogramma della matrice *img*, il valore massimo che voglio registrare è *v_max*
## Indicizzazione e Slicing
* ``a[x]``: Accedo all'elemento in posizione *x*
* ``a[x:y]``: Accedo ai valori dall'elemento *x* all'elemento *y-1*
* ``a[:x:p]``: Prendo tutte le righe e modifico fino a *x-1* con passo *p*, (x=6, p=2 $\rightarrow$ 0, 2, 4)
* ``a[::-1]``: Step negativo, vado in ordine inverso
* ``a[::p] += a[x::p]``: Equivale a *a[i]+=a[i+1], con i=0, cols-1-p*
* ``a[:]=-1``: Modifico tutti gli elementi
* ``a[x, y]``: Riga *x*, colonna *y*
* ``a[:x, y]``: Tutte le righe da *0 a x-1*, e tutte la colonna *y*
* ``a[:, y]``: Tutta la colonna *y*
* ``a[x, :]``: Tutta la riga *x*
* ``a[x]``: Tutta la riga *x*
* ``a[-x:]``: Ultime *x* righe
## Itarare su un array
Si puo fare con la maniera classica:
```python
for riga in matrix:
    print(riga)
```
Oppure
* ``a = np.fromfunction(lambda i,j: i*10+j, (3, 5), dtype=np.uint64)``
```python
for el in matrix.flat:
    print(el)
```
## Modifica della forma
* ``b = a.reshape(2, 6)``
* ``c = a.reshape(2, 6, -1)``: Se una dimensione è *-1*, viene calcolata automaticamente
* ``a.resize(2,6)``: Modifcia l'array stesso
* ``d = a.ravel()``: Restituisce i dati come array monodimensionale
* ``b = a[np.newaxis, ...]``: Aggiunta di nuove dimensioni in maniera automatica
* ``b = a[np.newaxis, ..., np.newaxis, np.newaxis]``
## Concatenare array
* ``vs = np.vstack((m1, m2))``: Accoda verticalmente (m1 = [1, 2, 3], m2 = [4, 5, 6] $\righarrow$ [1,2,3,4,5,6])
* ``hs = np.hstack((m1, m2))``: Accoda orizzontalemente
* ``cs = np.columnstack((m1, m2))``: affianca array 1D come colonne di un array 2D, si crea una matrice con colonne m1 e m2
## Copie e viste di array
* ``b = a``: Non crea un oggetto ma copio solo il riferimento
* ``c = a[x:y]``: Creo una vista di *a*
* ``d = a.copy()``: Creo una copia di *a*
## Broadcasting
Il **BroadCasting** consente di agire su input con forme diverse. Se gli array di input non hanno lo stesso numeri di dimensioni, un "1" viene anteposto alla shape dell'array piu piccolo. 
```python
a = np.array([7, 5, 3, 1]) ->  [7, 5, 3, 1]
b = np.arange(8).reshape(2, -1) -> [[0, 1, 2, 3],
                                    [4, 5, 6, 7]]
# -1 nel reshape cosi si arrangia lui a capire quante colonne fare
c = a + b 
"""
a viene convertito in una matrice con due righe, con tutti valori uguali. La prima riga verrà ricopiata nella nuova seconda riga avendo:
a = [[7, 5, 3, 1],
     [7, 5, 3, 1]]
"""
```
## Indicizzare un array di indici
```python
a = np.arange(12)**2 -> [0 ,1 ,4 ,9, 16, 25, 36, 49, 64, 81, 100, 121]
idx1 = np.array([1, 1, 3, 8, 5])
print(a[idx1])
"""
Ottengo: [1, 1, 9, 64, 25]
"""
idx2 = np.array[[3, 4], [9, 7]]
print(a[idx2])
"""
Ottengo: [[9, 16],
          [81, 39]]
"""
a = (np.arange(12)**2).reshaèe(3,4) # 3 righe 4 colonne
idx_r = np.array([[0,0,0], [1,1,1]])
idx_c  = np.array([2,3,2], [0,0,0])
print(a[idx_r, idx_c]) 
"""
[[4, 9, 4], 
 [16, 16, 16]]
 prendo: [(r=0, c=2), (r=0, c=3), (r=0, c=2)], (r=1, c=0), (r=1, c=0), (r=1, c=0)]
"""
```
### Indicizzare con array booleani
```python

a = (np.arange(12)**2).reshaèe(3,4) # 3 righe 4 colonne
b = a > 4
print(a[b]) # printo solamente tutti i valori maggiori stretti di 4.
"""
```

