import sys
from pathlib import Path

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

BASE_PATH = Path(__file__).resolve().parent.parent
ICON_PATH = BASE_PATH / "assets" / "ico"
IMG_PATH = BASE_PATH / "assets" / "img"

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Image & Icon paths
        self.img_chili = QPixmap(str(IMG_PATH / "chili.jpg"))
        self.img_norris = QPixmap(str(IMG_PATH / "cuke.jpg"))
        self.img_shroom = QPixmap(str(IMG_PATH / "addy.jpg"))
        self.img_hills = QPixmap(str(IMG_PATH / "banana.jpg"))

        icon_chili = QIcon(str(ICON_PATH / "chili.png"))
        icon_shroom = QIcon(str(ICON_PATH / "addy.png"))
        icon_rad = QIcon(str(ICON_PATH / "banana.png"))
        icon_karate = QIcon(str(ICON_PATH / "cuke.png"))

        #Basic window config
        self.setMinimumSize(850, 620)
        self.setWindowTitle("Schedule 1 Ingredient Mixing Utility")
        self.setWindowIcon(icon_shroom)

        # Central widget
        self.label = QLabel("Hello moto.")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)     

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, toolbar)

        # Spawn chili
        button_action_chili = QAction(QIcon(icon_chili), "&Chili", self)
        button_action_chili.setStatusTip("This button spawns chili")
        button_action_chili.triggered.connect(self.spawn_chili)
        button_action_chili.setShortcut(QKeySequence("Ctrl+s"))
        toolbar.addAction(button_action_chili)
        

        toolbar.addSeparator()

        # Use karate
        button_action_karate = QAction(QIcon(icon_karate), "Cuke", self)
        button_action_karate.setStatusTip("This button kills them with karate")
        button_action_karate.triggered.connect(self.roundhouse_kick)
        toolbar.addAction(button_action_karate)

        toolbar.addSeparator()

        # Nuke action
        button_action_nuke = QAction(QIcon(icon_shroom), "Addy", self)
        button_action_nuke.setStatusTip("Click this if you want to die a slow death by radiation poisoning")
        button_action_nuke.triggered.connect(self.nuke)
        toolbar.addAction(button_action_nuke)

        # Clean action
        button_action_clean_up = QAction(QIcon(icon_rad), "Banana", self)
        button_action_clean_up.setStatusTip("Click to clean up radiation.")
        button_action_clean_up.triggered.connect(self.clean_rad)
        toolbar.addAction(button_action_clean_up)

        # Add status bar
        self.setStatusBar(QStatusBar(self))

        # Menus
        menu = self.menuBar()

        file_menu = menu.addMenu("&Create")    
        file_menu.addAction(button_action_chili)

        file_menu2 = menu.addMenu("&Tools")    
        file_menu2.addAction(button_action_karate)
        file_menu2.addAction(button_action_nuke)

        file_menu3 = menu.addMenu("&Help")    
        file_menu3.addAction(button_action_clean_up)

        file_submenu = file_menu.addMenu("Sub-Species")
        file_submenu.addAction("L. d. delicatula")
        file_submenu.addAction("L. d. jole")
        file_submenu.addAction("L. d. operosa")


    # Functions to handle widget changes

    def spawn_chili(self, s):
        pixmap = self.img_chili
        self.label.setPixmap(pixmap)
        print("chili!")

    def roundhouse_kick(self, s):
        pixmap = self.img_norris
        self.label.setPixmap(pixmap)
        print("cuke!")

    def nuke(self, s):
        pixmap = self.img_shroom
        self.label.setPixmap(pixmap)
        print("addy!")

    def clean_rad(self, s):
        pixmap = self.img_hills
        self.label.setPixmap(pixmap)
        print("banana!")

# Create instance of QApplication, pass in sys.argv, (Python list containing CLI arguments passed to app)
app = QApplication(sys.argv)

# Create  instance of QWidget
window = MainWindow()
window.show()

# Start the event loop
app.exec()