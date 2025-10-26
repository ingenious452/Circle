"""Manage the life cycle of circled notifier 👹 """

import subprocess
import sys
from pathlib import Path

import psutil

from circle.core.logger import logger


class DaemonManager:

    def __init__(self, script_path, pid_file:Path, stop_file:Path, log_path:Path):
        self.pid_path = pid_file
        self.stop_path = stop_file
        self.log_path = log_path
        self.command = [sys.executable, "-m", script_path]

        self.os_proc_config = {}
        if sys.platform == "win32":
            self.os_proc_config["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW
        else:
            self.os_proc_config["start_new_session"] = True

        self._logger = logger.get_logger("daemon_manager", log_path)

    def __str__(self):
        return f"DaemonManager<Pid: {self.pid_path}, stop: {self.stop_path}, command: {self.command}>"
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
            self._logger.info("Reminder daemon is already running..")
            return
        with open(self.log_path, "a", buffering=1) as log_file:
            proc = subprocess.Popen(self.command,
                                    stdin=log_file,
                                    stdout=log_file,
                                    stderr=log_file,
                                    **self.os_proc_config
                                    )
        self.pid_path.parent.mkdir(parents=True, exist_ok=True)
        self.pid_path.write_text(str(proc.pid))
        self._logger.info(f"Started reminder daemon {proc.pid}")

    def terminate(self):
        if not self.pid_path.exists() or not self.__is_running():
            self._logger.info("Reminder daemon is not running (or PID file is missing)")
            return
        self.stop_path.parent.mkdir(parents=True, exist_ok=True)
        self.stop_path.write_text("stop")
        
        pid = None
        proc = None
        try:
            pid = int(self.pid_path.read_text().strip())
            proc = psutil.Process(pid)
            proc.wait(5)
            self._logger.info("Reminder daemon terminated gracefully")
        except psutil.NoSuchProcess:
            self._logger.info(f"Reminder daemon: {pid} not found")
        except psutil.TimeoutExpired:
            if proc.is_running():
                self._logger.info(f"Graceful timeout exceeded. Force killing reminder daemon: {pid}")
                proc.kill()
                try:
                    proc.wait(5)
                    self._logger.info("Force killed reminder daemon")
                except psutil.TimeoutExpired:
                    self._logger.error("Failed to force kill reminder daemon.")
        except Exception as e:
            self._logger.warning(f"Some error occurred while terminating reminder daemon: {e}")
        finally:
            self.pid_path.unlink(missing_ok=True)
            self.stop_path.unlink(missing_ok=True)
            self._logger.info("Control files cleaned up.")

    def status(self):
        if not self.pid_path.exists():
            return "terminated"
        try:
            pid = int(self.pid_path.read_text().strip())
            proc = psutil.Process(pid)
            return proc.status()
        except psutil.NoSuchProcess:
            self.pid_path.unlink(missing_ok=True)
            return "terminated"
