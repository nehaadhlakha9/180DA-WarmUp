import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

cap = cv2.VideoCapture(0)

#object tracking
while(1):
    _, frame = cap.read()
    
    lower_blue = np.array([100,0,0])
    upper_blue = np.array([150,255,255])
    mask = cv2.inRange(frame, lower_blue, upper_blue)
    #mask color with video frame

    #bounding box
    contours = cv2.findContours(mask.copy(), 1, 2)[-2]

    if len(contours) > 0:
        area = max(contours, key=cv2.contourArea)
        x,y,w,h = cv2.boundingRect(area)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)    
        hsv = frame[y:y+h, x:x+w]
        
        cv2.imshow('frame', frame)

        hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
        hsv = hsv.reshape((hsv.shape[0] * hsv.shape[1],3)) #represent as row*column,channel number

        clt = KMeans(n_clusters=3) #cluster number
        clt.fit(hsv)

        hist = find_histogram(clt)
        bar = plot_colors2(hist, clt.cluster_centers_)

        plt.axis("off")
        plt.imshow(bar)
        plt.show()

cap.release()
cv2.destroyAllWindows()
