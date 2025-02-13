import streamlit as st
import math

#素数判定
def factorize(n):
    c = 0

    for i in range(2 , int(n ** 0.5) + 1):
        if n % i == 0:
            return 'False ' + str(i)
            c = 1
            break
        if c == 0:
            return True

st.title('そすー')
a = st.number_input('a' , placeholder = "aの値を入力してください")
b = st.number_input('b' , placeholder = 'bの値を入力してください')

#素数ならTrue,合成数ならFalseを返す
x = factorize(3 * a + 2 * b)

#a,bの条件の確認および例外処理
if math.gcd(int(a) , int(b)) != 1 or a != 0 and a % 2 == 0 or b != 0 and b % 3 == 0 or a % 5 == b % 5 and a != 1 and b != 1:
    x = False

st.write('factorize:' + str(x))
st.write('number:' + str(int(3 * a + 2 * b)) , '' , 'a:' + str(int(a)) , '' , 'b:' + str(int(b)))
st.write('gcd:' + str(math.gcd(int(a) , int(b))) , '' * 2 , 'a.mod:' + str(int(a % 2)) , '' , 'b.mod:' + str(int(b % 3)))