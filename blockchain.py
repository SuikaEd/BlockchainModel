import time
import json
import hashlib
import random

class Blockchain:
    def __init__(self):
        self.chain = []
        # Create the Genesis block
        self.generate_block(proof=0, previous_hash='0', data="Hello World!")

    def generate_block(self, proof, previous_hash, data):
        block = {
            'index': len(self.chain),
            'timestep': time.strftime("%Y-%m-%d %H:%M:%S"),
            'data': data,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        # Hash the block
        block_hash = self.hash_block(block)
        block['hash'] = block_hash
        # Add the block to the chain
        self.chain.append(block)
        return block

    def hash_block(self, block):
        # Convert the block to a JSON string and encode it
        block_string = json.dumps(block, sort_keys=True).encode()
        # Hash the block using SHA-256
        block_hash = hashlib.sha256(block_string).hexdigest()
        return block_hash
    
    def add_block(self, data):
        # Get the previous block
        previous_block = self.chain[-1]
        # Get the previous hash
        previous_hash = previous_block['hash']
        # Get Proof
        proof = FindProof(previous_block['proof'])
        # Generate a new block
        new_block = self.generate_block(proof, previous_hash, data)
        return new_block
    
    def get_previous_block(self):
        # Return the last block in the chain
        return self.chain[-1] if self.chain else None

def FindProof(pre_proof):
    diff = 3
    proof = random.randint(1, 1000000)
    canProof = False
    while not canProof:
        proof = random.randint(1, 1000000) 
        canProof = isProof(pre_proof, proof, diff)
    return proof


def isProof(pre_proof, proof, diff):
    guess = f'{pre_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:diff] == '0' * diff


# Example usage:
if __name__ == '__main__':
    # Create a blockchain
    my_blockchain = Blockchain()

    # Block 2
    Block2 = my_blockchain.add_block("Transaction A")

    # Block 3
    Block2 = my_blockchain.add_block("Transaction B")

    # User input a new block
    usr_input = str(input("Next block data: "))
    Next_Block = my_blockchain.add_block(usr_input)

    # Display the generated blockchain
    for block in my_blockchain.chain:
        print(block)
        
    Pre_block = my_blockchain.get_previous_block()
    print(Pre_block)
    