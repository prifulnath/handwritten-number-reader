# pip install opencv-python
# pip install pandas
# pip install scikit-learn
import cv2
import csv
import glob

# making heading of dataset csv
header = ["label"]
for i in range(0,784):
    header.append("pixel" + str(i))
    
# Open file in append mode
# write the header list to the file as the row
with open('dataset.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(header)

# go through each folder images
for label in range(10):
    # get the path of each digit folders
    dir_list = glob.glob("capturedImages/" + str(label) + "/*.png")

    # read each images and convert to grayscale
    # blur the image to increase smoothness
    # (15,15) is kernel size, 0 indicate it automatically calculates singma_x abd sigma_y
    # - value which is requred to blur an image
    for image_path in dir_list:
        image = cv2.imread(image_path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_gray = cv2.GaussianBlur(image_gray, (15,15), 0)
        reason_of_intrest = cv2.resize(image_gray, (28,28), interpolation=cv2.INTER_AREA)
        
        data = []
        data.append(label)
        rows, cols = reason_of_intrest.shape
        
        # add pixel to dataset array
        for i in range(rows):
            for j in range(cols):
                k = reason_of_intrest[i, j]
                k = 1 if k > 100 else 0
                data.append(k)
        with open('dataset.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    