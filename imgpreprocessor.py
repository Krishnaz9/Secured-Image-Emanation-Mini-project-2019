import cv2
class Preprocessor:
     def process(self,file):

        img_resize=cv2.resize(file,(200,200))
        blur=cv2.blur(img_resize,(15,15))
        g_blur=cv2.GaussianBlur(img_resize,(5,5),0)
        b_filter=cv2.bilateralFilter(img_resize,76,76,4)
        cv2.imshow('original',img_resize)
        cv2.imshow('Blur',blur)
        cv2.imshow('G_Blur',g_blur)
        cv2.imshow('B_Filter',b_filter)
        cv2.waitKey(0)
