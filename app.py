import os
import sys

import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector
import numpy as np

from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractButton
from PySide6.QtCore import Qt, QThread, Signal, Slot, QTimer, QUrl
from PySide6.QtGui import QImage, QPixmap, QPainter, QPainterPath, QPen, QColor
from PySide6.QtMultimedia import QSoundEffect

from ui.main_window import Ui_MainWindow

current_path = os.path.dirname(__file__)
assets_dir = os.path.join(current_path, "assets")


def convert_cv_image_to_qt(cv_img, height):
    rgb_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_img.shape
    bytes_per_line = ch * w
    img = QImage(rgb_img, w, h, bytes_per_line, QImage.Format.Format_RGB888)
    img_resized = img.scaledToHeight(height)
    return QPixmap.fromImage(img_resized)


def adjust_scale(x, y, w, h, r):
    x = x - int(w * r // 2)
    y = y - int(h * r // 2)
    w = int(w * (1 + r))
    h = int(h * (1 + r))
    return x, y, w, h


class VideoCaptureThread(QThread):
    frame_updated_signal = Signal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        while self.running:
            success, image = cap.read()
            if not success:
                continue

            image = image[:, 360:920]
            image = cv2.flip(image, 1)

            self.frame_updated_signal.emit(image)

        cap.release()

    def stop(self):
        self.running = False
        self.wait()


class SelectablePhotoButton(QAbstractButton):
    photo_selection_changed_signal = Signal(np.ndarray, bool)

    def __init__(self, pixmap, index):
        super().__init__()
        self.pixmap = pixmap
        self.photo_index = index
        self.selected_photo_index = None

        self.setCheckable(True)
        self.toggled.connect(self.on_toggle)

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
                str(self.selected_photo_index)
            )
        
        painter.end()

    def sizeHint(self):
        return self.pixmap.size()
    
    def on_toggle(self, checked):
        self.photo_selection_changed_signal.emit(self.photo_index, checked)
        self.update()

    def set_selected_index(self, value):
        self.selected_photo_index = value
        self.update()


class FourCutWindow(QMainWindow, Ui_MainWindow):
    total_photos = 8
    total_cuts = 4
    photo_shot_interval = 3000
    column_count = 4

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("2024 대건네컷")

        self.navCamera.clicked.connect(self.switch_to_camera_page)
        self.navSelect.clicked.connect(self.switch_to_select_page)
        self.navResult.clicked.connect(self.switch_to_result_page)
        self.startButton.clicked.connect(self.begin_photo_session)
        self.selectButton.clicked.connect(self.confirm_photo_selection)
        self.selectButton.setDisabled(True)

        self.video_thread = VideoCaptureThread()
        self.video_thread.frame_updated_signal.connect(self.update_frame)
        self.video_thread.start()

        self.video_frame = None
        self.photo_timer = QTimer(self)
        self.photo_timer.setInterval(self.photo_shot_interval)
        self.photo_timer.timeout.connect(self.capture_photo)

        self.captured_photos = []
        self.selected_photo_indexes = []
        self.photo_buttons = []

        self.countdown_timer = QTimer(self)
        self.countdown_timer.setInterval(1000)
        self.countdown_timer.timeout.connect(self.count_seconds)
        self.countdown_value = 0

        self.shutter_sound_effect = QSoundEffect()
        audio_file = os.path.join(assets_dir, "camera.wav")
        self.shutter_sound_effect.setSource(QUrl.fromLocalFile(audio_file))
        self.shutter_sound_effect.setLoopCount(0)
        self.shutter_sound_effect.setVolume(0.7)

        frame_file = os.path.join(assets_dir, "frame.png")
        self.result_image = cv2.imread(frame_file, cv2.IMREAD_COLOR)
        self.filterButton_1.clicked.connect(self.apply_color_filter)
        self.filterButton_2.clicked.connect(self.apply_gray_filter)
        mask_file = os.path.join(assets_dir, "mask.png")
        self.mask_image = cv2.imread(mask_file, cv2.IMREAD_UNCHANGED)
        self.filterButton_3.clicked.connect(self.apply_daegun_filter)
        self.saveButton.clicked.connect(self.save_result_image)

    def closeEvent(self, event):
        self.video_thread.stop()
        event.accept()

    def switch_to_camera_page(self):
        self.navCamera.setChecked(True)
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_select_page(self):
        self.navSelect.setChecked(True)
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_result_page(self):
        self.navResult.setChecked(True)
        self.stackedWidget.setCurrentIndex(2)

    @Slot(np.ndarray)
    def update_frame(self, frame):
        self.video_frame = frame
        height = self.videoLabel.height()
        qt_img = convert_cv_image_to_qt(frame, height)

        if self.countdown_value > 0:
            painter = QPainter(qt_img)

            pen = QPen(QColor(255, 255, 255, 127))
            painter.setPen(pen)

            font = painter.font()
            font.setPointSize(120)
            font.setBold(True)
            painter.setFont(font)

            painter.drawText(
                qt_img.rect(),
                Qt.AlignmentFlag.AlignCenter,
                str(self.countdown_value)
            )
            
            painter.end()

        self.videoLabel.setPixmap(qt_img)

    def begin_photo_session(self):
        self.switch_to_camera_page()

        while self.selectLayout.count():
            child = self.selectLayout.takeAt(0)
            child.widget().deleteLater()

        self.selected_photo_indexes.clear()
        self.selectButton.setDisabled(True)
        self.captured_photos.clear()
        self.photo_buttons.clear()

        self.startButton.setDisabled(True)
        self.photo_timer.start()
        self.initiate_countdown()

    def capture_photo(self):
        self.captured_photos.append(self.video_frame)
        self.shutter_sound_effect.play()
        white_screen = np.full_like(self.video_frame, 255)
        height = self.videoLabel.height()
        qt_white = convert_cv_image_to_qt(white_screen, height)
        self.videoLabel.setPixmap(qt_white)
        self.video_thread.blockSignals(True)
        QTimer.singleShot(20, lambda: self.video_thread.blockSignals(False))
        self.initiate_countdown()

        if len(self.captured_photos) >= self.total_photos:
            self.photo_timer.stop()
            self.display_all_photos()

    def initiate_countdown(self):
        self.countdown_value = self.photo_shot_interval // 1000
        self.countdown_timer.start()

    def count_seconds(self):
        self.countdown_value -= 1
        if self.countdown_value == 0:
            self.countdown_timer.stop()

    def display_all_photos(self):
        self.switch_to_select_page()

        for i in range(len(self.captured_photos)):
            row = i // self.column_count
            col = i % self.column_count

            rows_needed = self.total_photos / self.column_count
            height_per_photo = self.widget.height() // rows_needed
            height_per_photo -= self.selectLayout.verticalSpacing()
            qt_photo = convert_cv_image_to_qt(self.captured_photos[i], height_per_photo)

            photo_button = SelectablePhotoButton(qt_photo, i)
            photo_button.photo_selection_changed_signal.connect(self.update_photo_selection)
            self.selectLayout.addWidget(photo_button, row, col)
            self.photo_buttons.append(photo_button)

        self.startButton.setDisabled(False)

    @Slot(np.ndarray, bool)
    def update_photo_selection(self, photo_index, is_selected):
        if is_selected:
            self.selected_photo_indexes.append(photo_index)
        else:
            self.selected_photo_indexes.remove(photo_index)

        for i, selected_index in enumerate(self.selected_photo_indexes):
            self.photo_buttons[selected_index].set_selected_index(i + 1)

        if len(self.selected_photo_indexes) == self.total_cuts:
            self.selectButton.setDisabled(False)
        else:
            self.selectButton.setDisabled(True)

    def confirm_photo_selection(self):
        self.apply_color_filter()
        self.switch_to_result_page()

    def insert_photo_to_frame(self, photo, cut_number):
        w, h = 560, 720
        points = [(80, 160), (670, 160),
                  (80, 910), (670, 910)]
        
        x, y = points[cut_number]
        photo_resized = cv2.resize(photo, (w, h), interpolation=cv2.INTER_CUBIC)
        self.result_image[y:y+h, x:x+w] = photo_resized

    def display_result_image(self):
        qt_img = convert_cv_image_to_qt(self.result_image, 560)
        self.resultLabel.setPixmap(qt_img)

    def apply_color_filter(self):
        for i in range(self.total_cuts):
            photo_index = self.selected_photo_indexes[i]
            photo = self.captured_photos[photo_index]
            self.insert_photo_to_frame(photo, i)
        self.display_result_image()

    def apply_gray_filter(self):
        for i in range(self.total_cuts):
            photo_index = self.selected_photo_indexes[i]
            photo = self.captured_photos[photo_index]
            photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
            photo = cv2.cvtColor(photo, cv2.COLOR_GRAY2BGR)
            self.insert_photo_to_frame(photo, i)
        self.display_result_image()

    def apply_daegun_filter(self):
        detector = FaceDetector(minDetectionCon=0.6, modelSelection=0)
        for i in range(self.total_cuts):
            photo_index = self.selected_photo_indexes[i]
            photo = self.captured_photos[photo_index]
            img, bboxs = detector.findFaces(photo.copy(), draw=False)
            if bboxs is None:
                continue
            for bbox in bboxs:
                x, y, w, h = bbox['bbox']
                offset_y = int(h * 0.3)
                x, y, w, h = adjust_scale(x, y, w, h, 0.6)
                mask = cv2.resize(self.mask_image, (w, h))
                img = cvzone.overlayPNG(img, mask, pos=[x, y - offset_y])
            self.insert_photo_to_frame(img, i)
        self.display_result_image()

    def save_result_image(self):
        cv2.imwrite("result.png", self.result_image)

        for i in self.selected_photo_indexes:
            self.photo_buttons[i].blockSignals(True)
            self.photo_buttons[i].setChecked(False)
            self.photo_buttons[i].set_selected_index(None)
            self.photo_buttons[i].blockSignals(False)

        self.selected_photo_indexes.clear()
        self.selectButton.setDisabled(True)
        self.switch_to_camera_page()

        # TODO: send file to server or printer


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FourCutWindow()
    window.show()
    sys.exit(app.exec())
