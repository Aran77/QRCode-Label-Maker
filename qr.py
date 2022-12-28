#import QRcode to make QR codes
import qrcode
#Import PDF functions
from fpdf import FPDF
#Import OS for file operations
import os

#configure QRCode
qr = qrcode.QRCode(
    version =1,
    box_size = 5,
    border = 1
    )
#set a counter
data = 1
#set a number of labels to produce
noofLabels = 8

#loop the number of labels required
for i in range(noofLabels):
    #create the actual qr code
    qr.add_data(str(data).rjust(4,'0'))
    qr.make(fit=True)
    img = qr.make_image(fill = 'black', back_color = 'white')
    img.save(str(data).rjust(4,'0') +'.png')
    #set PDF options
    pdf = FPDF(orientation="landscape", format=(50,100))
    pdf.add_page()
    #add the QR code png to the PDF
    pdf.image(str(data).rjust(4,'0') + '.png',5,5,w=40,h=40)
    #set font and add text label
    pdf.set_font("Arial", size = 35)
    pdf.cell(0,10, txt = str(data).rjust(4,'0'), align = 'R')
    #save the pdf
    pdf.output("labels/" +str(data).rjust(4,'0')+".pdf")
    print(str(data).rjust(4,'0') +'.pdf')
    #clear QR object
    qr.clear()
    #increment counter
    data = data +1
