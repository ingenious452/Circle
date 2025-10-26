"""Manage the life cycle of circled notifier 👹 """

import logging
import subprocess
import sys
from pathlib import Path

import psutil

class CircledManager:

    def __init__(self, script_path, pid_file:Path, stop_file:Path, log_path:Path):
        self.pid_path = pid_file
        self.stop_path = stop_file
        self. command = [sys.executable, script_path]

        self.os_proc_config = {}
        if sys.platform == "win32":
            self.os_proc_config["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW
        else:
            self.os_proc_config["start_new_session"] = True

        self.logger = logging.getLogger("circledManager")
        self.logger.setLevel(logging.INFO)

        log_path.parent.mkdir(parents=True, exist_ok=True)

        log_file_handler = logging.FileHandler(filename=log_path, mode="a", encoding="utf-8")
        log_formatter = logging.Formatter("{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M")
        log_file_handler.setFormatter(log_formatter)

        self.logger.addHandler(log_file_handler)


    def __is_running(self):
        if not self.pid_path.exists():
            return False
        try:
            pid = int(self.pid_path.read_text().strip())
            proc = psutil.Process(pid)
            return proc.is_running()
        except psutil.NoSuchProcess:
            self.pid_path.unlink(missing_ok=True)
            return False

    def start(self):
        if self.__is_running():
            self.logger.info("Circled 👹 is already running..")
            return
        proc = subprocess.Popen(self.command,
                                stdin=subprocess.DEVNULL,
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL,
                                **self.os_proc_config
                                )
        self.pid_path.parent.mkdir(parents=True, exist_ok=True)
        self.pid_path.write_text(str(proc.pid))
        self.logger.info(f"Started circled 👹.....")

    def terminate(self):
        if not self.pid_path.exists() or not self.__is_running():
            self.logger.info("Circled 👹 is not running (or PID file is missing)")
            return
        self.stop_path.parent.mkdir(parents=True, exist_ok=True)
        self.stop_path.write_text("stop")
        try:
            pid = int(self.pid_path.read_text().strip())
            proc = psutil.Process(pid)
            proc.wait(5)
            self.logger.info("Circled 👹 terminated gracefully")
        except psutil.NoSuchProcess:
            self.logger.info(f"Circled 👹 process: {pid} not found")
        except psutil.TimeoutExpired:
            if proc.is_running():
                self.logger.info(f"Graceful timeout exceeded. Force killing circled 👹: {pid}")
                proc.kill()
                try:
                    proc.wait(5)
                    self.logger.info("Force killed circled 👹 process")
                except psutil.TimeoutExpired:
                    self.logger.error("Failed to force kill circled 👹 process.")
        except Exception as e:
            self.logger.warning(f"Some error occurred while terminating circled 👹: {e}")
        finally:
            self.pid_path.unlink(missing_ok=True)
            self.stop_path.unlink(missing_ok=True)
            self.logger.info("Control files 📁 cleaned up.")

    def status(self):
        if not self.pid_path.exists():
            return "stopped"
        try:
            pid = int(self.pid_path.read_text().strip())
            proc = psutil.Process(pid)
            return proc.status()
        except psutil.NoSuchProcess:
            self.pid_path.unlink(missing_ok=True)
            return "stopped"


