import os
import cv2

base_files = [
            "apartment_0_rand_0009",
            "office_1_rand_0006",
            "room_0_rand_0009",
            "apartment_1_rand_0003",
            "office_2_rand_0009",
            "room_1_rand_0009",
            "hotel_0_rand_0003",
            "office_3_rand_0008",
            "office_0_rand_0006",
            "office_4_rand_0006",
              ]

output_dir = '/root/codes/OmniNeRF/logs_512x256'
for base_file in base_files:
    img_dir = '/root/codes/OmniNeRF/logs/' + base_file + '/testset_200000'
    img_list = os.listdir(img_dir)
    # keep only .png files
    img_list = [img_name for img_name in img_list if img_name.endswith('.png')]
    for img_name in img_list:
        # ignore img_name starting with d_
        if img_name.startswith('d_'):
            continue
        img = cv2.imread(os.path.join(img_dir, img_name))
        img = cv2.resize(img, (512, 256))
        os.makedirs(os.path.join(output_dir, base_file), exist_ok=True)
        cv2.imwrite(os.path.join(output_dir, base_file, img_name), img)