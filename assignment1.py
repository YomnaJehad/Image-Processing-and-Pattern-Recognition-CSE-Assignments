
import cv2 
import numpy as np
inputImage = cv2.imread('/home/yomnaj/Downloads/52883808_2365121180438230_6515732917249900544_n.jpg',1)

#inputImage = cv2.imread('/home/yomnaj/Downloads/52918040_842983602713658_9107732662340026368_n.jpg',1)

inputImage = cv2.resize(inputImage, (0, 0), None, .50, .50)


def inkwell(img):

	output= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


	return output


def Lily(img):
	output=img.copy()

	
	# output[:,:,0]=img[:,:,0]*0.1   #BLUE
	# output[:,:,1]=img[:,:,1]*1.5   #GREEN
	# output[:,:,2]=img[:,:,2]*0.1   #RED

	#output= cv2.blur(output,(3,3))
	"""
	output[:,:,0]    
	output[:,:,1] = 120
	output[:,:,2]
	"""

	output[:,:,0] = output[:,:,0]*0.05+50  
	output[:,:,1] = output[:,:,1]*0.6 +50 
	output[:,:,2] = output[:,:,2]*0.35+100

	#print([a*2 if a>=100 else a for b in output[:,:,1] for a in b   ])	
	return output

# def trials(img):

# 	hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# 	blur = cv2.GaussianBlur(hsv,(11,11),0)

# 	blur[:,:,0] = 100		#blur[:,:,0]* 0.1
# 	blur[:,:,1] = 100 	#blur[:,:,1]* 0.1
# 	blur[:,:,2] #= 		#blur[:,:,2]* 1.5
	

# 	return blur


def Poprocket(img):

	hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	blur=hsv
	#blur = cv2.GaussianBlur(hsv,(11,11),0)

	blur[:,:,0] = 100		#blur[:,:,0]* 0.1
	blur[:,:,1] = 100 	#blur[:,:,1]* 0.1
	blur[:,:,2] #= 		#blur[:,:,2]* 1.5
	
	#return blur

	output=img.copy()
	# B G R 
	#output[:,:,0]= output[:,:,0]*0.3+50
	#output[:,:,1]= output[:,:,1]*0.2
	output[:,:,2]= output[:,:,2]*.6 +100

	return output


def Lordkelvin(img):


	output=img.copy()
	output[:,:,0] = output[:,:,0] *0.3 + 50  
	output[:,:,1] = output[:,:,1] *0.6 +50
	output[:,:,2] = output[:,:,2] *0.5 +100




	return output


def Walden(img):


	output=img.copy()
	output[:,:,0] = output[:,:,0] *0.6+100 
	#output[:,:,1] = output[:,:,1] *0.9
	#output[:,:,2] = output[:,:,2] *0.4




	return output

def Lomo_fi(img):

	#output=img.copy()
	#hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	#hsv[:,:,0]= hsv[:,:,0] 
	#	img[:,:,1]= cv2.inRange(img, (26, 10, 30), (97, 100, 255)) 
	#img=cv2.cvtColor(img,cv2.COLOR_HSV2BGR)


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


output1=Lily(inputImage)
output2=inkwell(inputImage)
output3=Poprocket(inputImage)
output4=Lordkelvin(inputImage)
output5=Walden(inputImage)
output6=Lomo_fi(inputImage)
numpy_horizontal = np.hstack((inputImage, output1, output3))
numpy_horizontal_concat = np.concatenate((inputImage, output1, output3), axis=1)

cv2.imshow('hi', numpy_horizontal_concat)
cv2.imshow('hii', output2)
cv2.imshow('hiii',output4)
cv2.imshow('hiiii',output5)
cv2.imshow('hiiiiiiiii',output6	)

cv2.waitKey()

