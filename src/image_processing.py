import cv2

def get_all_contours(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (360, 360))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    STEP = 3
    height, width = binary.shape
    scale = 0.6 # adjust later on
    print(f"Image dimensions: {width}x{height}")

    all_contours = []

    for contour in contours:
        if len(contour) < 10:
            continue
        points = []
        for point in contour[::STEP]:
            x = (point[0][0].item() - width/2)*scale
            y = (height/2 - point[0][1].item())*scale
            points.append((x, y))
        
        all_contours.append(points)

    return all_contours