import csv
import datetime as dt
import json
import os
import sys
from collections import deque
from os.path import expanduser

import numpy as np
import pyqtgraph as pg
import serial
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import pyqtSignal

import tools

"""
Set Logger
"""
import logging

# set logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
FORMAT = "[%(asctime)s]  %(message)s"
formatter = logging.Formatter(fmt=FORMAT, datefmt=TIME_FORMAT)
logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt=TIME_FORMAT)


class DashLoggerHandler(logging.StreamHandler):
    def __init__(self, console):
        logging.StreamHandler.__init__(self)
        self.console = console
        self.setFormatter(formatter)

    def emit(self, record):
        msg = self.format(record)
        self.console.showMessage(msg)


"""
Main Window
"""


class MainWindow(QtWidgets.QMainWindow):
    init_settings = {
        "sampling_rate": 100,
        "log_interval": 1,
        "num_channels": 1,
        "display_duration": 5,
        "place": "家",
        "temperature": 20.0,
        "humidity": 50,
        "plant": "ポトス",
        "purpose": "",
        "note": "",
    }

    settings = init_settings.copy()

    def __init__(self, parent=None, *args, **kwargs):
        super(MainWindow, self).__init__(parent, *args, **kwargs)
        uic.loadUi("./UI/main_window.ui", self)
        # uic.loadUi("./UI/main_window.ui", self)
        self.setWindowTitle("Measurement")
        self.InputMeasureStop.setEnabled(False)
        self.InputOpenFolder.setEnabled(False)
        self.RecordSettings.setEnabled(False)
        self.Record.setEnabled(False)
        self.NoteBox.setEnabled(False)

        # variable
        home = expanduser("~")
        default_save_dir = "Documents/PlantAnalysis/"
        self.path_save_base_folder = os.path.join(home, default_save_dir)
        self.InputSaveDirPath.setText(self.path_save_base_folder)

        # logger
        dashLoggerHandler = DashLoggerHandler(self.statusbar)
        logger.addHandler(dashLoggerHandler)

        # button events
        self.cw = ConnectionWindow(parent=self)
        self.InputChgSerialPort.clicked.connect(
            lambda: self.cw.show_window(self.serial_port)
        )
        self.InputMeasureStart.clicked.connect(lambda: self.measure_start())
        self.InputMeasureStop.clicked.connect(lambda: self.measure_stop())

        self.InputChgSaveFolder.clicked.connect(lambda: self.get_folder())

        self.InputRecordStart.clicked.connect(lambda: self.record_start())
        self.InputRecordStop.clicked.connect(lambda: self.record_stop())

        self.settings = self.init_ui(self.settings)

    def init_ui(self, settings):
        self.InputNumChannels.setValue(settings["num_channels"])
        self.InputNumChannels.setMinimum(1)
        self.InputNumChannels.valueChanged.connect(
            lambda value: self.chg_settings("num_channels", value)
        )

        self.InputSamplingRate.setRange(1, 1000)
        self.InputSamplingRate.setValue(settings["sampling_rate"])
        self.InputSamplingRate.setSingleStep(10)
        self.InputSamplingRate.valueChanged.connect(
            lambda value: self.chg_settings("sampling_rate", value)
        )

        self.InputRecordInterval.setValue(settings["log_interval"])
        self.InputRecordInterval.setRange(1, settings["display_duration"])
        self.InputRecordInterval.valueChanged.connect(
            lambda value: self.chg_settings("log_interval", value)
        )
        self.InputRecordInterval.valueChanged.connect(
            lambda value: self.InputDisplayDuration.setMinimum(value)
        )

        self.InputDisplayDuration.setValue(settings["display_duration"])
        self.InputDisplayDuration.setMinimum(settings["log_interval"])
        self.InputDisplayDuration.setSingleStep(5)
        self.InputDisplayDuration.valueChanged.connect(
            lambda value: self.chg_settings("display_duration", value)
        )
        self.InputDisplayDuration.valueChanged.connect(
            lambda value: self.InputRecordInterval.setMaximum(value)
        )

        self.InputPlace.setText(settings["place"])
        self.InputPlace.textChanged.connect(
            lambda value: self.chg_settings("place", value)
        )

        self.InputTemperature.setValue(settings["temperature"])
        self.InputTemperature.valueChanged.connect(
            lambda value: self.chg_settings("temperature", value)
        )

        self.InputHumidity.setValue(settings["humidity"])
        self.InputHumidity.valueChanged.connect(
            lambda value: self.chg_settings("humidity", value)
        )

        self.InputPlant.setText(settings["plant"])
        self.InputPlant.textChanged.connect(
            lambda value: self.chg_settings("plant", value)
        )

        self.InputPurpose.setPlainText(settings["purpose"])
        self.InputPurpose.textChanged.connect(
            lambda: self.chg_settings("purpose", self.InputPurpose.toPlainText())
        )

        self.InputNote.setPlainText(settings["note"])
        self.InputNote.textChanged.connect(
            lambda: self.chg_settings("note", self.InputNote.toPlainText())
        )

        return settings

    def chg_settings(self, key, value):
        self.settings[key] = value
        if hasattr(self, "save_data"):
            self.save_data.save_settings(self.settings)

    def show_windows(self):
        self.show()
        self.cw.show_window("")

    def set_serial_port(self, serial_port):
        self.serial_port = serial_port
        self.InputSerialPort.setText(serial_port)

    def measure_start(self):
        try:
            self.arduino = serial.Serial(self.serial_port, 2000000)

            self.store_data = StoreData(self.arduino, self.settings)
            self.store_data.singal.connect(lambda errorCode: self.on_error(errorCode))
            self.store_data.console.connect(lambda msg: logger.info(msg))
            if not self.store_data.isRunning():
                self.store_data.restart()
            self.store_data.start()

            self.draw_graph = DrawGraph(
                self.GraphicsLayoutWidget, self.store_data, self.settings
            )

            self.InputMeasureStart.setEnabled(False)
            self.InputMeasureStop.setEnabled(True)
            self.MesaurementSettingsBox.setEnabled(False)
            self.RecordSettings.setEnabled(True)
            self.InputRecordStop.setEnabled(False)
            self.Record.setEnabled(True)
            self.InputOpenFolder.setEnabled(False)
        except serial.SerialException:
            logger.info(f"指定されたシリアルポートが見つかりません。USB接続を確認してください。")
            self.cw.show_window(self.serial_port)

    def measure_stop(self):

        self.store_data.stop()
        self.arduino.close()
        self.draw_graph.stop()
        if hasattr(self, "save_data"):
            self.record_stop()
        logger.info("測定を停止しました。")
        self.InputMeasureStart.setEnabled(True)
        self.InputMeasureStop.setEnabled(False)
        self.MesaurementSettingsBox.setEnabled(True)
        self.RecordSettings.setEnabled(False)
        self.Record.setEnabled(False)

    def record_start(self):
        self.save_data = SaveData(
            self.GraphicsLayoutWidget,
            self.store_data,
            self.settings,
            self.path_save_base_folder,
        )
        self.save_data.console.connect(lambda msg: logger.info(msg))
        self.save_data.run()
        self.InputSaveDir.setText(self.save_data.get_folder_name())
        self.InputOpenFolder.clicked.connect(
            lambda: self.open_folder(self.save_data.get_folder_path())
        )
        self.save_data.save_settings(self.settings)
        self.save_data.singal.connect(lambda data: self.update_record_info(data))

        settings = self.init_settings.copy()
        self.InputPlace.setText(settings["place"])
        self.InputTemperature.setValue(settings["temperature"])
        self.InputHumidity.setValue(settings["humidity"])
        self.InputPlant.setText(settings["plant"])
        self.InputPurpose.setPlainText(settings["purpose"])
        self.InputNote.setPlainText(settings["note"])

        self.InputRecordStart.setEnabled(False)
        self.InputRecordStop.setEnabled(True)
        self.InputOpenFolder.setEnabled(True)
        self.NoteBox.setEnabled(True)

    def record_stop(self):
        self.save_data.stop()
        self.InputElapsedTime.setText("")
        self.InputNumSamples.setText("")
        self.InputFolderSize.setText("")
        self.InputSaveDir.setText("")

        self.InputRecordStart.setEnabled(True)
        self.InputRecordStop.setEnabled(False)
        self.InputOpenFolder.setEnabled(False)
        self.NoteBox.setEnabled(False)

    def lost_usb_connection(self):
        self.measure_stop()
        self.cw.show_window(self.serial_port)

    def update_record_info(self, data):
        self.InputElapsedTime.setText(data["elapsed_time"])
        self.InputNumSamples.setText(data["num_samples"])
        self.InputFolderSize.setText(data["folder_size"])

    def open_folder(self, path):
        os.system(f"open {path}")

    def get_folder(self):
        path_save_base_folder = str(
            QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        )
        if path_save_base_folder != "":
            self.path_save_base_folder = path_save_base_folder
            self.InputSaveDirPath.setText(self.path_save_base_folder)

    def on_error(self, _error_code):
        if _error_code == "01":
            self.lost_usb_connection()
        elif _error_code == "02":
            self.measure_stop()
            logger.info("Error: チャンネル数を確認してください。")


