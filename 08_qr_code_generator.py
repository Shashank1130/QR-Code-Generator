from ensurepip import version
import qrcode
from PIL import Image

# Basic code generator 
# img = qrcode.make("https://www.youtube.com/watch?v=tFnMPudt3n0&t=107s")  # Make function makes  the qr!
# img.save("imgage2.png")  # save function will save the qr .



# Advanace code generator
qr = qrcode.QRCode(version=1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border = 4)

print("\n-------------------------------------------")
print("   **** WELCOME TO THE QR GENERATOR ****")
print("-------------------------------------------\n")


# adding the data in the qr
getting_data = input("Enter the 'url' or 'text' to generate the qr code: \n")

qr.add_data(getting_data)
qr.make(fit = True)



# now, generating the qr code
qr_color = input("\nChoose the color of the qr: ").lower()

qr_bg_color = input("Choose the back ground color: ")
img = qr.make_image(fill_color = qr_color, back_color = qr_bg_color)


# Getting the file name
name = input("\nEnter the name of the file as you want to save: ")

# saving the image
print("\nGenerating the qrcode!!")
img.save(f"{name}.png")

print(f"Sucessfully generated the qrcode named as {name}.png :)")
