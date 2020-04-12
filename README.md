# Contributers
* Siva Saai Ravipati, 11702930, Roll no:35
* Sadanala Naga Venkat, 11705142, Roll no:36
* Lakkireddy Upendranath, 11710784, Roll no:22

# Face Detector Using Facebook
int247-machine-learning-project-2020-kem031-venkat_36 created by GitHub Classroom

Face Detector Using Facebook

*  Our Assumption is that there will be atleast one photo of the user in first six images of the user in fb profile.

#  Project Documentation

for complete documentation you can got to the link:https://sites.google.com/view/ml-foundation-project/home?authuser=0

#  Video
for Video Presentation  of project you can go to link:https://youtu.be/hhfhBYXAd1A

#  photo_scraper_from_facebook.py (To Download Images from Facebook).

* It needs name of the user and fb_id of the user as input and saves the first 6 images in his/her facebook profile the images file.
side by side it adds the Details of the Image along with the name of the user to "photos.xlsx".

* It uses "cookiejar" module to save the login details to cookies.
* It uses "xlrd" and "xlutils" to miodify the excel sheet with new details.

#  face_detector.py(To Detect the face from live camera).

* It processes the images stored in images folder using the data present in "photos.xlsx" .Then detects the image using open-cv and face_recognition modules present in Python.
* It uses the "xlrd" module to read the data from excel sheet.

#  photos.xlsx:
* To maintain the record of the images along with their names.
#  images folder
* Images folder contains all the images trained to the model.
