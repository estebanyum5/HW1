import cv2
import numpy as np

def predict_personal_color(image_bytes: bytes) -> dict:
    """
    Dummy/Lightweight model function for personal color inference.
    In a real scenario, you'd run a face detector and a deep learning model.
    Here we simulate it by analyzing the average color of the image.
    """
    # Convert bytes to numpy array
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        raise ValueError("Invalid image provided")

    # Simple mock logic based on average RGB (for demonstration)
    # OpenCV uses BGR
    avg_color_per_row = np.average(img, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    b, g, r = avg_color
    
    # Very naive logic for returning a personal color season
    if r > b and g > b:
        season = "Spring Warm"
    elif b > r and b > g:
        season = "Summer Cool"
    elif r > 150 and b < 100:
        season = "Autumn Warm"
    else:
        season = "Winter Cool"
        
    return {
        "season": season,
        "average_rgb": {"r": int(r), "g": int(g), "b": int(b)},
        "message": "This is a lightweight mock prediction based on average image color."
    }
