import cv2 
import imutils as iu
from google.colab.patches import cv2_imshow


print("Choices are:\n 1.image\n2.video")
choice=input("Enter your if want to use image or video:")
if choice=="image":

    h=cv2.HOGDescriptor()       #HOG human detector
    h.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    img=cv2.imread("/content/img2.jpg")      #Read image (2 backward slash required!)

    #Image Preprocessing
    size=int(input("Write suitable size for winstride:"))
    img=iu.resize(img,width=min(size,img.shape[1]))

    (regions,_)=h.detectMultiScale(img,winStride=(1,1),padding=(32,32),scale=1.05) #group method which allows to select the clusters of object
    print("Humans detected: ",len(regions))

    #creating regions

    for (x,y,w,h) in regions:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    #Output

    cv2_imshow(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    

elif choice=="video":
    
    #Video detection
    h=cv2.HOGDescriptor()                                               #HOG human detector
    h.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    vid=cv2.VideoCapture("/content/vid2.mp4")                                    #Read video(2 backward slash required!)

    while vid.isOpened():
        ret,image=vid.read()
        if ret:
            size=int(input("Write suitable size for winstride:"))
            image=iu.resize(image,width=min(size,image.shape[1]))      

            #creating regions
            (regions,_)=h.detectMultiScale(image,winStride=(1,1),padding=(32,32),scale=1.05) #group method which allows to select the clusters of object
            print("Humans detected: ",len(regions))

            for (x,y,w,h) in regions:
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
                 # Showing the output Image
            cv2_imshow(image)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    vid.release()
    cv2.destroyAllWindows()                            


