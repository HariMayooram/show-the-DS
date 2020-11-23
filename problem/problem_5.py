import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculation_of_hash(data)
        self.next = None
    
    def calculation_of_hash(self, data):
        sha = hashlib.sha256()

        hash_str = data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        timestamp = self.timestamp
        data = self.data
        sha256_hash = self.hash
        prev_hash = self.previous_hash

        return 'Timestamp: {}\nData: {}\nSHA256 Hash: {}\nPrev_Hash: {}'.format(timestamp, data, sha256_hash, prev_hash)

class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, data):
        if not data:
            return None
        timestamp = datetime.now()
        current_node = self.head

        if self.head == None:
            current_node = Block(timestamp, data, 0)
            self.head = current_node
        else:
            while current_node.next is not None:
                current_node = current_node.next
            previous_hash = current_node.hash
            current_node.next = Block(timestamp, data, previous_hash)

blockchain = Blockchain()

blockchain.add_block('Some Information in Block 1')
blockchain.add_block('Some Information in Block 2')
blockchain.add_block('Some Information in Block 3')
blockchain.add_block(None)

print('-----Block 1------')
print(blockchain.head)

print('\n-----Block 2------')
print(blockchain.head.next)

print('\n-----Block 3------')
print(blockchain.head.next.next)

print('\n-----Block 4------')
print(blockchain.head.next.next.next)