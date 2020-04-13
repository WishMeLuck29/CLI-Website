# source link:
# https://www.w3schools.com/python/python_datatypes.asp

""" 
Tipe Data
"""

"""

python memiliki beberapa tipe data default, yaitu :
	text				-> str
	angka				-> int, float, complex
	data terurut 		-> list, tuple, range
	tipe data map		-> dict
	tipe data set		-> set, frozenset
	boolean				-> bool
	tipe data biner		-> bytes, bytearray, memoryview
"""

"""
Untuk mengetahui tipe data dari sebuah objek, dapat menggunakan:
	print (type(nama_variabel))
"""

"""

cara deklarasi tipe 							tipe data

x = str("Hello World") 							str 	
x = int(20) 									int 	
x = float(20.5) 								float 	
x = complex(1j) 								complex 	
x = list(("apple", "banana", "cherry")) 		list 	
x = tuple(("apple", "banana", "cherry")) 		tuple 	
x = range(6) 									range 	
x = dict(name="John", age=36) 					dict 	
x = set(("apple", "banana", "cherry")) 			set 	
x = frozenset(("apple", "banana", "cherry")) 	frozenset 	
x = bool(5) 									bool 	
x = bytes(5) 									bytes 	
x = bytearray(5) 								bytearray 	
x = memoryview(bytes(5)) 						memoryview

"""

""" 

Int
adalah tipe data angka, bisa positif atau negatif, bukan desimal dan unlimited (untuk python)


"""

""" 

Float
adalah tipe data angka yang memiliki angka desimal

dalam penggunaannya, bisa juga menggunakan huruf e / E.
contoh :
	x = 35e3
	y = 12E4
	z = -87.7e100 

"""
