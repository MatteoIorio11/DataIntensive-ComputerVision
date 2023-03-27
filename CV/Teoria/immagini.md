# Immagini
Le immagini digitali sono una *matrice di pixel*, dove ogni pixel rappresenta il dato misurato da un sensore. I pixel possono avere diversi formati:
* Bianco e Nero;
* Grayscale;
* Colore;
le immagini inoltre possono essere salvate con diversi formati e diversi stili di compressione. Per identificare *l'occupazione* totale in memoria di una immagine è necessario effettuare il calcolo: $Width\times Height \times BitDepth$. 
## Matrici Gray Scale
Una immagine in gray scale è una *matrice di punti di luce*. Tutti i valori dei singoli pixel vanno da 0 a 255, identificando per ciascun valore una tonalità differentre di grigio. Nel caso in cui i valori siano alti stanno ad identificare **maggiore luminosità** al contrario valori bassi identificano una **minore luminosità**. Le matrici *gray scale* possono essere identificate in due modi:
- 1 Byte [0, 255];
- 2 Float [0, 1];
## Coordinate dei pixel
Ogni singolo pixel all'interno della matrice è identificato da una coppia di coordinate *x-y* ``cv.line(immagine, start=(colonna=4,riga=0), end=(colonna=3,riga=6), color)``,``immagine[riga=3, colonna=1]``.
## Organizzazione dei pixel in memoria
I pixel all'interno della matrice sono *salvati come un matrice in C*, ovvero viene allocata una porzione di memoria grande quanto l'intera immagine in cui ogni pixel punta al suo successivo in questo modo è più facile eseguire iterazioni sui singoli pixel o fare accessi diretti.
### Immagini Gray Scale in Python
```python
img1 = np.zeros((15,16), dtype=np.uint8) #tutti i pixel a zero
img2 = np.full((15, 16), dtype=np.uint8) # tutti i pixel a 255
img3 = np.random.randint(0, 256, (15, 16), dtype=np.uint8) #pixel random

#Caricamento immagini tramite OpenCV

img4 = cv2.imread("path", cv.IMREAD_GRAYSCALE)
```
## Immagini a Colori
Le immagini a colori, chiamate anche *tensori 3D*, sono immagini composte da 3 matrici:
* Matrice del Blue;
* Matrice del Verde;
* Matrice del Rosso
Ogni canale contiene la luminosità di un colore primario, in questo modo sommando la luminosità dei tre colori primasi si ottengono i valori colori dell'immagine.

### Modello RGB
**Modello additivo**:
* I colori sono ottenuti mediante la combinazione dei 3 colori primari Red, Green, Blue

**Spazio RGB**:
* Ogni colore può essere considerato come un punto in uno spazio a tre dimensioni, non è idoneo per il raggruppamento spaziale di colori percepiti come simili dall'uomo. Le distanze tra due sfumature non sono le somiglianze percepite dalle persone, in quanto la differenza è minima.
#### Coordinate dei Pixel
Per individuare le coordinate con la quale identificare un singolo pixel è necessario indicare *x-y-canale*:
* Coordinate cartesiane ``pixel_pos = (x=14, y=3, channel=1)``
* Notazione matriciale ``immagine[14, 3, 0] = 255``
La libreria di *OpenCV* utilizza come ordine dei canali il modello **Blue-Green-Red**, B=0, G=1, R=2.
Le immagini all'interno della memoria sono salvate all'interno di una matrice in cui in ogni pixel c'è una tripletta che identifca le varie tonalità di (B, G, R).
```python
immagine=cv.imread("path", cv.IMREAD_ANYCOLOR)
b, g, r = immmagine.copy(), immmagine.copy(), immmagine.copy()
b[...,1:3], g[...,0:3:2], r[...,0:2] = 0, 0, 0 
#b[...,1:3]: azzero i canali 1 e 2 ovvero i canali green e red in modo da lasciare solamente il blue
#g[..., 0:3:2]: azzero i canali 0 e 2 ovvero i canali blue e red in modo da lasciare solo il green
#r[..., 0:2]: azzero il  canale 0 e 1 ovvero il blue e il green in modo da lasciare solo il red
```
### Rappresentazione HSV-HSL
Oltre al modello BGR è possibile utilizzare altre modalità con la quale rappresentare i colori di un'immagine. Le rappresentazioni *HSV*, *HSL* sono tecniche con la quale i colori sono molto più riconoscibili dal punto di vista di come gli esseri umani percepiscono i colori, questi due standard sono basati su:
* Tinta (HUE)
* Saturazione: quanto è acceso il mio colore
* Luminosità (Value o Lightness): quantità di luce che c'è nel colore

La comodità di utilizzare questi due standard è quella di:
*  *specificare i colori* in maniera più intuitiva.
*  possono essere utilizzate più efficacemente per localizzazione e riconoscimento di oggetti nelle immagini.

Lo *HUE* può essere rappresentato attraverso una circonferenza in cui ogni angolo rappresenta un colore diverso (angoli da 0 a 180):
* rosso primario a 0 gradi
* verde primario a 120 gradi
* blu primaroo a 240 gradi.  

