class Flight:

    def __init__(self, engine):
        self.engine = engine # inject object

    def startEngine(self):
        self.engine.start()

class AirbusEngine:

    def start(self):
        print("Starting airbus engine")

air = AirbusEngine()
fli = Flight(air)
fli.startEngine()