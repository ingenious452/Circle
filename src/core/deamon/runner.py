"""
Get the database and fetch all the birthday that are due today
"""
import logging
import subprocess
import sys
from pathlib import Path

import psutil

# Run this script in detached mode
# python = sys.executable
# script = Path().absolute().parent / 'scheduler.py'
# PID_FILE = Path().absolute().parent.parent / 'circled.pid'
# stop_file = Path().absolute().parent.parent / 'circled.stop'


logger = logging.getLogger("manager")

log_file = r"D:\Web_Development\kill_enemy\circle\circle_v1\logs\scheduler\daemonmanager.log"
logger.setLevel(logging.INFO)

log_file_handler = logging.FileHandler(filename=log_file, mode="a", encoding="utf-8")
log_formatter = logging.Formatter("{asctime} - {levelname} - {message}",
                                  style="{",
                                  datefmt="%Y-%m-%d %H:%M",
                                )
log_file_handler.setFormatter(log_formatter)
logger.addHandler(log_file_handler)


class DaemonManager:

    def __init__(self, script_path: Path, pid_file: Path, stop_file: Path):
        self.pid_file = pid_file
        self.stop_file = stop_file
        self.command = [sys.executable, script_path]

        self.os_proc_config = {}
        if sys.platform == "win32":
            self.os_proc_config["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW
        else:
            self.os_proc_config["start_new_session"] = True

    def _is_running(self):
        if not self.pid_file.exists():
            return False
        try:
            pid = int(self.pid_file.read_text().strip())
            proc = psutil.Process(pid)
            return proc.is_running()
        except psutil.NoSuchProcess:
            self.pid_file.unlink()
            return False

    def start(self):
        if self._is_running():
            logger.info("Circled 👹 is already running..")
            return
        proc = subprocess.Popen(self.command,
                                stdin=subprocess.DEVNULL,
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL,
                                **self.os_proc_config
        )
        self.pid_file.parent.mkdir(parents=True, exist_ok=True)
        self.pid_file.write_text(str(proc.pid))
        logger.info("Started circled 👹.....")

    def terminate(self):
        if not self.pid_file.exists() and not self._is_running():
            logger.info("Circled 👹 is not running (or PID file is missing)")
            return

        # Graceful exit signal to scheduler
        self.stop_file.parent.mkdir(parents=True, exist_ok=True)
        self.stop_file.write_text("stop")
        logger.info("Circled 👹 to terminated gracefully")

        # stop the process now
        try:
            pid = int(self.pid_file.read_text().strip())
            proc = psutil.Process(pid)
            proc.wait(5)  # waiting for the child process to stop gracefully using stop file
        except psutil.NoSuchProcess:
            logger.info(f"Circled 👹 process: {pid} not found")
        except psutil.TimeoutExpired:
            if proc.is_running():
                logger.info(f"Gracefully timeout exceeded. Force killing circled: {pid}")
                proc.kill()
                try:
                    proc.wait(5)
                    logger.info("Force killed circled 👹 process")
                except psutil.TimeoutExpired:
                    logger.error("Failed to force kill circled 👹 process.")
        except Exception as e:
            logger.warning(f"Some error occurred while terminating circled: {e}")
        finally:
            self.pid_file.unlink(missing_ok=True)
            self.stop_file.unlink(missing_ok=True)
            logger.info("Control files cleaned up.")

    def status(self):
        if not self.pid_file.exists():
            return "stopped"
        try:
            pid = int(self.pid_file.read_text().strip())
            proc = psutil.Process(pid)
            return proc.status()
        except psutil.NoSuchProcess:
            self.pid_file.unlink()
            return "stopped"
