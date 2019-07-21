import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
time = 0
ave = 0
x = []
y = []
plt.ion()

plt.title('average')
plt.xlabel('time')
plt.ylabel('para')
plt.ylim(0,255)
plt.grid()

while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ave = gray.mean()
    
    time  = time+1
    x.append(time)
    y.append(ave)
    plt.plot(x,y,color = 'red')
    plt.draw()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break

# When everything done, release the capture
plt.close()
cap.release()
cv2.destroyAllWindows()