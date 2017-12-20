import cv2
import os, sys
import glob

def main():
    file_name = sys.argv[1]

    if not os.path.exists('input'):
        os.makedirs('input')

    vidcap = cv2.VideoCapture(file_name)
    success,image = vidcap.read()
    string_to_write = ''
    count = 0
    while True:
      success,image = vidcap.read()
      if not success:
          break
      print 'Read a new frame: {}'.format(count)
      cv2.imwrite(os.path.join('input', 'frame{}.jpg'.format(count)), image)     # save frame as JPEG file
      string_to_write += 'video/input/frame{}.jpg\n'.format(count)
      count += 1
    with open('pkllist.txt', 'w') as f:
        f.write(string_to_write)
        print "pkllist.txt created."

if __name__ == "__main__":
   main()
