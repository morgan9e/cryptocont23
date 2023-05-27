def XORFILE(f, g, save = ""):
	with open(f, 'rb') as f:
		q = f.read()

	with open(g, 'rb') as f:
		p = f.read()

	p = bytearray(p)
	q = bytearray(q)
	r = [(p[i] ^ q[i]) for i in range(min(len(p), len(q)))]
	r = bytes(r)

	if save:
		with open(save, "wb") as f:
			f.write(r)

	return r


X3 = XORFILE("3.bmp", "enc_3.bmp", "xor_3")
X4 = XORFILE("4.png", "enc_4.png", "xor_4")

XORFILE("enc_5.png", "xor_4", "xor_5")

# print(r[0:50])

# with open("key", "wb") as f:
# 	f.write(r)

# with open("key", "rb") as f:
# 	s = f.read()

# print(s[0:59])

# d = b"\x94PbA\xb2Y2\xb28\xbbqu\xf6\xab$\xc7\x86)\xd0\xe9\xcd\x95\xe3<\xe1\xd8\xd2~z\xb4\xab\xb6\xf3\x03\x89\x8a\xab\xb6\x08\x14\x04\x9f\x93\xb9)\x16_\x8do\x1fS\xad3T\r\x98\xe7\x0c>"

# g = [d + i for i in s.split(d)]
# print([len(i) for i in g])
# print(g[1])
# print(s[0:10])
# # print(s[-430:-1])

# with open("head", 'wb') as f:
# 	f.write(g[1])
# with open("body", 'wb') as f:
# 	f.write(key)
# with open("foot", 'wb') as f:
# 	f.write(footer)
