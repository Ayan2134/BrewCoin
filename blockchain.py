from hashlib import sha256

def update_hash(*args) :
        hashing_text=""
        h=sha256() # h acts as a object of class sha256 
        for arg in args :
            hashing_text+=str(arg)
        h.update(hashing_text.encode()) #we call inbuilt function update() from object h which takes input in bytes and returns hash value in non readable form
        return h.hexdigest()#convert the hash value to hexadecimal string to make it readable

class  Block :
    data=None
    hash=None
    prev_hash="0"*64 #sha 256 has a 64 digit hash number as each digit is hexadecimal
    nonce=0

    def __init__(self,data,block_num) :
        self.data=data
        self.block_num=block_num

    def hash(self) :
        return update_hash(self.prev_hash,self.block_num,self.data,self.nonce)
    
    def __str__(self):
         return f"Block Number : {self.block_num}\n Block Hash : {self.hash()}\n Previous Block Hash : {self.prev_hash}\n Data : {self.data}\n Nonce : {self.nonce}"
    
class Blockchain :
     difficulty=3
     
     def __init__(self,chain=[]) :
          self.chain=chain

     def add_block(self,block) :
        new_block={ "hash" : block.hash(),
                    "previous _block" : block.prev_hash,
                    "Block_num" : block.block_num ,
                    "Data" : block.data ,
                    "Nonce" : block.nonce
                   }
        self.chain.append(new_block)
     def mine(self,block) :
        difficulty=self.difficulty
        try :
            block.prev_hash=self.chain[-1].get("hash")
        except :
             pass
        while True:
             if block.hash()[:difficulty]=="0"*difficulty :
                  self.add_block(block)
                  break
             else :
                  block.nonce+=1

def main() :
     blockchain=Blockchain()
     database=[]
     print("Add data to database :")
     database=input().split()
     i=0 #i is the number of blocks in chain
     for data in database :
          i+=1
          block=Block(data,i)
          blockchain.mine(block)
     for block in blockchain.chain :
          print(block)

if __name__ == '__main__' :
     main()