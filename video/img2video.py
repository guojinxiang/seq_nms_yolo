import cv2
import os, sys, getopt
import glob
import time

def generate_video(video_name):
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

def play_video(video_name):
    cap = cv2.VideoCapture(video_name)
    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        time.sleep(0.05)    #20fps
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    video_name = sys.argv[1]
    generate_video(video_name)
    play_video(video_name)


if __name__ == "__main__":
   main()
