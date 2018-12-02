from dproj_app.views import get_array_views
from os import environ

class Shards:

    def __init__(self, number):
        self.shard_size = number
        self.views = get_array_views()
        self.num_nodes = len(views)
        self.shard_directory = {}
        # 
        if self.num_nodes >= 2 * self.shard_size:
            for idx, IP_PORT in self.views:
                self.shard_directory[idx%self.shard_size] = IP_PORT
        elif self.shard_size >= self.num_nodes and self.num_nodes/2 > 1:
            self.shard_size = self.num_nodes/2
            for idx, IP_PORT in self.views:
                self.shard_directory[idx%self.shard_size] = IP_PORT
        else:
            # # of nodes = 3 or something liek that.
            self.shard_size = 1
            self.shard_directory[0] = self.views 
            
        self.my_shard = self.views.index(environ.get("IP_PORT"))%self.shard_size
    
    def get_directory(self):
        return self.shard_directory
    
    def get_my_shard(self):
        return self.my_shard
    
    def get_shard_size(self):
        return self.shard_size
    
    def update_shard_size(self, new_size):
        self.shard_size = new_size
        # maybe call function to reevaluate and redistrbute data here?
        return True

    

        
            

    