L'asse verticale al centro della circonferenza comprende tutte le varie tonalità di grigio, dal nero (luminosità 0) al bianco (luminosità 1). I colori primari (BGR) e secondari si trovano attorno al cilindro con saturazione a 1.
* In **HSV** questi colori saturi hanno luminosità 1
* In **HSL** invece hanno luminosità 0.5
#### HSV e HSL in Python/OpenCV
Anche in questo caso le immagini sono tensori 3D. In python è possibile utilizzare la funzione ``newIMG = cv2.cvtColor(immagine, cv.COLOR:HSV2BGR/cv.COLOR:HSL2BGR/...)`` per convertire da RGB a HSL/HSV e viceversa. In OpenCV nel caso in cui volessimo usare il formato **HSL** l'ordine con la quale sono suddivisi i canali è HLS (H=0, L=1, S=2). Gli intervalli di valori per le immagini soni:
* H [0, 179] corrisponde a [0, $\pi$]
* S, V/L [0, 255] corrispondente a [0...1]
Per visualizzare o salvare le immagini **è necessario convertire l'immagine in formato BGR**.
```python
original = cv.imread("path")
hls = cv.cvtColor(original, cv.COLOR_BGR2HLS)
h, l, s = cv.split(hls)
l1 = l//2 #dimezzo la luminosità di tutti i pixel
s1 = np.full_like(s, 64) # metto a 64 tutta la saturazione
risultato = cv.cvtColor(cv.merge((h, l1, s1)), cv.COLOR_HLS2BGR)
```
## Istogramma di un'immagine grayscale
Un istogramma identifica il numero di pixel dell'immagine per ciascun livello di grigio. Ogni colonna dell'istogramma è il numero di pixel che corrisponde al livello di grigio, si hanno in totale 255 colonne, *all'interno di ogni colonna c'è il numero di pixel per quella tonalità*.

### Calcolo istogramma
```python
def calc_hist_python(img):
    h = np.zeros(256, dtype=int)
    for p in np.nditer(img):
        h[p] += 1
    return h

def calc_hist_np(img):
    return np.histogram(img, 256, [0, 256])[0]

def calc_hist_cv(img):
    return cv.calcHist([img], [0], None, [256], [0, 256]).squeeze() #poichè potrei fare tanti istogrammi per ogni immagine passata
```
### Analisi dell'istogramma
Se i diversi oggetti in un'immagine hanno livelli di grigio differenti, l0istogramma può fornire un *primo semplice meccanismo di separazione* degli oggetti dallo sfondo. 

## Operazioni sui pixel
Su una singola immagine: $I'[y, x] = f(I[y, x])$ (quando otteniamo una nuova immagine tramite una funzione su ogni pixel). Ogni pixel dell'immagine di uscita è *funzione* solo del corrispondente pixel dell'immagine di input (es: variazione della luminosità, variazione contrasto, ...). Questa operazione può essere eseguita anche su una serie di immagini (es operazioni aritmetiche su immagini).

### Variazione luminosità e contrasto
La funzione $f(v) = \alpha (v+\beta)$ dove:
* $\alpha$ controlla il contrasto
* $\beta$ la luminosità
* v il colore del pixel originale
i valori di output sono forzati in [0, 255]

### Gamma correction
$$
f(v) =
\begin{pmatrix}
    \frac{v}{255}
\end{pmatrix}^\gamma \times 255
$$
* se $\gamma < 1$ aumenta la luminosità dei toni scuri
* se $\gamma > 1$ diminuisce la luminosità dei toni chiari 
### Lookup Table (LUT)
Se il numero di colori o livelli di grigio è inferiore al numero di pixel nell'immagine, è più efficiente memorizzare il risultato della funzione di mapping $f$ per ogni input in un array, da utilizzare poi come tabella per eseguire l'operazione su tutti i pixel. 

$$
I'[y, x] = f(I[y, x]) \rightarrow I'[y, x] = LUT[I[y, x]]
$$
Questo vuol dire che per ogni pixel nell'immagine originale, ci sarà una riga all'interno della LUT che andrà a specificare la tonalità del colore. 
LUT=
| v | $f(v)$  |
|------|------|
|  0   |   0  |
|  .   |   .  |
|  .   |   .  |
|  .   |   .  |
|  100 | 17   |

Una strategia che può nascere attraverso l'utilizzo delle LUT è quella di salvare la nostra immagine in formato *gray scale* e successivamente applicare la nostra LUT, LUT[gray] in modo da ottenere la combinazione RGB.

| GRAY | RED  | GREEN | BLUE |
|------|------|-------|------|
|  0   |   0  |  10   |  30  |
|  .   |   .  |   .   |  .   |
|  .   |   .  |   .   |  .   |
|  100 | 17   |  65   | 91   |

#### LUT in Python
```python
def applica_np_lut(img):
    return lut[img]

def applica_cv_lut(img):
    return cv.LUT(img, lut)
```

### Lut da GrayScale a RGB
La libreria di *OpenCV* mette a disposizione una funzione con la quale è possibile convertire una immagine a livelli di grigi in una immagine a colori appoggiandosi ad una LUT table. 
```python
img = cv.imread("paht", cv.IMREAD_GRAYSCALE)
colored_img = cv.applyColorMap(img, cv.COLORMAP_JET)
```
## Operazioni aritmetiche fra immagini: Differenza
Tramite l'utilizzo della sottrazione dello "sfondo" è possibile individuare gli oggetti di interesse
```python 
img, back = cv.imread("path1"), cv.imread("path2")
diff = img-back
mask = diff!=0 #maschera booleana in cui prendo tutti i bit non neri, ovvero dove c'è il nostro oggetto di interesse
res = np.zeros_like(img)
res[mask] = img[mask]
```
## Operazioni aritmetiche fra immagini: Operatori Bitwise
Analogamente alla maschera di bit, l'operatore **AND** consente di azzerare selettivamente alcuni dei pixel in una immagine, **OR** consente invece di impostarne dei valori.
## Operazioni aritmetiche fra immagini: Alpha Blending
Combinazione fra uno sfondo (RGB)  e un'immagine(RGB) con abbinato un valore di "trasparenza" er ciascun pixel (fra 0 e 1).

