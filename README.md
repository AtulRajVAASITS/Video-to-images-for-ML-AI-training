# Video-to-images-for-ML-AI-training
This is python script to make a 10 seconds long video to a 1000 equal images for training AI&amp; ML.
This is tested in python 3.8 with opencv 4.5.3.56.
To use this script download it and then rename the video you want to split to sample.mp4 and place it in the script containing directory. Then run the script. Make sure the video is less than 10 seconds not more.
If you want to change the number of splits from 1000 then change "interval = int((seconds*1000)/1000)" the second dividing 1000 to the desired number and change the "for x in range(1, 1001)" 1001 to the desired number.
Note the range function upper limit is exclusive of the desired number so if you need 100 splits then give 101 not 100.
