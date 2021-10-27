from captcha.image import ImageCaptcha
import cv2
import random
import string

"""------------------------------- Generate Captcha -------------------------------"""



def generating_captcha():

    alphabet_string = string.ascii_lowercase                                          # Lowercase Alphanet for Captcha Text
    alphabet_list = list(alphabet_string)


    alphabet_string_upper = string.ascii_uppercase                                    # Uppercase Alphanet for Captcha Text
    alphabet_list_upper = list(alphabet_string_upper)

    number_list = [1,2,3,4,5,6,7,8,9]                                                 # Numbers for Captcha Text


    alphabet_list.extend(alphabet_list_upper)
    number_list_for_string_format = [str(number) for number in number_list]           # Merge one list to Generate Captcha Text
    alphabet_list.extend(number_list_for_string_format)
    text_for_captcha_list = random.sample(alphabet_list,5)

    joiner = ""
    text_captcha = joiner.join(text_for_captcha_list)                                  # The purpose of concatenation is to combine characters and numbers.


    captcha_text = text_captcha                                                        # Determining Captcha Text



    img = ImageCaptcha(width=300, height=100)                                          # Generating Captcha Image
    img.generate(captcha_text)


    captcha_iamge_name = "Captcha" + str(random.choice(range(1000))) + ".png"
    img.write(captcha_text,captcha_iamge_name)                                         # Saving Image as Png Format




    image = cv2.imread(captcha_iamge_name)                                             # Reading Captcha Image using OpenVC

    cv2.imshow(captcha_iamge_name, image)

    print(text_captcha)
    key = cv2.waitKey(0) & 0xFF

    if key == ord("s"):       # Press "s" to close window

        cv2.destroyAllWindows()



generating_captcha()