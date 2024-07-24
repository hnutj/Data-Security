from phe import paillier
from cryptography.fernet import Fernet
import random
import math

#client init
key=Fernet.generate_key()
f=Fernet(key)

##client plain data
msg_list=[1,2,3,4,5,6,7,8,9,10]
msglist_len=len(msg_list)
enc_msglist=list(f.encrypt(x.to_bytes()) for x in msg_list)
a=1

#client op
public_key, private_key = paillier.generate_paillier_keypair()
pos=random.randint(0,msglist_len-1)
print(pos)

##select data
select_list=[]
encryt_list=[]
for i in range(msglist_len):
    select_list.append(i==pos)
    encryt_list.append(public_key.encrypt(select_list[i]))
    #print(encryt_list[i].ciphertext())

#server calculates   
c=0
for i in range(msglist_len):
    c=c+encryt_list[i]*int.from_bytes(enc_msglist[i],byteorder='little',signed=False)

tmp=private_key.decrypt(c)
byte_length = math.ceil(tmp.bit_length() / 8)
m=f.decrypt(tmp.to_bytes(byte_length, byteorder='little'))
print(int.from_bytes(m,byteorder='little',signed=False))