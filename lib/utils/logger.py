import logging
import logging.handlers
import os

dir = os.path.join(os.getcwd(), "results")

if os.path.exists(dir):
    print("Result directory path exists")
else:
    os.makedirs(dir)

filename = os.path.join(dir, "pytest.log")
should_roll_over = os.path.isfile(filename)
handler = logging.handlers.RotatingFileHandler(filename, backupCount=5)
if should_roll_over:  # log already exists, roll over!
    handler.doRollover()

def getLogger(name):
    logger = logging.getLogger(name)
    fileHandler = logging.FileHandler(filename)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object

    logger.setLevel(logging.DEBUG)
    return logger
