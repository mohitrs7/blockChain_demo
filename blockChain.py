import hashlib

t1 = "Mohit has given 4 rs to satyam"
t2 = "Mohit has given 1.2 rs to vaibhabh"
t3 = "Satyam has given 1 rs to Kallu"
t4 = "Kallu has given 4 rs to vaibhabh"
t5 = "vaibhabh has given 3 rs to Mohit"


class BlockChain:
    def __init__(self, transection_list, previous_block_hash):
        self.transection_list = transection_list
        self.previous_block_hash = previous_block_hash
        self.block_data = "-".join(transection_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


inital_block = BlockChain([t1, t2], "initial string")

print(inital_block.block_data)
print(inital_block.block_hash)

second_block = BlockChain([t3, t4], inital_block.block_hash)

print(second_block.block_data)
print(second_block.block_hash)


third_block = BlockChain([t4, t5], second_block.block_hash)

print(third_block.block_data)
print(third_block.block_hash)

