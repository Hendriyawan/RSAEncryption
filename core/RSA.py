#  di tulis oleh Hendriyawan (gdev)
# selasa 26 juni 2018
# thanks to RedFox (Abdul Ghani)

# @gitbub : github.com/Hendriyawan
# 
#
"""
!!! Algoritma RSA.
dibuat oleh 3 orang peneliti dari MIT
(Massachussets Institute of Technology) pada tahun 1976, 
yaitu: 
1. Ron (R)ivest
2. Adi (S)hamir
3. Leonard (A)dleman.


!!! Properti Algoritma RSA
Besaran-besaran yang digunakan pada algoritma RSA:
1. p dan q bilangan prima, nilai p dan q tidak boleh sama.    (rahasia)
2. n = p q           (tidak rahasia)
3. phi = (p-1)(q-1)          (rahasia)
4. e (kunci enkripsi)          (tidak rahasia)
5. d (kunci dekripsi)          (rahasia)
6. m (plainteks)          (rahasia)
7. c (cipherteks)          (tidak rahasia)


"""
import random
import sys

"""
Dalam matematika , bilangan prima adalah bilangan asli yang lebih besar dari angka 1, yang faktor pembaginya adalah 1 dan bilangan itu sendiri. 2 dan 3 adalah bilangan prima. 4 bukan bilangan prima karena 4 bisa dibagi 2.
sumber : https://id.m.wikipedia.org/wiki/Bilangan_prima

"""
"""
fungsi ini untuk mengecek apakah bilangan prima, jika benar akan mengembalikan nilai benar (True)
"""
def is_prime(num):
	if num < 2:
		return False
	for prime in range(2, num):
		if num % prime == 0:
			return False
	return True
"""
fungsi ini untuk mencari bilangan prima dari yang terkecil (min) sampai yang terbesar (max)
"""
def find_prime(min, max):
	while 1:
		value = random.randrange(min, max)
		prime = is_prime(value)
		if prime:
			return value

"""
Algoritma Euclid untuk menentukan pembagi umum terbesar
Gunakan iterasi untuk membuatnya lebih cepat untuk bilangan bulat yang lebih besar
"""
def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a

"""
fungsi ini mencari nilai e (kunci public)
1.pilih e antara 1 dan phi (pilih e, sehingga e tidak bisa membagi rata phi).
membagi rata disini adalah phi di mod e dan hasilnya berupa 0.

contoh: phi phi % 3 = 0

2. menentukan nilai e dengan syarat GCD(e, phi) = 1
pastikan hasil dari GCD(e, phi) = 1. kembalikan nilai ke e

dimana e bilangan prima, dan 1 < e < phi
"""
def find_e(phi):
	while True:
		e = random.randrange(2, phi)
		if gcd(e, phi) == 1:
			break
	return e
	
"""
fungsi ini mencari nilai d (kunci private)
mencari nilai d = (d*e) mod phi = 1
hasilnya harus 1. baru kembalikan ke nilai d
"""
def find_d(e, phi):
	d = 2
	while 1:
		if ((d*e) % phi) == 1:
			break
		d += 1
	return d

class RSAEncryption:
	
	#generate keypair
	def gen_key(self):
		
		self.p = find_prime(128, 256)
		self.q = find_prime(128, 256)
		# nilai p dan q tidak boleh sama, p != q
		if self.p != self.q:
			self.n = self.p * self.q
			self.phi = (self.p-1) * (self.q-1)
			self.e = find_e(self.phi)
			self.d = find_d(self.e, self.phi)
			return ((self.e, self.n), (self.d, self.n))
			
	#fungsi ini untuk mengenkripsi
	#dengan rumus => c = (m^e) mod n
	# c = ciphertext
	# m = plaintext
	# e = kunci public
	# maksud (m^e) adalah nilai m dipangkatkan nilai e
	#jika di coding ke bahasa pemrograman python ubah ^ menjadi **
	#namun sebelum nya ubah dulu text ke nilai ascii, dengan menggunakan fungsi ord
	# c = (m**e) % n
	def encrypt(self, public_key, plaintext):
		self.e, self.n = public_key
		self.ciphertext = [(ord(m)**self.e) % self.n for m in plaintext]
		return self.ciphertext
	
	#fungsi ini unduk mendekripsi
	#dengan rumus => m = (c^d) mod n
	# m = plaintext
	# c = ciphertext
	# d = kunci private
	# m = (c**d) % n
	# setelah itu ubah kembali dari nilai ascii ke text/character
	def decrypt(self, private_key, ciphertext):
		self.d, self.n = private_key
		self.plaintext = [chr((c**self.d) % self.n) for c in ciphertext]
		return self.plaintext