# OpenCV
## Lettura di una immagine
* ``img = cv.imread("/path/img.png")``: Leggo un'immagine
## Conversione di immagini
* ``hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)``: Rendo l'immagine da BGR a HLS
* ``gray = cv.imread('path/img.png', cv.IMREAD_GRAYSCALE)``
* ``r = cv.cvtColor(img, cv.HLS2BGR)``: Converto l'immagine da HLS a BGR
* ``h, l, s = cv.split(hls)``: Splitto l'immagine nei tre canali differenti
* ``b, g, r = cv.split(bgr)``: Splitto l'immagine nei tre canali differenti
* ``bgr = cv.merge((b, g, r))``: Unisco i tre canali formando un'unica immagine composta da *b, g, r*
* ``img = a * img1 + b``: Funzione di variazione *luminosità* e *contrasto*, **a** regola il nostro contrasto e **b** regola la nostra luminosità
* $f(img) = \frac{img}{255}^{\gamma} \times 255$: Funzione di *Gamma Correction*, $\gamma \le 1$ aumenta la luminosità dei toni scuri mentre $\gamma ge 1$ diminuiscire la luministà toni chiari 
* $f(I[y, x])= 255 \times \frac{I[y, x] - \alpha}{\beta - \alpha}$: Espansione dei livelli di grigio per aumentare il contrasto, riscalo tutti i valori tra un minimo ed un massimo, scegliere $\alpha$ e $\beta$ in corrispondenza dei *percentili*, guardare metodo ``cv.equalizeHist``
## Calcolo Istogramma
* ``hist = cv.calcHist([img], [0], None, vmax=[256], range=[0, 256])``: Inserisco tutto all'interno di array siccome posso calcolarne nello stesso metodo piu istogrammi
* ``hist = np.histogram(img, vmax=256, range=[0, 256])[0]``:  Creo un istogramma utilizzando **numpy**
## Calcolo LUT
* ``img = cv.LUT(img, lut_table)``: Applico la *lut_table* all'immagine di input *img*
* ``img = cv.applyColorMap(img, map)``: Applico la *color map* all'immagine, tra le tante *maps* abbiamo **cv.COLORMAP_AUTMN, cv.COLORMAP_JET, cv.COLORMAP_HSV**
## Binarizzare un'immagine
* ``thr, result = cv.threshold(img, threshold=128, max_val=255, cv.THRESH_BINARY)``
* ``thr, result = cv.threshold(img, 128, 255, cv.THRESH_OTSU)``
* ``res = cv.adaptiveThreshold(img, value=255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, t1=11, t2=10)``: Binarizzo un'immagine, i valori di bianco verranno impostati a *value*, i valori ````*t1* e *t2* sono i due valori soglia che permettono di binarizzare l'immagine.
## Equalizzare
* ``res  = cv.equalizeHist(img)``: Equalizzo l'istogramma distribuendo meglio i valori dell'immagine
## Modifiche sull'immagine
* ``img_nn = cv.resize(img, (n_r, n_c), interpolation=cv.INTER_NEAREST)``: Faccio un resize di *img* nella nuova dimensione *(n_r, n_c)* con metodo di interpolazione *NEAREST*
* ``cv.line(img, p1=(x1, y1), p2=(x2, y2), color=(255, 0, 0))``: Mi permette di disegnare una linea sulla mia immagine con punto di partenza *(x1, y2)* e punto di destinazione *(x2, y2)*.
* ``img_bl = cv.resize(img, size, interpolation=cv.INTER_LINEAR)``: Metodo di interpolazione *LINEAR*
* ``imb_bc = cv.resize(img, size, interpolation=cv.INTER_CUBIC)``: Metodo di interpolazione *CUBIC*
## Calibrazione camera
* ``imgP, jacobian = cv.projectPoints(objPoint=obj, rvec=r, tvec=t, camera_m=m)``: Proiezione di punti 3D sull'immagine, conversione da punti 3D a punti 2D dati i parametri *intriseci* ed *estrinseci* della camera, *rvec* è la matrice di rotazione, *tvec* è il vettore di traslazione, *camera_m* sono i valori *intrinseci* della camera
* ``retVal, corners = cv.findChessboardCorners(img, size_chess=(w, h), corners=c, flags=..)``: Questo metodo mi permette di individuare dei vertici interi di un pattern scacchiera su un'immagine, *size_chess* numero di righe e colonne della scacchiera, *corners* array dei corner
* ``corners = cv.cornerSubPix(img, corners, winSize, zeroZone)``: Rifinisce le coordinate della scacchiera, mi permette di trovare il pixel esatto in cui è definito il mio corner
* ``img = cv.drawChessboardCorners(img, chess_size=(w, h), corners, retVal)``: Mi permette di visualizzare i corner della scacchiera
* ``retVal, cameraMatrix = cv.calibrateCamera(objP, imgP, imgSize, cameraMatrix)``: Stima dei parametri *intrinseci* ed *estrinseci* da un insieme di corrispondenze di punti 3D-2D individuate in una serie di immagini di un pattern di calibrazione
* ``cv.getOptimalNewCameraMatrix()``: Rettifica della informazione di un'immagine dati i parametri *instrinseci* della camera
## Trasformazioni affini
* ``img = cv.warpAffine(img, homography, size=(n_r, n_c), None, interpolation=cv.INTER_CUBIC, border_type=cv.BORDER_CONSTANT, value_border=x)``: Eseguo un warp affine utilizzando la matrice *homography*, con una nuova *size*
* ``h = cv.getPersceptiveTranforms(points1, points2)``: Mi permette di ottenere la matrice di trasformazione proiettiva, *points1, points2* sono due matrici di punti in cui sono presenti esattamente 4 punti in ciascuna matrice. 
* ``res = cv.warpPerspective(img, persp_m=h, size=(w, h), flags=cv.INTER_CUBIC)``: Mi permette di eseguire una *trasformazione proiettiva* partendo dalla mia *img* ed utilizzando la matrice *h* per eseguire la trasformazione
* ``cv.getRotationMatrix2D(center=(x, y), angle=z, scale=s)``: Calcola una matrice di affinità per una rotazione 2D
$$
  [α−ββα(1−α)⋅center.x−β⋅center.y]
  [β⋅center.x+(1−α)⋅center.y]
