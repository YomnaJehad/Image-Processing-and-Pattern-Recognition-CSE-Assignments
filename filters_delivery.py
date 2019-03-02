
#NAME : YOMNA JEHAD MOHAMMED
#ID : 1401696
#E-MAIL: yomnaj96@gmail.com



########################################################
#import opencv
import cv2 
import numpy as np

#read the input image and resize for more convenient output
inputImage = cv2.imread('/home/yomnaj/Downloads/52883808_2365121180438230_6515732917249900544_n.jpg',1)
inputImage = cv2.resize(inputImage, (0, 0), None, .50, .50)


#This filter's output is a gray scaled image 
def inkwell(img):

	output= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


	return output



#This filter's output is a greenish-yellowish version of the image
#  *The scaling values are obtained through iterations of tuning and checking*
def Lily(img):
	output=img.copy()

	output[:,:,0] = output[:,:,0]*0.05+50  
	output[:,:,1] = output[:,:,1]*0.6 +50 
	output[:,:,2] = output[:,:,2]*0.35+100

	return output


#This filter's output is reddish
def Poprocket(img):

	output=img.copy()
	# B G R 
	#output[:,:,0]= output[:,:,0]*0.3+50
	#output[:,:,1]= output[:,:,1]*0.2
	output[:,:,2]= output[:,:,2]*.6 +100

	return output

#This filter's output is uhmm dusty i'd say, like a dust storm  
def Lordkelvin(img):


	output=img.copy()
	output[:,:,0] = output[:,:,0] *0.3 + 50  
	output[:,:,1] = output[:,:,1] *0.6 +50
	output[:,:,2] = output[:,:,2] *0.5 +100




	return output

#This filter's output is blue-ish
def Walden(img):


	output=img.copy()
	output[:,:,0] = output[:,:,0] *0.6+100 
	#output[:,:,1] = output[:,:,1] *0.9
	#output[:,:,2] = output[:,:,2] *0.4




	return output

#This filter's output is of larger contrust in the colors
def Lomo_fi(img):


	#-----Converting image to LAB Color model----------------------------------- 
	lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
	#cv2.imshow("lab",lab)

	#-----Splitting the LAB image to different channels-------------------------
	l, a, b = cv2.split(lab)
	#cv2.imshow('l_channel', l)
	#cv2.imshow('a_channel', a)
	#cv2.imshow('b_channel', b)

	#-----Applying CLAHE to L-channel-------------------------------------------
	clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
	cl = clahe.apply(l)
	#cv2.imshow('CLAHE output', cl)

	#-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
	limg = cv2.merge((cl,a,b))
	#cv2.imshow('limg', limg)

	#-----Converting image from LAB Color model to RGB model--------------------
	final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

	return final



##GENERAL FUNCTION 
def insta_like(img,instafilter):

	if instafilter == 'Lily':
		output=Lily(inputImage)
	elif instafilter == 'Inkwell':	
		output=inkwell(inputImage)
	elif instafilter == 'Poprocket':
		output=Poprocket(inputImage)
	elif instafilter == 'Lordkelvin':	
		output=Lordkelvin(inputImage)
	elif instafilter == 'Walden':
		output=Walden(inputImage)
	elif instafilter == 'Lomo_fi':
		output=Lomo_fi(inputImage)
	else:
		output= img
	return output

#Show all the outputs each in a separate window 
cv2.imshow('Original Image', inputImage)
cv2.imshow('Lily Filter', insta_like(inputImage,'Lily'))
cv2.imshow('Inkwell Filter',  insta_like(inputImage,'Inkwell'))
cv2.imshow('Poprocket Filter', insta_like(inputImage,'Poprocket'))
cv2.imshow('Lordkelvin Filter', insta_like(inputImage,'Lordkelvin'))
cv2.imshow('Walden Filter', insta_like(inputImage,'Walden')	)
cv2.imshow('Lomo_fi Filter', insta_like(inputImage,'Lomo_fi')	)

cv2.waitKey()

