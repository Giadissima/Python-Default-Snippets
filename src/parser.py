import argparse
class Parser:
    def __init__(self, description=""):
        self.parser = argparse.ArgumentParser(description=description)

    def arguments(self):
        self.parser.add_argument(
            "-is", "--imagesize", required=False, type=int, help="Set image size")
        self.parser.add_argument(
            "-bp", "--basepath", required=False, type=str, help="Set basepath where images will save (default value=\"src\")")
        self.parser.add_argument(
            "-i", "--imagespath", required=False, type=str, help="Set where images are saved")
        self.parser.add_argument(
            "-l", "--logpath", required=False, type=str, help="Set where you want to save info and error logs")
        self.parser.add_argument(
            "-ic", "--imgcategories", required=False, type=list, help="Set images's categories of each folder")
        self.parser.add_argument(
            "-dev", "--dev_mode", required=False, type=str, help="Set development mode. Default value: True")

        return vars(self.parser.parse_args())

        