def decode_vigenere(ciphertext, key):
	cipher_ascii = [ord(letter) for letter in ciphertext]
	key_ascii = [ord(letter) for letter in key]
	plain_ascii = []
	for i in range(len(cipher_ascii)):
		plain_ascii.append(((cipher_ascii[i]-key_ascii[i % len(key)]) % 26) +97)
	plaintext = ''.join(chr(i) for i in plain_ascii)
	return plaintext