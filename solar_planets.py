import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Earth",(280,300),3,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Mars",(400,300),3,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Venus",(180,300),3,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Mercury",(110,170),3,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Jupiter",(450,90),3,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Saturn",(760,120),3,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Uranus",(950,120),3,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Neptune",(1100,120),3,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Sun",(110,90),3,fontScale=2,color=(0,0,255))
cv2.imshow("Solar System",img)
cv2.waitKey(0)