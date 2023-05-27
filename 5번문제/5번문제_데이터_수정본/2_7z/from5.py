import scrypt

def enc(P):
	salt = b"contest2023"
	data = scrypt.hash(password=P, salt=salt, N=65536, r=8, p=1, buflen=48)
	KEY = data[:16]
	NONCE = data[16:32]
	AD = data[32:]
	print(data)
	return KEY, NONCE, AD

k = enc("#59mmk35nasd82@2023#")
for j in k:
	a = bytearray(j)
	b = ['0x'+hex(i)[2:].zfill(2) for i in a]
	print(b)