$$
α=scale⋅cosangle,β=scale⋅sinangle
* ``H = cv.getAffineTransform(m_points, pts)``: Date tre coppie di punti corrispondnenti calcola la matrice di trasformazione affine, dove:
  1. ``m_points = np.float32([[1, 1], [3, 1], [4, 6]])``
  2. ``c_pts = np.float32([[68, 35], [104, 51], [19, 50]], [[4, 110], [23, 14], [58, 10]])``
## Ottenere una maschera
* ``mask = cv.inRange(img, min_values=(0, 20, 40), max_values=(180, 256, 256))``: Attraverso questa funzione è possibile estrapolare dall'immagine di input una maschera. Nel caso in cui avessimo un'immagine con più canali, in questo caso 3, posso esprimere 3 diverse condizioni per ogni canale. In questo esempio voglio prendere sul canale *0* tutt i valori tra *0* e *179*, sul canale *1* voglio prendere tutti i valori tra *20* e *255* e sull'ultimo canale, il canale *2* voglio prendere tutti i valori tra *40* e *255*. La maschera che si ottiene è data dall'unione dei delle tre condizioni, viene fatto un *AND* logico sulle tre condizioni in modo da tenere solo quelle che realizzano tutti e tre i criteri. 


## Filtri, Blur
* ``img = cv.copyMakeBorder(img, top, bottom, left, right, cv.BORDER_DEFAULT)``
* ``img = cv.filter2D(img, type=cv.CV_16S, filter)``: Applico il filtro *f* all'immagine, la nuova immagine avrà tipo di dato *type*, se dovessi mettere *-1* manterrei il tipo originale dell'immagine
* ``smot = cv.boxFilter(img, type=-1, k_size=(7,7), normalize=True)``: Applico un box filter con normalizzazione
* ``f = np.ones((7, 7))``: Ottengo un filtro 7x7, posso usare questo filtro per ottenere un blur dato dalla media di un intorno 7x7 di ogni pixel
* ``img = cv.filter2D(img, type=-1, f)``: Applico il filtro *f* ottenendo un blur dato dalla media di 7 pixel per ciascun pixel. 
### Blur Gaussian, Median 
* ``bl = cv.blur(img, k_size=(x, y))``: Applico un blur all'immagine *img* con un filtro di dimensione *k_size*
* ``g = cv.getGaussianKernel(k_size=5, omega=1)``: Creo un filtro *gaussiano* con dimensione *k_size* e con valore *omega*
* ``img_b = cv.sepFilter(img, type=-1, g, g)``: Applico il filtro gaussiano
* ``img_b = cv.GaussianBlue(img, k_size(5,5), omega=1)``: Applico il filtro *gaussiano* attraverso un'unica funzione
* ``cv.medianBlur(img, k_size=x)``: Filtro mediano dell'immagine, il blur viene eseguito come *media* dei valori dei x vicini di ogni pixel.
## Bordi
Per rilevare i bordi di un'immagine bisogna compiere delle operazioni preliminari, in quanto un'immagine può contenere del **rumore**, per prima cosa quindi bisogna applicare un'operazione di *pulizia*, applicando dei filtri di blur.
### Trovare i bordi tramite (Difference of Gaussians)
Per rilevare i bordi tramite un filtro **Gaussiano** si base su: 
``Borders = IMG - (IMG_Blurred)``
### Bordi tramite Derivate
1. ``Prewitt``
2. ``Sobel``: 
  ```python
    dx, dy = cv.Sobel(img, type=cv.CV_32F, x=1, y=0, scale=1/8), cv.Sobel(img, type=cv.CV_32F, x=0, y=1, scale=1/8)
    mod = cv.magnitude(dx, dy)
    ang = cv.phase(dx, dy, angleInDegrees=True)
  ```
   * ``der = cv.Sobel(...)``: Mi permette di calcolare una sola derivata, vanno calcolate sia quella su *x* e quella su *y* tramite gli appositi flag
   * ``mod = cv.magnitude(derX, derY)``: Calcolo il modulo del gradiente per ogni pixel
   * ``angl = cv.phase(derX, derY, angleInDegrees=True)``: Ottengo l'angolo del gradiente in ogni pixel dell'immagine
