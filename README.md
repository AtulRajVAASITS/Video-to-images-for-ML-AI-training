# Video-to-images-for-ML-AI-training
This is python script to make video to equal images for training AI&amp; ML.
This is tested in python 3.8 with opencv 4.5.3.56.
To use this script download it and then rename the video you want to split to sample.mp4 and place it in the script containing directory. Then run the script. It is better to have a video with a variety of posses of the content you want to train.
If you want to change the number of splits from 1000 then change "number_of_cuts = 1000"  to the desired number.
Also create a folder with name images in the current directory and create a folder inside it named Trainable_images.
The desired splits of the video will be placed in the images folder and trainabe images with less similarity will be placed in the Trainable_images folder.
