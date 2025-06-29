import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSplitter,
    QFrame,
)
from PySide6.QtCore import Qt


class DependencyWidget(QWidget):
    def __init__(self, name):
        super().__init__()
        layout = QHBoxLayout(self)
        self.name_label = QLabel(name)
        self.status_label = QLabel("Not Installed")
        self.action_button = QPushButton("Install")
        layout.addWidget(self.name_label)
        layout.addStretch()
        layout.addWidget(self.status_label)
        layout.addWidget(self.action_button)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Appium Dependency Installer")
        self.setMinimumSize(800, 600)

        # Main layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # Dependency list
        dependencies = [
            "Node.js",
            "Android SDK",
            "Appium Server",
            "Appium Drivers",
            "Xcode",
        ]

        for dep in dependencies:
            main_layout.addWidget(DependencyWidget(dep))

        main_layout.addStretch()

        # Documentation view (placeholder)
        docs_view = QLabel("Documentation will be shown here")
        docs_view.setAlignment(Qt.AlignCenter)

        # Splitter
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(main_widget)
        splitter.addWidget(docs_view)
        splitter.setSizes([600, 200])

        self.setCentralWidget(splitter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
