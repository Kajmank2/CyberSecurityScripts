from pyzbar import pyzbar
import cv2
import argparse

#ap =argparse.ArgumentParser()
#ap.add_argument("-i","--image",required=True,help="path to input")

#args = vars(ap.parse_args())

#image =cv2.imread(args["image"])
data = []
for i in range(9374):
    i=i+1
    image = cv2.imread(str(i) + ".png")
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        (x,y,w,h)=barcode.rect
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType=barcode.type

        text = "{} ({})".format(barcodeData,barcodeType)
        print(text)
        data.append(text)
        cv2.putText(image,text,(x,y+10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
readingstring=""
tempstring=""
for x in data:
    tempstring+=str(x[0])
    if( x == "  (CODE128)"):
        tempstring=int(tempstring)
        readingstring+=chr(tempstring)
        readingstring+=''
        print(readingstring)
        tempstring=""
print(readingstring)
#cv2.imshow("Image",image)
#cv2.waitKey(0)


def decode(image):

    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        print("detected barcode:", obj)
        image = cv2.draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()

    return image

#decode("1.png")