class LFUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.key_to_val={}
        self.key_to_freq={}
        self.freq_to_key=defaultdict(OrderedDict)
        self.min_freq=0
    def update(self,key):
        freq=self.key_to_freq[key]
        del self.freq_to_key[freq][key]
        if not self.freq_to_key[freq]:
            del self.freq_to_key[freq]
            if not self.min_freq==freq:
                self.min_freq+=1
        self.key_to_freq[key]+=1
        self.key_to_freq[freq+1][key]=None
    def get(self,key):
        if key not in self.key_to_val:
            return -1
        self.key_to_val[key]
        self.update(key)
        return self.key_to_val[key]
    def put(self,key,value):
        if self.capacity==0:
            return
        if key in self.key_to_val:
            self.key_to_val[key]=value
            self.update(key)
            return
        if len(self.key_to_val)>=self.capacity:
            lfu,_=self.freq_to_key[self.min_freq].popitem(last=False)
            del self.key_to_val[lfu]
            del self.key_to_freq[lfu]
        self.key_to_val[key]=value
        self.key_to_freq[key]=1
        self.min_freq=1
        self.freq_to_key[1][key]=None
        return
