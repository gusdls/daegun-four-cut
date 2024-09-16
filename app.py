import os
import sys

import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractButton
from PySide6.QtCore import Qt, QThread, Signal, Slot, QTimer, QUrl
from PySide6.QtGui import QImage, QPixmap, QPainter, QPainterPath, QPen, QColor
from PySide6.QtMultimedia import QSoundEffect
import numpy as np

from ui.main_window import Ui_MainWindow

current_path = os.path.dirname(__file__)
assets_folder = os.path.join(current_path, "assets")


def convert_cv_to_qt(cv_img, height):
    rgb_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_img.shape
    bytes_per_line = ch * w
    img = QImage(rgb_img, w, h, bytes_per_line, QImage.Format.Format_RGB888)
    img_resized = img.scaledToHeight(height)
    return QPixmap.fromImage(img_resized)


class VideoThread(QThread):
    change_frame_signal = Signal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._running = True

    def run(self):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        while self._running:
            ret, frame = cap.read()
            if not ret:
                continue

            frame = frame[:, 360:920]
            frame = cv2.flip(frame, 1)
            self.change_frame_signal.emit(frame)

        cap.release()

    def stop(self):
        self._running = False
        self.wait()


class PhotoButton(QAbstractButton):
    change_photos_signal = Signal(np.ndarray, bool)

    def __init__(self, pixmap, index):
        super().__init__()
        self.pixmap = pixmap
        self.index = index
        self.select_index = None

        self.setCheckable(True)
        self.toggled.connect(self.handle_toggle)

    def paintEvent(self, event):
        painter = QPainter(self)
        
        clip_path = QPainterPath()
        clip_path.addRoundedRect(event.rect(), 4, 4)
        painter.setClipPath(clip_path)
        painter.drawPixmap(event.rect(), self.pixmap)

        if self.isChecked():
            painter.setBrush(QColor(0, 0, 0, 77))
            painter.drawRect(event.rect())

            pen = QPen(QColor(255, 255, 255))
            painter.setPen(pen)

            font = painter.font()
            font.setPointSize(80)
            font.setBold(True)
            painter.setFont(font)
            
            painter.drawText(
                event.rect(),
                Qt.AlignmentFlag.AlignCenter,
                str(self.select_index)
            )
        
        painter.end()

    def sizeHint(self):
        return self.pixmap.size()
    
    def handle_toggle(self, checked):
        self.change_photos_signal.emit(self.index, checked)
        self.update()

    def setSelectIndex(self, value):
        self.select_index = value
        self.update()


