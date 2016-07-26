from PIL import Image

def to_binary(image, umb):
   w, h = image.size
   pix = image.load()
   output = Image.new("L", (w, h))
   out_pix = output.load()
   for i in range(w):
     for j in range(h):
        if image.mode == "RGB":
	  if max(pix[i, j]) >= umb: out_pix[i, j] = 255
          else: out_pix[i, j] = 0
        elif image.mode == "L":
	  if pix[i, j] >= umb: out_pix[i, j] = 255
	  else: out_pix[i, j] = 0
   output.save(OUTPUT_FILE, 'PNG')
   return output

OUTPUT_FILE = '/Users/eric/Desktop/binbaltos.png'
I = Image.open('/Users/eric/Desktop/baltos.png')
to_binary(I,120)