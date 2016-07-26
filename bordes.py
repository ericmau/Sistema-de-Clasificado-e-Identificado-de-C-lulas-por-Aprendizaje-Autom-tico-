import pywt
from PIL import Image
import sys, pylab, numpy

def edges(path):
    im = Image.open(path).convert('L')
    arr = numpy.fromstring(im.tobytes(), numpy.uint8)
    arr.shape = (im.size[1], im.size[0])

    data = pywt.swt2(arr, 'haar', level=3, start_level=0)
    LL, (LH, HL, HH) = data[2]
    pylab.imshow(LH, interpolation='nearest', cmap=pylab.cm.gray)
    pylab.show()

def main():
    if len(sys.argv) > 1:
        path = str(sys.argv[1])
        edges(path)
    else:
        print 'Image file needed'


main()