from circle.core.daemon.manager import CircledManager
from circle.core.config import config

def get_daemon_manager():
    return CircledManager(config.DAEMON_SCRIPT,
                          config.PID_FILE,
                          config.STOP_FILE,
                          config.LOG_DIR / 'daemon' / 'circledM.log')
