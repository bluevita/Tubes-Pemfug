import streamlit as st

menu_options = {
    1: 'Create Decorator',
    2: 'Multiple Decorators',
    3: 'Memoization using decorators',
    4: 'High Order Function lambda',
    5: 'High Order Function map()',
    6: 'High Order Function filter()',
    7: 'High Order Function sorted()',
}

def print_menu():
    for key in menu_options.keys():
        st.write (key, '--', menu_options[key] )

def option1():
     st.write('-----------------------------------------------------')
     st.title('                 Create Decorator')
     st.write('-----------------------------------------------------')
     @title
     def hallo():
       st.write('Before Decorator :\ntrio maut feri abdul habib\n\nAfter Decorator :')  
       return 'trio maut feri abdul habib'
     st.write(hallo())

def option2():
     st.write('-----------------------------------------------------')
     st.title('                 Multiple Decorators')
     st.write('-----------------------------------------------------')
     @splt_fungsi
     @upper_fungsi
     def hallo():
       st.write('Before Decorator :\ntrio maut feri abdul habib\n\nAfter Decorator :')  
       return 'trio maut feri abdul habib'
     st.write(hallo())

def option3():
     st.write('-----------------------------------------------------')
     st.title('           Memoization using decorators')
     st.write('-----------------------------------------------------')
     @memoize_factorial
     def facto(num):  
       if num == 1:
         return 1
       else:
         return num * facto(num-1)

     st.write(facto(5))
     st.write(facto(5)) # directly coming from saved memory

def option4():
    st.write('\n-----------------------------------------------------\n')
    st.title('||           High Order Function lambda              ||\n')
    st.write('\n-----------------------------------------------------\n')

    st.write("Studi Kasus : High Order Function")
    st.write("Lambda")    
    
    kuadrat = lambda x: x * x
    st.write('Perhitungan Kuadrat')
    angka = st.number_input('Masukkan bilangan : ')
    st.write("Hasil Kuadrat = ", kuadrat(float(angka)))
    
    st.write('Perhitungan Perkalian')
    angka = st.number_input('Masukkan bilangan pertama : ')
    angka1 = st.number_input('Masukkan bilangan kedua : ')
    kali = lambda x, y: x * y
    st.write('Hasil perkalian = ', kali(float(angka), float(angka1)))

def option5():
    st.write('\n-----------------------------------------------------\n')
    st.title('||            High Order Function map()              ||\n')
    st.write('\n-----------------------------------------------------\n')
    nilai = [1, 2, 3, 4, 5]
    pangkat = []
    st.write(nilai)

    def pangkat(x): return x ** 2
    st.write('\nmenggunakan list')
    st.write('Hasil = ', list(map(pangkat, nilai)))
    
def option6():
     st.write('\n-----------------------------------------------------\n')
     st.title('           High Order Function filter()')
     st.write('\n-----------------------------------------------------\n')
     alfabet = ['a', 'b', 'c', 'e', 'i', 'k', 'o', 'z']
     def filter_vocal(alfabet):
       vocal = ['a', 'i', 'u', 'e', 'o']
       if alfabet in vocal:
         return True
       else:
         return False

     vocal_terfilter = filter(filter_vocal, alfabet)
     st.write(alfabet)
     st.write('Huruf vocal yang tersaring adalah:')
     for vocal in vocal_terfilter:
       st.write(vocal)

     my_list = [1, 5, 4, 6, 8, 11, 3, 12]
     new_list = list(filter(lambda x: (x%2 == 0) , my_list))
     st.write('\n', my_list)
     st.write('Angka genap yang tersaring adalah:')
     st.write(new_list)

def option7():
    st.write("-----------------------------------------------------")
    st.title("          High Order Function sorted()")
    st.write("-----------------------------------------------------")

    pyList = ['e', 'a', 'u', 'o', 'i']
    st.write(pyList)
    st.write("Hasil sorted list = ", sorted(pyList))

    pyString = 'Python'
    st.write("Hasil sorted string = ", sorted(pyString))

    pyTuple = ('e', 'a', 'u', 'o', 'i')
    st.write("Hasil sorted tuple = ", sorted(pyTuple))

    data_set ={'e', 'a', 'u', 'o', 'i'}
    st.write("Hasil sorted reverse = ", sorted(data_set, reverse=True))

    data_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
    st.write("Hasil sorted reverse = ", sorted(data_dict, reverse=True))

    def takeSecond(elem):
        return elem[1]

    random = [(2, 2), (3, 4), (4, 1), (1, 3)]
    sortedList = sorted(random, key=takeSecond)
    st.write(random)
    st.write("Sorted key list :", sortedList)
    
# A decorator function for function 'f' passed
# as parameter
memory = {}

def memoize_factorial(f):
	
	# This inner function has access to memory
	# and 'f'
	def inner(num):
		if num not in memory:
			memory[num] = f(num)
			st.write('result saved in memory')
		else:
			st.write('returning result from saved memory')
		return memory[num]

	return inner

def upper_fungsi(fungsi):
  def wrapper():
    func_ret = fungsi()
    output = func_ret.upper()
    return output
  return wrapper

def splt_fungsi(fungsi):
  def wrapper():
    func_ret = fungsi()
    output = func_ret.split()
    return output
  return wrapper

def title(fungsi):
  def wrapper(): #menmanggil fungsi
    func_ret=fungsi()
    ubah_ke_title=func_ret.title()
    return ubah_ke_title
  return wrapper

if __name__=='__main__':
    st.title("PROGRAM MENU DECORATOR AND HIGH ORDER FUNCTION")
    option1()
    option2()
    option3()
    option4()
    option5()
    option6()
    option7()
