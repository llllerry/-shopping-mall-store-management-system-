from pathlib import Path
from tkinter import filedialog, messagebox
import dlib, cv2, numpy as np

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "models"
PREDICTOR_PATH = MODEL_DIR / "shape_predictor_68_face_landmarks.dat"
FACE_REC_PATH = MODEL_DIR / "dlib_face_recognition_resnet_model_v1.dat"

def _pick_file(title, pattern):
    fp = filedialog.askopenfilename(title=title, filetypes=[("Model", pattern), ("All Files", "*")])
    return Path(fp) if fp else None

def ensure_models():
    MODEL_DIR.mkdir(exist_ok=True)
    pred = PREDICTOR_PATH if PREDICTOR_PATH.exists() else _pick_file("选择 shape_predictor_68_face_landmarks.dat", "*.dat")
    face = FACE_REC_PATH   if FACE_REC_PATH.exists()   else _pick_file("选择 dlib_face_recognition_resnet_model_v1.dat", "*.dat")
    if not pred or not face:
        messagebox.showerror("模型缺失", "未找到必要的人脸模型文件，请按 README 放置到 models/ 目录。")
        raise FileNotFoundError("Face models not found")
    return pred, face

def load_detectors():
    pred_path, face_path = ensure_models()
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(str(pred_path))
    facerec = dlib.face_recognition_model_v1(str(face_path))
    return detector, predictor, facerec

def get_face_descriptor(img_path):
    detector, predictor, facerec = load_detectors()
    img = cv2.imread(str(img_path))
    if img is None:
        return None
    dets = detector(img, 1)
    if len(dets) == 0:
        return None
    shape = predictor(img, dets[0])
    desc = facerec.compute_face_descriptor(img, shape)
    return np.array(desc)