"""
Sub Window
"""


class ConnectionWindow(QtWidgets.QDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super(ConnectionWindow, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        uic.loadUi("./UI/connection.ui", self)
        # uic.loadUi("./UI/connection.ui", self)
        self.setWindowTitle("")
        self.setModal(True)
        self.InputSelect.clicked.connect(lambda: self.select())
        self.InputSerialPorts.currentTextChanged.connect(
            lambda text: self.reload_serial_port(text)
        )

    def show_window(self, current_serial_port):
        serial_ports = tools.get_serial_ports()
        self.InputSerialPorts.clear()
        self.InputSerialPorts.addItems(serial_ports)
        self.InputSerialPorts.addItem("[Research serial ports]")
        if current_serial_port in serial_ports:
            self.InputSerialPorts.setCurrentText(current_serial_port)
        else:
            self.InputSerialPorts.setCurrentText(serial_ports[0])
        self.show()

    def reload_serial_port(self, text):
        if text == "[Research serial ports]":
            self.show_window("")

    def select(self):
        self.parent.set_serial_port(self.InputSerialPorts.currentText())
        self.close()

    def closeEvent(self, event):
        if not hasattr(self.parent, "serial_port"):
            self.parent.close()
        else:
            event.accept()


"""
Data processing
"""


class StoreData(QtCore.QThread):
    # singal = QtCore.Signal(str)
    # console = QtCore.Signal(str)
    singal = pyqtSignal(str)
    console = pyqtSignal(str)

    def __init__(self, arduino, settings, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.mutex = QtCore.QMutex()
        self.stopped = False
        self.arduino = arduino
        self.settings = settings
        show_samples = settings["display_duration"] * settings["sampling_rate"]
        self.raw_signals = []
        for idx in range(settings["num_channels"]):
            self.raw_signals.append(deque(np.zeros(show_samples), maxlen=show_samples))

    def __del__(self):
        # Threadオブジェクトが削除されたときにThreadを停止する(念のため)
        self.stop()
        self.wait()

    def stop(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stopped = True

    def restart(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stopped = False

    def run(self):
        self.console.emit("測定を開始しました。")
        try:
            for line in self.arduino:
                try:
                    line = line.decode().rstrip().split(",")
                    # 文字から数値に変換
                    raw_signal_now = np.array([int(s) for s in line]) * 5 / 1023
                    for idx, raw_signal in enumerate(self.raw_signals):
                        raw_signal.append(raw_signal_now[idx])
                except ValueError:
                    pass
                except IndexError:
                    self.console.emit("Error: チャンネル数を確認してください。")
                    self.singal.emit("02")
        except serial.SerialException as e:
            if "[Errno 9]" in str(e):
                # self.console.emit("測定を停止しました。")
                pass
            elif "[Errno 6]" in str(e):
                self.console.emit("Error: USB接続が切れました。記録を停止します。")
                self.singal.emit("01")

    def get_raw_signals(self):
        return self.raw_signals


"""
Graph
"""


class DrawGraph:
    colorpalette = iter(
        [
            "#636EFA",
            "#EF553B",
            "#00CC96",
            "#AB63FA",
            "#FFA15A",
            "#19D3F3",
            "#FF6692",
            "#B6E880",
            "#FF97FF",
            "#FECB52",
        ]
    )
    plots = {}

    def __init__(self, parent, store_data_class, settings):
        self.win = parent
        self.store_data = store_data_class

        self.settings = settings
        time_delta = 1 / self.settings["sampling_rate"]
        self.show_samples = (
            self.settings["display_duration"] * self.settings["sampling_rate"]
        )
        self.x = np.arange(0, self.settings["display_duration"], time_delta)[
            0 : self.show_samples
        ]

        self.set_graph_ui()
        self.timer = QtCore.QTimer(self.win)
        self.timer.timeout.connect(lambda: self.draw())
        self.timer.start(100)

    def set_graph_ui(self):
        for idx in range(self.settings["num_channels"]):
            if idx != 0:
                self.win.nextRow()
            self.plots.update(
                {f"channel_{idx}": {"area": self.win.addPlot()}}
            )  # add plot
            self.plots[f"channel_{idx}"]["area"].addLegend()  # add regend

            curve = self.plots[f"channel_{idx}"]["area"].plot(
                self.x,
                np.zeros(self.show_samples),
                pen=next(self.colorpalette),
                name=f"<span style='color: #ffffff; font-weight: bold; font-size: 12px'>channel {idx}</span>",
            )
            self.plots[f"channel_{idx}"].update({"curve": curve})
            self.plots[f"channel_{idx}"]["area"].setLabel(
                "bottom",
                text="<span style='color: #ffffff; font-weight: bold; font-size: 12px'>Time [s]</span>",
            )
            self.plots[f"channel_{idx}"]["area"].showGrid(True)
            self.plots[f"channel_{idx}"]["area"].enableAutoRange(axis="y")
            self.plots[f"channel_{idx}"]["area"].setAutoVisible(y=True)
            self.plots[f"channel_{idx}"]["area"].setMouseEnabled(False)

    def draw(self):
        raw_signals = self.store_data.get_raw_signals()
        for idx, raw_signal in enumerate(raw_signals):
            curve = self.plots[f"channel_{idx}"]["curve"]
            curve.setData(self.x, raw_signal)

    def stop(self):
        self.timer.stop()
        self.win.clear()


"""
Save data
"""


class SaveData(QtCore.QObject):
    start_flg = False
    num_sample_points = 0
    singal = pyqtSignal(dict)
    console = pyqtSignal(str)

    def __init__(self, parent, store_data_class, settings, _path_save_base_folder):
        QtCore.QObject.__init__(self)
        self.store_data = store_data_class
        self.settings = settings
        self.dt_start_time = dt.datetime.now()
        self.str_start_time = self.dt_start_time.strftime("%Y-%m-%d_%H-%M-%S")
        self.dir_path = os.path.join(
            _path_save_base_folder, f"Data/{self.str_start_time}"
        )
        os.makedirs(self.dir_path, exist_ok=True)
        self.save_data_path = f"{self.dir_path}/{self.str_start_time}.csv"
        self.save_settings_path = f"{self.dir_path}/settings.json"

        self.timer = QtCore.QTimer(parent)
        self.timer.timeout.connect(lambda: self.save_csv())

    def run(self):
        self.console.emit(f"記録を開始しました。保存先: {self.dir_path}")
        self.timer.start(self.settings["log_interval"] * 1000)

    def save_csv(self):
        raw_signals = self.store_data.get_raw_signals()
        num_log_samples = self.settings["log_interval"] * self.settings["sampling_rate"]
        last_averages = []

        if not self.start_flg and not np.all(
            np.array(raw_signals[0])[0:-num_log_samples] == 0
        ):
            self.start_flg = True

        if self.start_flg:
            self.num_sample_points += 1
            for raw_signal in raw_signals:
                last_average = np.mean(list(raw_signal)[-num_log_samples:])
                last_averages.append(last_average)
            last_averages.insert(0, str(dt.datetime.now()))

            with open(self.save_data_path, "a") as f:
                writer = csv.writer(f)
                writer.writerow(last_averages)

        self.emit_info()

    def save_settings(self, settings):
        with open(self.save_settings_path, "w") as f:
            json.dump(settings, f, indent=4, ensure_ascii=False)

    def get_folder_name(self):
        return self.str_start_time

    def get_folder_path(self):
        abs_folder_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), self.dir_path
        )
        return abs_folder_path

    def emit_info(self):
        duration = str(dt.datetime.now() - self.dt_start_time).split(".")[0]
        num_sample_points = str(self.num_sample_points)
        folder_size = tools.get_dir_size(self.dir_path)
        self.singal.emit(
            {
                "elapsed_time": duration,
                "num_samples": num_sample_points,
                "folder_size": folder_size,
            }
        )

    def stop(self):
        self.timer.stop()
        self.console.emit("記録を停止しました。")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show_windows()
    sys.exit(app.exec_())
