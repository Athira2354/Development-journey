from abc import ABC,abstractmethod

class Bike(ABC):

    @abstractmethod
    def transmission(self):pass
    
    @abstractmethod
    def start(self):pass

class Pulsar(Bike):

    def transmission(self):
        print("pular transmission")

    def start(self):
        print("pulsar start method")
pulsar_instance=Pulsar()
pulsar_instance.start()
pulsar_instance.transmission()

