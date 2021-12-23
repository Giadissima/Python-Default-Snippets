from imutils import resize as res

from src.constants import IMG_SIZE

def resize(frame, width, height, max_size = IMG_SIZE):
    if width > max_size or height > max_size:
        if width > height:
            return res(frame, width=max_size)
        else:
            return res(frame, height=max_size)
    else:
        return frame