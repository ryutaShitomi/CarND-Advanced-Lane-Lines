import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from pipeline import FindLane



find_lane = FindLane(ym_per_pix=30/720, xm_per_pix=3.7/700)
# challenge
# src = np.float32([[730, 480], [1050, 730], [265, 720], [630, 480]])
dst = np.float32([[900, 0], [900, 720], [320, 720], [320, 0]])
src = np.float32([[685, 450], [1120, 720], [190, 720], [595, 450]])
rows, cols, channel =720, 1280, 3
height = rows
# challenge
# vertices = np.array([[(200,rows) ,(650, 430), (750, 430), (1130, rows)]], dtype=np.int32)
vertices = np.array([[(0,height) ,(0, 0), (1200, 0), (1200, height)]], dtype=np.int32)
warped_size = (cols, rows)
find_lane.createWarp(src, dst, warped_size, vertices)
find_lane.createColorGrad(color_space='RGB')

# img = mpimg.imread('../test_challenge_images/test5.jpg')
# draw_region = find_lane.warp.draw_region(img)
# plt.figure(figsize=(12, 8))
# plt.imshow(draw_region)
# plt.show()


# for im_name in os.listdir('../test_images'):
#     path = os.path.join('../test_images', im_name)
#     img = mpimg.imread(path)
#     print(img.shape)
#     find_lane.left_fit = None
#     find_lane.right_fit = None
#     out_img = find_lane.pipeline(img)
#     res = find_lane.warp.draw_region(img)
#     plt.figure(figsize=(12, 8))
#     plt.imshow(res)
#     plt.show()
#     save_path = os.path.join('../test_images_output', im_name)
#     plt.imsave(save_path, out_img)
