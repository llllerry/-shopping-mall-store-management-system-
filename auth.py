# src/auth.py
from database import get_user_by_username
import cv2
import dlib

def verify_login(username, password):
    """验证账号密码"""
    user = get_user_by_username(username)
    if user and user['password'] == password:
        return True
    return False

def face_recognition(image_path):
    """人脸识别逻辑"""
    detector = dlib.get_frontal_face_detector()
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    return len(faces) > 0
