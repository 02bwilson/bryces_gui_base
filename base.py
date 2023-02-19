from PyQt6.QtWidgets import QMainWindow
import yaml

class MainWindowBase(QMainWindow):
    _VERSION_ = "1.0"

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.cfg = kwargs.get('cfg')
        self.parse_args()

    def parse_args(self):
        with open(self.cfg, "r") as stream:
            try:
                print(yaml.safe_load(stream))
            except yaml.YAMLError as exc:
                print(exc)
