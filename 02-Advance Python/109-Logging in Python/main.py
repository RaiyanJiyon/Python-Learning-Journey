import logging

# Configure the logging system
logging.basicConfig(level=logging.DEBUG,  # Set the minimum logging level to display
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log message format
                    filename='example.log',  # Specify the log file name
                    filemode='w')  # Specify the file mode ('w' for write)

# Log messages at different severity levels
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
