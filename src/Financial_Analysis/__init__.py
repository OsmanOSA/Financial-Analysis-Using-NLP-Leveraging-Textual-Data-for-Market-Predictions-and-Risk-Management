import os
import sys
import logging


# Set up logging
logginf_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s]"

log_dir = "logs"
log_fil_path = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(level=logging.INFO, 
                    format=logginf_str, 
                    handlers=[
                        logging.FileHandler(log_fil_path),
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger("Financial_Analysis")