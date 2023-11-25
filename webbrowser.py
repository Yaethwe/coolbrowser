import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTabBar, QPushButton, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView

class BrowserTab(QWidget):
    def __init__(self, parent=None):
        super(BrowserTab, self).__init__(parent)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        layout.addWidget(self.browser)

        self.setLayout(layout)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))

class BrowserWindow(QMainWindow):
    def __init__(self):
        super(BrowserWindow, self).__init__()

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        self.setCentralWidget(self.tabs)
        self.create_new_tab()

        self.showMaximized()

        # Create a new tab when the "+" button is clicked
        new_tab_button = QPushButton("+")
        new_tab_button.clicked.connect(self.create_new_tab)

        # Access the tab bar and set the custom button on the right side
        tab_bar = self.tabs.tabBar()
        index = self.tabs.addTab(QWidget(), "New Tab")
        tab_bar.setTabButton(index, QTabBar.RightSide, new_tab_button)

    def create_new_tab(self, url=None):
        tab = BrowserTab()
        index = self.tabs.addTab(tab, "new tab")
        self.tabs.setCurrentIndex(index)

        if url:
            tab.browser.setUrl(QUrl(url))

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            self.close()

def main():
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

    window = BrowserWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()