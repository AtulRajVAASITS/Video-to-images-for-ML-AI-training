import cv2
import os

video = cv2.VideoCapture('sample.mp4')

fps = video.get(cv2.CAP_PROP_FPS)
print('frames per second =',fps)
frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)
seconds = frames / fps
interval = int((seconds*1000)/1000)
minutes = 0
# vseconds = seconds % 60
frame_id = int(fps*(minutes*60 + seconds))
print("Video Length =",(minutes*60 + seconds))
print('frame id =',frame_id,'Interval between each frames in milliseconds',interval)

z = 0000
tfps =frame_id*1000
for x in range(1, 1001):
  print(z)
  while z < tfps:
        video.set(cv2.CAP_PROP_POS_MSEC, z)
        ret, frame = video.read();
        cv2.imshow('Frames Being split from video',frame);cv2.waitKey(250)
        filename = os.path.join("images", f'{x}.jpg')
        cv2.imwrite(filename, frame)
        z += interval
        break