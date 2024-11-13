bind = "0.0.0.0:8000"  # The host:port Gunicorn will listen on
workers = 3  # Number of worker processes, recommended: (2 x num_cores) + 1
worker_class = "sync"  # Worker type
timeout = 30  # Timeout in seconds
keepalive = 2  # Keepalive timeout
accesslog = "access.log"  # Access log file
errorlog = "error.log"    # Error log file
loglevel = "info"        # Log level