from utils.logger import Logger


class Application(object):
    def __init__(self):
        self.logger = Logger("application")
        
        self.running = True

        self.logger.log_neutral("Starting Application...")
        self.run()

    def run(self):
        self.logger.log_neutral("Running...")
