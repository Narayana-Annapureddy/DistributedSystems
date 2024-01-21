import math

class ConsistentHashing:

    def __init__(self, num_servers, slots):

        # parameters
        self.num_servers = num_servers
        self.num_slots = slots
        self.virtual_servers = int(math.log2(slots))

        # server mapping
        self.servers = [None] * slots
        for i in range(num_servers):
            self.add_server(i)


    def add_server(self, i):
        # add log(slots) no.of servers
        for j in range(self.virtual_servers):
            server_id = f"s_{i}_{j}"
            hash = self.server_mapping(i, j)
            self.servers[hash] = server_id
    
    def server_mapping(self, i, j):

        hash = i**2 + j**2 + 2*j + 25
        jump = 1
        # quadratic probing is used to resolve collision
        while (self.servers[hash] != None):
            hash = (hash + jump**2) % self.num_slots
            jump += 1
        return hash

    def remove_server(self, i):
        
        for j in range(self.virtual_servers):

            hash = (self.server_mapping(i, j)) % (self.num_slots)
            jump = 1
            # same quadratic probing is used to find all virtual servers of 'i'
            while (self.servers[hash] != f"s_{i}_{j}"):
                hash = (hash + jump**2) % self.num_slots
                jump += 1
            self.servers[hash] = None

    def req_server(self, req_id):

        hash = (self.request_mapping(req_id)) % (self.num_slots)
        while (self.servers[hash] == None):
            hash = (hash+1) % (self.num_slots)
            
        # The hash value represents the server_id of the server
        # Now extract the true server number and return it.
        
        server_num = int(self.servers[hash].split('_')[1])
        return server_num

    def request_mapping(self, i):
        hash = i**2 + 2*i + 17
        return hash 
    

# create object for consistent hashing
obj = ConsistentHashing(3, 512)

print(obj.servers)

print(obj.add_server(3))
print(obj.remove_server(0))
print(obj.servers)

req = 428342
print(obj.req_server(req))
