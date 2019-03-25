# def hash(astring, tablesize):
#     sum = 0
#     for pos in range(len(astring)):
#         print(ord(astring[pos]))
#         sum = sum + ord(astring[pos])

#     return sum%tablesize

# print(hash("cat", 7))

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hash_function(key, self.size)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                newhash = self.rehash(hashvalue, self.size)
                while self.slots[newhash] != None and self.slots[newhash] != key:
                    newhash = self.rehash(newhash, self.size)
                if self.slots[newhash] == None:
                    self.slots[newhash] = key
                    self.data[newhash] = data
                else:
                    self.data[newhash] = data

    def hash_function(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hash_function(key, self.size)
        found = False
        stop = False
        data = None
        position = startslot

        if self.slots[startslot] == key:
            return self.data[startslot]

        while self.slots[startslot] != None and not found and not stop:
            if self.slots[startslot] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(startslot, self.size)
                if position == startslot:
                    stop = True
        
        return data

        def __getitem__(self,key):
            return self.get(key)

        def __setitem__(self,key,data):
            self.put(key,data)

H = HashTable()
H.put(54,"cat")
H.put(26,"dog")
H.put(93,"lion")
H.put(17,"tiger")
H.put(77,"bird")
H.put(31,"cow")
H.put(44,"goat")
H.put(55,"pig")
H.put(20,"chicken")

# H[54]="cat"
# H[26]="dog"
# H[93]="lion"
# H[17]="tiger"
# H[77]="bird"
# H[31]="cow"
# H[44]="goat"
# H[55]="pig"
# H[20]="chicken"
print(H.slots)
print(H.data)

H.put(20,"duck")

print(H.data)
