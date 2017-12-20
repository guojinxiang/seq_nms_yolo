import cv2
import os, sys, getopt
import glob

def main():
    video_name = sys.argv[1]
    image_folder = 'output'
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    count = 0
    for element in os.listdir('output'):
        if(str(element).endswith('jpg')):
            count = count + 1
    images = ['frame{}.jpg'.format(i) for i in range(count)]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    video = cv2.VideoWriter(video_name, fourcc, 30.0, (width,height))
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    cv2.destroyAllWindows()
    video.release()

if __name__ == "__main__":
   main()
