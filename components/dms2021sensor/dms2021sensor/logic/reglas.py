from dms2021sensor.data.config.sensorconfiguration import SensorConfiguration

class Reglas():

    instance = None


    def __init__(self):
        self.time = SensorConfiguration().get_rules_time()
        self.route = SensorConfiguration().get_rules_route()


    @staticmethod
    def get_instance():
        if instance is None:
            instance = Reglas()

        return instance

    def modify_rules(self, route: str, time: int):
        self.time = time
        self.route = route

    def get_time(self):
        return self.time

    def get_route(self):
        return self.route