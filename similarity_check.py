import cv2
import os
from skimage import metrics
import numpy as np

def similarity_check(total_images):

        for i in range(1,total_images):
                print(i)
                for j in range(i + 1, total_images):
                        image1 = cv2.imread(f'images/{i}.jpg')
                        image2 = cv2.imread(f'images/{j}.jpg')
                # Structural Similarity Index
                        print(i,j)
                        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]), interpolation = cv2.INTER_AREA)
                        # print(image1.shape, image2.shape)
                        # Convert images to grayscale
                        image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
                        image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
                        # Calculate SSIM
                        ssim_score = metrics.structural_similarity(image1_gray, image2_gray, full=True)
                        print("SSIM Score: ", round(ssim_score[0], 2))
                        score = round(ssim_score[0], 2)
                        if score <= 0.80:
                                result_image = np.concatenate((image1, image2), axis=1)
                                cv2.imshow("image",result_image)
                                cv2.waitKey(500)
                                filename = os.path.join("images/Trainable_images", f'{i}.jpg')
                                cv2.imwrite(filename, image1)
                                filename = os.path.join("images/Trainable_images", f'{j}.jpg')
                                cv2.imwrite(filename, image2)
                                i = j
                                print(i)
            
if __name__ == "__main__":
        similarity_check(total_images)
