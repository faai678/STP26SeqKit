# settings.py
"""
LOGGING CONFIGURATION (DEFENSIVE VERSION)

----------------------------------------
WHAT THIS TEACHES
----------------------------------------
✔ Centralised logging configuration
✔ Safe file handling
✔ Defensive programming
✔ Logger naming conventions (important in real systems)
✔ Log rotation (preventing uncontrolled file growth)

KEY IDEA:
Even when things seem simple, we still validate inputs
and design logging for clarity, consistency, and extensibility.
"""

import os

# --------------------------------------------------
# STEP 1: Define default log file (hidden, home directory)
# this bit here is so that you dont hardcode paths, so its usable on any system without modification
# creates path string for hidden log to be used later
# --------------------------------------------------


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define logs folder INSIDE your package
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Define log file inside that folder
LOG_FILE = os.path.join(LOG_DIR, "seqkitstp.log")





#home_dir = os.path.expanduser("~")
#DEFAULT_LOG = os.path.join(home_dir, ".seqkitstp.log")

#LOG_FILE = DEFAULT_LOG


# --------------------------------------------------
# STEP 2: NORMALISE the path (defensive step)
# --------------------------------------------------
#LOG_FILE = os.path.abspath(os.path.expanduser(LOG_FILE))


# --------------------------------------------------
# STEP 3: Ensure directory exists
# and if dont, it will create it (defensive step))
# --------------------------------------------------
LOG_DIR = os.path.dirname(LOG_FILE)
if LOG_DIR:
    os.makedirs(LOG_DIR, exist_ok=True)


# --------------------------------------------------
# STEP 4: Logging configuration
# four main sections: formatters, handlers, loggers, root
# --------------------------------------------------
LOGGING_CONFIG = {
    "version": 1, #always 1. leave as it is
    "disable_existing_loggers": False, #so you dont change other moduels or confiq for other loggers or tools
    # --------------------------------------------------
    # FORMATTERS: how log looks
    # --------------------------------------------------
    "formatters": {
        "standard": {
            "format": (
                "%(asctime)s | %(levelname)s | %(name)s | "
                "%(filename)s:%(lineno)d | %(message)s"
            )
        }
    },
    # --------------------------------------------------
    # HANDLERS: where logs are sent, decides where your log messages go console and/or file
    # why not start level at debug? debug is like print, u dont need to log but u want info
    # --------------------------------------------------
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
        },
        # --------------------------------------------------
        # ROTATING FILE HANDLER (UPDATED)
        # --------------------------------------------------
        #
        # This replaces the basic FileHandler with a
        # RotatingFileHandler to prevent unlimited growth.
        #
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            # Only store ERROR and CRITICAL messages in file
            # (keeps disk usage focused on important events)
            "level": "ERROR",
            "formatter": "standard",
            "filename": LOG_FILE ,
            # --------------------------------------------------
            # ROTATION SETTINGS (IMPORTANT TEACHING POINT)
            # --------------------------------------------------
            #
            # maxBytes:
            # Maximum size of the log file BEFORE rotation happens.
            #
            # Example:
            # 1_048_576 bytes = 1 MB
            #
            # Here we set a small size for demonstration.
            #
            "maxBytes": 1024 * 50,  # 50 KB
            #
            # backupCount:
            # Number of OLD log files to retain.
            #
            # Example with backupCount = 3:
            #
            # Files will look like:
            #   .seqkitstp.log      (current active log)
            #   .seqkitstp.log.1    (most recent previous)
            #   .seqkitstp.log.2
            #   .seqkitstp.log.3    (oldest retained)
            #
            # When rotation occurs:
            #   .log.3 is deleted
            #   .log.2 → becomes .log.3
            #   .log.1 → becomes .log.2
            #   .log   → becomes .log.1
            #   new empty .log is created
            #
            "backupCount": 3,
            # Optional: ensures file opens safely even if reused
            "encoding": "utf-8",
        },
    },
    # ---------------------------------------------------------------------------------------
    # OPTIONAL: NAMED LOGGER (TEACHING EXAMPLE) - But easy to import into other
    # tools by name
    # ---------------------------------------------------------------------------------------
    "loggers": {
        "SeqKitSTP": {
            # Capture everything at this level;
            # handlers will decide what gets written
            "level": "DEBUG",
            # Send logs to both console and rotating file
            "handlers": ["console", "file"],
            # Prevent duplication from parent/root loggers
            "propagate": False,
        },
    },
    # --------------------------------------------------
    # ROOT LOGGER
    # --------------------------------------------------
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"],
    },
}
