import os
import cv2
import fire


class Downscaler():

    def downscale_folder(self, in_dir, out_dir, keepdims=False):
        
        hr_image_dir = in_dir
        lr_image_dir = out_dir

        os.makedirs(lr_image_dir)

        supported_img_formats = (".bmp", ".dib", ".jpeg", ".jpg", ".jpe", ".jp2",
                                 ".png", ".pbm", ".pgm", ".ppm", ".sr", ".ras", ".tif",
                                 ".tiff")

        # Downsample HR images
        for filename in os.listdir(hr_image_dir):
            if not filename.endswith(supported_img_formats):
                continue

            # Read HR image
            hr_img = cv2.imread(os.path.join(hr_image_dir, filename))
            hr_img_dims = (hr_img.shape[1], hr_img.shape[0])

            # Blur with Gaussian kernel of width sigma=1
            hr_img = cv2.GaussianBlur(hr_img, (0, 0), 1, 1)

            # Downsample image 4x
            lr_img_4x = cv2.resize(hr_img, (0, 0), fx=0.25, fy=0.25,
                                   interpolation=cv2.INTER_CUBIC)
            if args.keepdims:
                lr_img_4x = cv2.resize(lr_img_4x, hr_img_dims,
                                       interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(os.path.join(lr_image_dir + "/4x", filename), lr_img_4x)

if __name__ == '__main__':
  fire.Fire(Calculator)
