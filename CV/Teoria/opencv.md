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
* ``img_bl = cv.resize(img, size, interpolation=cv.INTER_LINEAR)``: Metodo di interpolazione *LINEAR*
* ``imb_bc = cv.resize(img, size, interpolation=cv.INTER_CUBIC)``: Metodo di interpolazione *CUBIC*
## Trasformazioni affini
* ``img = cv.warpAffine(img, homography, size=(n_r, n_c), None, interpolation=cv.INTER_CUBIC, border_type=cv.BORDER_CONSTANT, value_border=x)``: Eseguo un warp affine utilizzando la matrice *homography*, con una nuova *size*
* ``h = cv.getPersceptiveTRanforms(points1, points2)``
## Filtri
* ``img = cv.copyMakeBorder(img, top, bottom, left, right, cv.BORDER_DEFAULT)``
* ``img = cv.filter2D(img, type=cv.CV_16S, filter)``: Applico il filtro *f* all'immagine, la nuova immagine avrà tipo di dato *type*, se dovessi mettere *-1* manterrei il tipo originale dell'immagine
* ``smot = cv.boxFilter(img, type=-1, k_size=(7,7), normalize=True)``: Applico un box filter con normalizzazione
* ``bl = cv.blur(img, k_size=(x, y))``: Applico un blur all'immagine *img* con un filtro di dimensione *k_size*
* ``g = cv.getGaussianKernel(k_size=5, omega=1)``: Creo un filtro *gaussiano* con dimensione *k_size* e con valore *omega*
* ``img_b = cv.sepFilter(img, type=-1, g, g)``: Applico il filtro gaussiano
* ``img_b = cv.GaussianBlue(img, k_size(5,5), omega=1)``: Applico il filtro *gaussiano* attraverso un'unica funzione
## Bordi
### Trovare i bordi tramite (Difference of Gaussians)