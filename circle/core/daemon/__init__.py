from circle.core.daemon.manager import DaemonManager
from circle.config import config

def get_daemon_manager():
    return DaemonManager(config.DAEMON_SCRIPT,
                          config.PID_FILE,
                          config.STOP_FILE,
                          config.LOG_DIR / "daemon.log")