class FourCutWindow(QMainWindow, Ui_MainWindow):
    total_photos = 8
    total_cuts = 4
    shot_interval = 5000
    number_of_columns = 4

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("2024 대건네컷")

        self.navCamera.clicked.connect(self.switch_to_camera_page)
        self.navResult.clicked.connect(self.switch_to_result_page)
        self.startButton.clicked.connect(self.start_taking_photos)
        self.saveButton.clicked.connect(self.save_photos)
        self.saveButton.setDisabled(True)

        self.thread = VideoThread()
        self.thread.change_frame_signal.connect(self.update_frame)
        self.thread.start()

        self.current_frame = None
        self.camera_timer = QTimer(self)
        self.camera_timer.setInterval(self.shot_interval)
        self.camera_timer.timeout.connect(self.take_photo)

        self.photos = []
        self.selected_indexes = []
        self.photo_buttons = []

        self.countdown_timer = QTimer(self)
        self.countdown_timer.setInterval(1000)
        self.countdown_timer.timeout.connect(self.count_seconds)
        self.countdown_seconds = 0

        self.effect = QSoundEffect()
        audio_file = os.path.join(assets_folder, "camera.wav")
        self.effect.setSource(QUrl.fromLocalFile(audio_file))
        self.effect.setLoopCount(0)
        self.effect.setVolume(0.7)

    def switch_to_camera_page(self):
        self.navCamera.setChecked(True)
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_result_page(self):
        self.navResult.setChecked(True)
        self.stackedWidget.setCurrentIndex(1)

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @Slot(np.ndarray)
    def update_frame(self, frame):
        self.current_frame = frame
        height = self.videoLabel.height()
        qt_img = convert_cv_to_qt(frame, height)

        if self.countdown_seconds > 0:
            painter = QPainter(qt_img)

            pen = QPen(QColor(255, 255, 255))
            painter.setPen(pen)

            font = painter.font()
            font.setPointSize(120)
            font.setBold(True)
            painter.setFont(font)

            painter.drawText(
                qt_img.rect(),
                Qt.AlignmentFlag.AlignCenter,
                str(self.countdown_seconds)
            )
            
            painter.end()

        self.videoLabel.setPixmap(qt_img)

    def start_taking_photos(self):
        while self.gridLayout.count():
            child = self.gridLayout.takeAt(0)
            child.widget().deleteLater()

        self.saveButton.setDisabled(True)
        self.photos.clear()
        self.photo_buttons.clear()

        self.startButton.setDisabled(True)
        self.camera_timer.start()
        self.start_countdown()

    def take_photo(self):
        self.photos.append(self.current_frame)
        self.effect.play()
        self.start_countdown()

        if len(self.photos) >= self.total_photos:
            self.camera_timer.stop()
            self.show_result_photos()

    def start_countdown(self):
        self.countdown_seconds = self.shot_interval // 1000
        self.countdown_timer.start()

    def count_seconds(self):
        self.countdown_seconds -= 1
        if self.countdown_seconds == 0:
            self.countdown_timer.stop()

    def show_result_photos(self):
        self.switch_to_result_page()

        for i in range(len(self.photos)):
            row = i // self.number_of_columns
            col = i % self.number_of_columns

            number_of_rows = self.total_photos / self.number_of_columns
            height = self.widget.height() // number_of_rows
            height -= self.gridLayout.verticalSpacing()
            qt_img = convert_cv_to_qt(self.photos[i], height)

            photo_button = PhotoButton(qt_img, i)
            photo_button.change_photos_signal.connect(self.update_photos)
            self.gridLayout.addWidget(photo_button, row, col)
            self.photo_buttons.append(photo_button)

        self.startButton.setDisabled(False)

    @Slot(np.ndarray, bool)
    def update_photos(self, index, adding):
        if adding:
            self.selected_indexes.append(index)
        else:
            self.selected_indexes.remove(index)

        for i in range(len(self.selected_indexes)):
            btn = self.selected_indexes[i]
            self.photo_buttons[btn].setSelectIndex(i + 1)

        if len(self.selected_indexes) == self.total_cuts:
            self.saveButton.setDisabled(False)
        else:
            self.saveButton.setDisabled(True)

    def save_photos(self):
        w, h = 560, 720
        pos_list = [(80, 160), (670, 160), (80, 910), (670, 910)]

        frame_file = os.path.join(assets_folder, "frame.png")
        frame_image = cv2.imread(frame_file, cv2.IMREAD_COLOR)

        for i in range(self.total_cuts):
            x, y = pos_list[i]
            photo_idx = self.selected_indexes[i]
            photo = self.photos[photo_idx]
            photo_resized = cv2.resize(photo, (w, h), interpolation=cv2.INTER_CUBIC)
            frame_image[y:y+h, x:x+w] = photo_resized

        cv2.imwrite("result.png", frame_image)

        for i in self.selected_indexes:
            self.photo_buttons[i].blockSignals(True)
            self.photo_buttons[i].setChecked(False)
            self.photo_buttons[i].setSelectIndex(None)
            self.photo_buttons[i].blockSignals(False)

        self.selected_indexes.clear()
        self.saveButton.setDisabled(True)
        self.switch_to_camera_page()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FourCutWindow()
    window.show()
    sys.exit(app.exec())
