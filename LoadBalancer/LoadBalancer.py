import math
class LoadBalancer:
    def __init__(self):
        self.no_of_slots = 512
        self.vir_servers = math.log(self.no_of_servers,2)
    def ConsistentHash(rid):
        no_of_servers = 3
        rid = int(rid)
        slot = (rid*rid+2*rid+17)%(self.vir_servers*no_of_servers)
        

        