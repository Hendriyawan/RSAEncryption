#! /usr/bin/env python
#
# selasa 26 juni 2018 by Hendriyawan
# copyrights 2018 gdev
# python 2.7.12
from core import RSA
from core import console
import sys

console.set_windowTitle('RSA-Encryption')
console.Banner()
cons = console.pyConsole()
rsa = RSA.RSAEncryption()

def main():
	# generate keypair
	# pasangan kunci public dan private
	# kunci public : (e, n)
	# kunci private : (d, n)
	
	print(cons.Proc('generate keypair...'))
	public_key, private_key = rsa.gen_key()
	
	print(cons.Proc('e : public key : %s' % str(public_key)))
	print(cons.Proc('d : private key : %s' % str(private_key)))
	message = raw_input(cons.Proc('Enter your message : '))
	
	if len(message) == 0:
		print(cons.Err('please enter your message ! \n'))
		sys.exit(1)
	else:
		ciphertext = rsa.encrypt(public_key, message)
		plaintext = rsa.decrypt(private_key, ciphertext)
		
		encrypted = ''.join(map(lambda x: str(x), ciphertext))
		decrypted = ''.join(plaintext)
		
		print('')
		print(cons.print_c('Encrypted message : %s' % str(encrypted)))
		print(cons.print_m('Decrypted message : %s' % str(decrypted)))
		print('')
	
if __name__ == '__main__':
	main()