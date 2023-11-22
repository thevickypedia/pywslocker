import logging
import subprocess

from .module import settings


def lock(logger: logging.Logger = None) -> None:
    """Locks the workstation.

    Args:
        logger: Bring your own logger.
    """
    if settings.os == "Darwin":
        cmd = """osascript -e 'tell application "System Events" to keystroke "q" using {control down, command down}'"""
    elif settings.os == "Windows":
        try:
            import ctypes
            ctypes.windll.user32.LockWorkStation()
            return
        except (ImportError, AttributeError) as error:
            logger.warning(error) if logger else None
            cmd = "rundll32.exe user32.dll, LockWorkStation"
    else:
        cmd = "gnome-screensaver-command --lock"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode and logger:
        logger.error("Command `%s` failed with error code: %d", result.args, result.returncode)
