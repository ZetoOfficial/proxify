import sys
import requests
import json
from PyQt6.QtWidgets import QApplication, QDialog
from mainUI import Ui_Dialog


# class DataDownloader:
#     def download_data(self):
#         # Replace this URL with the actual data source URL
#         data_url = "https://example.com/data.json"
#         response = requests.get(data_url)
#         if response.status_code == 200:
#             return json.loads(response.text)
#         else:
#             return None
#
#
# class DataAnalyzer:
#     def find_closest_objects(self, data):
#         # Implement your logic to find the closest objects of different varieties here
#         # For this example, we'll just return a placeholder result
#         return ["Object 1", "Object 2"]
#
#
# class DataApp(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Data Analysis App")
#         self.layout = QtWidgets.QVBoxLayout()
#
#         self.download_button = QtWidgets.QPushButton("Download Data")
#         self.download_button.clicked.connect(self.download_data)
#         self.layout.addWidget(self.download_button)
#
#         self.result_label = QtWidgets.QLabel()
#         self.layout.addWidget(self.result_label)
#
#         self.setLayout(self.layout)
#
#         self.data_downloader = DataDownloader()
#         self.data_analyzer = DataAnalyzer()
#
#     def download_data(self):
#         # data = self.data_downloader.download_data()
#         # if data:
#         result = self.data_analyzer.find_closest_objects([])
#         self.result_label.setText(f"Closest Objects: {', '.join(result)}")
#         # else:
#         #     self.result_label.setText("Failed to download data.")


def main():
    app = QApplication(sys.argv)
    dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
