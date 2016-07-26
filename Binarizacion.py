from PIL import Image
#Convertir a grayscale
#Parametros
#image Objeto de la libreria PIL con la imagen a convertir.
#filt Filtro a usar("prom" para promedio, "max" para mayor", "min" para menor)
def to_grayscale(image, filt):
  if image.mode == "RGB":
    w, h = image.size
    pix = image.load()
    output = Image.new("RGB", (w, h))
    out_pix = output.load()
    for i in range(w):
      for j in range(h):
        curr = pix[i, j]
	if filt == "prom":
	  prom = (curr[0] + curr[1] + curr[2]) / 3
	  out_pix[i, j] = prom, prom, prom
	if filt == "max":
          out_pix[i, j] = max(curr), max(curr), max(curr)
	if filt == "min":
          out_pix[i, j] = min(curr), min(curr), min(curr)
    output.save(OUTPUT_FILE, 'PNG')
    return output
  else:
    print "Imagen en blanco y negro"
    return image


OUTPUT_FILE = '/Users/eric/Desktop/byn.png'
I = Image.open('/Users/eric/Desktop/b2.png')
to_grayscale(I,'min')