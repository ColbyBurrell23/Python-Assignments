
import instaloader
ig = instaloader.Instaloader()
dp = input("Enter Insta Username: ")
ig.download_profile(dp, profile_pic_only=True)

weight = input("what is your weight? ")
unit = input("was your weight above in kgs or lbs? ")
if unit.upper() == "LBS":
    converted = float(weight)*.45
    print("Your weight in kgs is " +str(converted))
else:
    converted = float(weight)/.45
    print(f'your weight in lbs is {converted}')

    #list = ["apple", "Oranges", Bananas"]
fruits = ["apple", "oranges", "Banana"]
for i in fruits:
        print(i)
prices = [500, 300, 200]
Total = 0
for i in prices:
    print(i)

correct_pin = 1245
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Enter your pin for ATM: "))

    if guess == correct_pin:
        print("Access granted. Your pin is correct")
        break # no need to loop. end our code

    else:
        guess_count+=1
        remaining_attempts = guess_limit-guess_count

        if remaining_attempts>0:
            print(f"Incorrect PIN. You have {remaining_attempts} left.")
        else:
            print("Sorry to many attempts. Your account is locked")

my_list = [1,2,3]
my_list2 = ["a", "b", "c"]

my_list = ["apple", "banana", "cherry"]
print(my_list)

#Creating QR Code
#pip install qrcode
#pip install pillow

import qrcode
from PIL import Image
data = 'Python is fun'  # your data or YouTube link here

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="white")
img.save("MyQRCode2.jpeg")
img.show()


