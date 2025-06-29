import sys
import os
import http.server
import socketserver
import threading
import webbrowser
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QStackedWidget,
    QListWidget,
    QListWidgetItem,
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Appium Dependency Installer")
        self.setMinimumSize(600, 400)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.create_install_view()
        self.create_manual_steps_view()

        self.httpd = None
        self.server_thread = None

    def create_install_view(self):
        view = QWidget()
        layout = QVBoxLayout(view)

        title = QLabel("The following dependencies will be installed:")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.install_list = QListWidget()
        dependencies = [
            "Node.js v20.11.0",
            "Android SDK Platform-Tools",
            "Appium v2.5.1",
            "Appium Drivers (UIAutomator2, XCUITest)",
        ]
        for dep in dependencies:
            self.install_list.addItem(dep)
        layout.addWidget(self.install_list)

        install_button = QPushButton("Install Dependencies")
        install_button.clicked.connect(self.show_manual_steps_view)
        layout.addWidget(install_button)

        self.stacked_widget.addWidget(view)

    def create_manual_steps_view(self):
        view = QWidget()
        layout = QVBoxLayout(view)

        title = QLabel("Manual steps remaining:")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.manual_steps_list = QListWidget()
        manual_steps = {
            "Install Xcode": "index.md",
            "Enable Developer Mode on iOS Device": "index.md",
            "Enable Developer Mode on Android Device": "index.md",
        }

        for step, doc_path in manual_steps.items():
            item_widget = QWidget()
            item_layout = QHBoxLayout(item_widget)
            item_layout.addWidget(QLabel(step))
            item_layout.addStretch()
            view_docs_button = QPushButton("View Docs")
            view_docs_button.clicked.connect(lambda checked=False, path=doc_path: self.view_docs(path))
            item_layout.addWidget(view_docs_button)
            list_item = QListWidgetItem(self.manual_steps_list)
            list_item.setSizeHint(item_widget.sizeHint())
            self.manual_steps_list.setItemWidget(list_item, item_widget)

        layout.addWidget(self.manual_steps_list)

        self.stacked_widget.addWidget(view)

    def show_manual_steps_view(self):
        # In the future, this will run the installation process
        self.stacked_widget.setCurrentIndex(1)

    def start_server(self):
        if self.server_thread is None:
            PORT = 8000
            # Get the path to the docs/site directory
            doc_root = os.path.join(os.path.dirname(sys.argv[0]), '..', 'docs', 'site')

            class Handler(http.server.SimpleHTTPRequestHandler):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, directory=doc_root, **kwargs)

            self.httpd = socketserver.TCPServer(("", PORT), Handler)

            self.server_thread = threading.Thread(target=self.httpd.serve_forever)
            self.server_thread.daemon = True
            self.server_thread.start()
            print(f"Serving documentation at http://localhost:{PORT}")

    def view_docs(self, path):
        self.start_server()
        url = f"http://localhost:8000/{path.replace('.md', '.html')}"
        webbrowser.open(url)

    def closeEvent(self, event):
        if self.httpd:
            self.httpd.shutdown()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
