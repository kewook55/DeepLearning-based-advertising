그 파일이 main.py 인데 내용은
import cv2, glob, dlib

age_list = ['(0, 2)','(4, 6)','(8, 12)','(15, 20)','(25, 32)','(38, 43)','(48, 53)','(60, 100)']
gender_list = ['Male', 'Female']

detector = dlib.get_frontal_face_detector()

img_list = glob.glob('img/*.jpg')

for img_path in img_list:
  img = cv2.imread(img_path)

  faces = detector(img)

  for face in faces:
    x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()

    face_img = img[y1:y2, x1:x2].copy()

  crop = img[face.top():face.bottom(), face.left():face.right()]
  cv2.imwrite(img_path,crop)