1. ``Sharr``
2. ``Canny``:
   * ``edges = cv.Canny(blurred, th1, th2)``
### Gradiente
* ``n = cv.normalize(img, None, 0, 255, cv.NORM_MINMAX, type=cv.CV_8U)``: Normalizzo tutti i valori dell'immagine *img*, nei valori *0* e *255*, attraverso il metodo *NORM_MINMAX* 
* ``der = cv.Sobel(...)``: Mi permette di calcolare una sola derivata, vanno calcolate sia quella su *x* e quella su *y* tramite gli appositi flag
* ``mod = cv.magnitude(derX, derY)``: Calcolo il modulo del gradiente per ogni pixel
* ``angl = cv.phase(derX, derY, angleInDegrees=True)``: Ottengo l'angolo del gradiente in ogni pixel dell'immagine
### Laplaciano
Derivata seconda dell'immagine
* ``dst = cv.Laplacian(src_gray, ddepth=cv.CV_64F, ksize=kernel_size)``
## Analisi
### Trasformata Distanza
La trasformata distanza permette di ottenere la distanza di ogni pixel di *foreground* dal *background*. Ogni pixel avrà la distanza dal pixel di *background* più vicino. 
* ``dt4 = cv.distanceTransform(img, cv.DIST_L1, size=3)``: In questo caso la distanza viene calcolata con la metrica *L1*, ovvero *alto, basso, destra e sinistra* escludendo le diagonali
* ``dt8 = cv.distanceTransform(img, cv.DIST_C, size=3)``: In questo caso la distanza viene calcolata con la metrica *L_inf*, ovvero *alto, basso, destra, sinistra e le due diagonali*.  
### Estrazione dei Contorni
* ``c, topology = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)``: Questa funzione permette di estrarre solamente i contorni esterni, siccome abbiamo specificato il flag **cv.RETR_EXTERNAL**. 
* ``res = cv.drawContours(img, contours, -1, color=(255, 0, 0), thickness=2)``: Una volta ottenuti i contorni è possibile colorarli e disegnarli attraverso questo metodo. Prima di chiamare questa funzione è necessario *avere già i contorni*.
### Etichettatura delle componenti connesse
* ``numbers, conn_components = cv.connectedComponents(img)``: Attraverso questa funzione è possibile ottenere le *componenti connesse* all'interno dell'immagine **binarizzata**, all'interno del vettore *conn_components* si avrà una matrice in cui ogni singola componente è identificata dallo stesso valore. Nel caso in cui io volessi ogni singola componente connessa distina posso fare: 
```python
n, cc = cv.connectedComponents(img)
l = []
for num in range(n):
  m = np.zeros_like(cc)
  m[cc == num] = 255
  l.append(m)
```
In questo caso sapendo che ho **n** componenti connesse, io posso iterare su di essere, prendere tutte le varie componenti connesse in maniera distinta creando delle *maschere*, siccome ogni componente connessa è identificata da un numero unico. Di conseguenza la stessa componente connessa è identificata *dallo stesso numero*.
* ``n, cc, stats, centroids = cv.connectedComponentsWithStats(img)``: In questo caso oltre a ottenere le componenti connesse, ottengo anche tutte le **statistiche** di ogni componente connessa e tutti i **centroidi** di ogni componente connessa.
```python
  n, cc, stats, centroids = cv.connectedComponents(img)
  for i in range(n):
    area = stats[i, cv.CC_STAT_AREA]
    x, y = stats[i, cv.CC_STAT_LEFT], stats[i, cv.CC_STAT_RIGHT]
    w, h = stats[i, cv.CC_STAT_WIDTH], stats[i, cv.STAT_HEIGTH]
```
  1. **stats[i, cv.CC_STAT_AREA]**: Mi permette di ottenere l'area della componente *i-esima*
  2. **stats[i, cv.CC_STAT_LEFT]**: Ottengo il punto più a sinistra della componente connessa
  3. **stats[i, cv.CC_STAT_RIGHT]**: Ottengo il punto più a destra della componente connessa
  4. **stats[i, cv.CC_STAT_WIDTH]**: Ottengo la *lunghezza* della componente connessa
  5. **stats[i, cv.CC_STAT_HEIGTH]**: Ottengo *l'altezza* della componente connessa
