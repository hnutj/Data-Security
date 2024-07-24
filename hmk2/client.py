from phe import paillier

#get the data
data=list(map(int,input("input the data:").split()))

#generate the keypairs
public_key,private_key=paillier.generate_paillier_keypair()
with open("priv_key","wb+") as f_pvk:
    f_pvk.write(private_key.)
f_pvk.closed

#encrypt the data
enc_data=list(map(public_key.encrypt,data))
with open("enc_data","wb+") as f:
    f.write(enc_data)
f.closed

