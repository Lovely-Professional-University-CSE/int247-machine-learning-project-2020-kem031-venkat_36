# int247-machine-learning-project-2020-kem031-venkat_36
int247-machine-learning-project-2020-kem031-venkat_36 created by GitHub Classroom

Face Detector Using Facebook

This Project Contains Two Python Programs to do two different actions:

#  photo_scraper_from_facebook.py (To Download Images from Facebook).

* It needs name of the user,fb_id of the user as input and saves the first 6 images in his/her fb profile the images file.
side by side it adds the Details of the Image along with the name of the user to "photos.xlsx".

* It uses "cookiejar" module to save the login details to cookies.
* It uses "xlrd" and "xlutils" to miodify the excel sheet with new details.

#  face_detector.py(To Detect the face from live camera).

* It processes the images stored in images folder using the data present in "photos.xlsx" .Then detects the image using open-cv and face_recognition modules.
* It uses the "xlrd" module to read the data from excel sheet.

#  photos.xlsx:
* To maintain the record of the images along with their names.
#  images folder
* Images folder contains all the images trained to the model.