### Dilatazione ed Erosione
Attraverso la *dilatazione ed *erosione* posso eseguire operazioni fondamentali sulle *componenti connesse*.
1. **Dilatazione**: La nuova immagine che si va ad ottenere è il risultato dell'applicazione di una maschera, si accende sempre il pixel *q*, ovvero il pixel centrale della maschera, tale pixel si accende se ho un pixel di *foreground* all'interno della mia maschera
2. **Erosione**: La nuova immagine che si va ad ottenere è l'insieme dei pixel tali che, traslando l'intera maschera S tutti i pixel di *foregound* sono contenuti nell'elemento strutturante. Accendo il pixel se e solo se *tutti i pixel di foregound sono contenuti nell'elemento strutturante*.
* ``se = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))``: Ottengo un elemento strutturante quadrato di lato 15x15
* ``dil = cv.morphologyEx(img, se)``: Eseguo una *dilatazione* con un filtro *se*
* ``ero = cv.morphologyEx(img, se)``: Eseguo una *erosione* con un filtro *se*
### Apertura e Chiusura
* **Apertura**: Erosione seguita da dilatazione, *seprata gli oggetti debolmente connessi e rimuove regioni piccole*
* **Chiusura**: Dilatazione seguita da erosione, *riempie buchi e piccole concavità e rafforza la connessione di regioni unite debolmente*
* ``s = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))``: Ottengo un elemento strutturante di forma circolare con raggio 5.
* ``res1 = cv.morphologyEx(img, cv.MORPH_OPEN, s)``: Eseguo un'operazione di *apertura* utilizzando *s* come elemento strutturante
* ``res2 = cv.morphologyEx(img, cv.MORPH_CLOSE, s)``: Eseguo un'operazione di *chiusura* utilizzando *s* come elemento strutturante
## Movimento
### Estrazione di frame
* ``cap = cv.VideoCapture('myvideo.mp4)``: Leggo il video
* ``ret, frame = cap.read()``: Per leggere ogni singolo frame di un video, va usato tale metodo il quale ritorna un *flag*, il quale vale *False* quando non ho più frame da leggere
* ``cap.release()``: Rilascio la *risorsa*
### Algoritmo di MOG
* ``mog = cv.createBackgroundSubractorMOG2(detectShadows=False)``: Istanzio l'oggetto poichè ho la necessità di *mantenere uno stato*
* ``mask = mog.apply(frame)``: Eseguo l'algoritmo di *mog* sul frame grayscale, al metodo **apply** è possibile passare un valore, il *learning rate* compreso tra 0 ed 1, controlla in che misura il background è aggiornato.
### Tracking di oggetti, Mean-Shift
* ``conf_map = cv.calcBackProject([img], [0], histogram, [0, 255], 1)``: Ottengo la mappa di confidenzialità per l'immagine corrente
* ``_, new_wind = cv.meanShift(confidential_map, wind, term_crit)``:  Applico l'algoritmo di *mean shift*, il quale necessita di una *mappa di confidenza* in grado di determinare quali siano gli oggetti di nostro interesse.
* ``_, (x, y, w, h) = cv.meanShift(confidential=conf, wind_size=(pos[0] - OBJ_SIZE//2, pos[1]-OBJ_SIZE//2, OBJ_SIZE, OBJ_SIZE), term=TERM_CRIT)``
## Template Matching
* ``R = cv.matchTemplate(img, template, method=cv.TM_SQDIFF/cv.TM_SQDIFF_NORMED/cv.TM_CCORR/cv.TM_CCORR_NORMED/cv.TM_CCOEFF/cv.TM_CCOEFF_NORMED)``: Confronta *template* con tutte le posizioni di (x, y) di *img*, risultato in *R*, il valore del matching in ogni pixel.
* ``r_min, r_max, pos_min, pos_max = cv.minMaxLoc(R)``: Ottengo il minimo e il massimo locale di R
## CNN con openCV
* ``net = cv.dnn.readNet('network)``: Carico la rete neurale dal file
* ``net.setInput(cv.dnn.blobFromImage(img))``: Carico l'immagine all'interno della rete
* ``out = net.forward()``: Esegue la rete per ottenere l'output
* ``type = np.argmax(out) | out.argmax()``: Ottengo il valore di output più probabile