import qrcode
from PIL import Image
Logo_link = 'csumb.jpg'
logo = Image.open(Logo_link)
basewidth = 100
wpercent = (basewidth/float(logo.size[0]))
13
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
QRcode = qrcode.QRCode(
error_correction=qrcode.constants.ERROR_CORRECT_H
)
url = 'https://csumb.edu/business/about/'
QRcode.add_data(url)
QRcode.make()
QRcolor = 'Green' #want the QR code to be of green color
QRimg = QRcode.make_image(
fill_color=QRcolor, back_color="white").convert('RGB')
pos = ((QRimg.size[0] - logo.size[0]) // 2,
(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
QRimg.save('gfg_QR.png')
img = Image.open("gfg_QR.png") #this will open the qrcode we created in line above
img.show() #this will show us the qrcode
print('QR code generated!')

#2. QR Code with CSUMB's logo (transparent logo in QrCode)

# Import Files & Libraries #
import qrcode
from PIL import Image

# Logo Variables For Transparency #
img = Image.open('csumb.jpg') # Allows us to open CSUMB logo image
img1 = img.convert("RGBA") # Converts image to an RGBA format

img2 = img1.getdata() # Allows to pull RGBA data from the image

# Logo Transparency #
newData = [] # Variable that will store new RGB data for the image #
for item in img2:
    if item[:3] == (255, 255, 255): # Pulls the white RGB value from the CSUMB logo #
        newData.append((255, 255, 255, 0)) # Then replaces the white with transparency/red RGB value #
    else:
        newData.append(item)
img1.putdata(newData) # Applies changes to the image
img1.save("csumb.png") # Saves the new image with the updated data #

# Logo Variables For QR Insertion #
Logo_Link = 'csumb.png'
Logo = Image.open(Logo_Link)

# Logo Set-Up Coding #

basewidth = 100
wpercent = basewidth/float(Logo.size[0])
hsize = int(Logo.size[1]*float(wpercent))
Logo = Logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)

# QR Code Set-Up Coding #

QRCode = qrcode.QRCode(
    error_correction = qrcode.constants.ERROR_CORRECT_H
    )
URL = 'https://youtu.be/9XLeGxPRINE'
QRCode.add_data(URL)
QRimg = QRCode.make_image(
    fill_color = 'red', back_color = 'white').convert('RGB')

# Print & Save QR Code #

diff = (QRimg.size[0]-Logo.size[0])//2, (QRimg.size[1]-Logo.size[1])//2
QRimg.paste(Logo, diff, Logo)
QRimg.save('TheNewestQRCode.png')
img = Image.open('TheNewestQRCode.png')
img.show()



#1c) Separting two consecutive pages 2 to 4 and then 4 to 5.
#Everything will be same except adding another for loop
from PyPDF3 import PdfFileReader, PdfFileWriter
pdf_file_path = 'myfile.pdf'
pdf = PdfFileReader(pdf_file_path)
pdfwriter = PdfFileWriter()

# Loop through pages 1 to 3
for page_num in range(0,3 ):  #  includes pages 1, 2 and 3
    pdfwriter.addPage(pdf.getPage(page_num))
# Loop through pages 8 to 9
for page_num in range(7, 9):  #  includes pages 8, and 9
    pdfwriter.addPage(pdf.getPage(page_num))

# Save the extracted pages into a new PDF file
with open('newoutput1.pdf', 'wb') as out:
    pdfwriter.write(out)
print('Selected pages have been extracted')

#2a) PDF file merger using each pdf file name
#install PyPDF2 library first
# Import PdfReader to read PDF files and PdfMerger to merge multiple PDFs
from PyPDF2 import PdfReader, PdfMerger

# Load the first PDF file into a PdfReader object
pdf_file1 = PdfReader("file1.pdf")

# Load the second PDF file into another PdfReader object
pdf_file2 = PdfReader("file2.pdf")

# Create a PdfMerger object to combine multiple PDFs
output = PdfMerger()

# Append the first PDF file to the merger
output.append(pdf_file1)

# Append the second PDF file to the merger
output.append(pdf_file2)

# Open (or create) a new file "merged15.pdf" in binary write mode to save the merged PDF
with open("merged15.pdf", "wb") as output_stream:
    output.write(output_stream)  # Write the merged PDF content to the file

#2a) Same codes as above but with minor change. Allow selecting which Pages to be merged from the files.

#install PyPDF2 library first
from PyPDF2 import PdfMerger
pdfs = ['file1.pdf', 'file2.pdf']
merger = PdfMerger()
merger.append("file1.pdf")
merger.append("file2.pdf", pages=(0,2) ) #allows page 1, and 2 to be included from this pdf
merger.write("mergeddd.pdf")
merger.close


#2c). PDF file merger without using file name (for hundreds of PDF files in our project folder)
#Below, we want to merge all PDF files that are under Project folder called HelloWorld. We will name this merged file as merged.pdf.

import os  # Importing the os module to interact with the operating system
from PyPDF2 import PdfMerger  # Importing PdfMerger from PyPDF2 to merge PDFs

# Get the current working directory where the script is being executed
source_dir = os.getcwd()

# Create an instance of PdfMerger to handle merging PDFs
merger = PdfMerger()

# Loop through all files in the current directory
for item in os.listdir(source_dir):
    # Check if the file ends with '.pdf' (i.e., it's a PDF file)
    if item.endswith('pdf'):
        # Append the PDF file to the merger
        merger.append(item)

# Write the merged PDFs into a new file named 'Complete.pdf'
merger.write('Complete.pdf')

# Close the merger object to free up resources
merger.close()


#GUI code:
#below we are creating a GUI using PyCharm. If we run the code below, it gives us a GUI Window.
#This Window may not have nay labels (i.e., text), or EntryBox (i.e., box that allows typing) or Buttons that take command
from tkinter import *  # Import everything from the Tkinter library. no need to install this library
root = Tk()  # Create the main application window (root window)
print(root)  # Print the reference of the Tkinter window object in the console
root.mainloop()  # Start the Tkinter event loop to keep the window open

#GUI Code with some adjustments such as Title, or siz geometry
#This Window may not have nay labels (i.e., text), or EntryBox (i.e., box that allows typing) or Buttons that take command
from tkinter import *  # Import everything from the Tkinter library
root = Tk()  # Create the main application window (root window)
root.title("Age Calculator")  # Set the window title
root.geometry("400x400")  # Set window size as a string "widthxheight"
#root.resizeable(0,0) or root.resizable(width=False, height=False) to not allow people to expand GUI window
print(root)  # Print the reference of the Tkinter window object in the console
root.mainloop()  # Use root.mainloop() instead of mainloop()