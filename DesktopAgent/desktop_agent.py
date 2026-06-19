import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class DesktopAgent(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DesktopAgent - Control Panel")
        self.setGeometry(300, 200, 900, 600)

        # Status label
        self.status = QLabel("Status: Idle", self)
        self.status.move(50, 50)

        # Start button
        self.start_btn = QPushButton("Start Agent", self)
        self.start_btn.move(50, 100)
        self.start_btn.clicked.connect(self.start_agent)

        # Stop button
        self.stop_btn = QPushButton("Stop Agent", self)
        self.stop_btn.move(200, 100)
        self.stop_btn.clicked.connect(self.stop_agent)

    def start_agent(self):
        self.status.setText("Status: Running...")

    def stop_agent(self):
        self.status.setText("Status: Stopped")

app = QApplication(sys.argv)

window = DesktopAgent()
window.show()

sys.exit(app.exec())