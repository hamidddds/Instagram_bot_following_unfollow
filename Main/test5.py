import os
from Lib_Finding_image_on_screen import find_images
likecommentfowrward_position = (450, 650, 600, 350)
like_bottom_location = find_images(
    r'Images\like_button.png', chrome_region=(likecommentfowrward_position))
