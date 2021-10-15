from ipynta import ImageGlobber
from pathlib import Path

SAMPLES_DIR = (Path(__file__).parent / "./imgs")

def test_image_path():
    globber = ImageGlobber(SAMPLES_DIR)
    img_paths = globber.get_img_paths()

    assert(len(img_paths) == 1)