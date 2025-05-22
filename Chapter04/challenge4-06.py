
def number(x):
    """   
    return x**2.
    :param x: int.
    :return: ｘ２乗の結果.
    """
result=number(int(input("数を入力してください。")))
print(result)


x="今日のご飯"

def words():
    """
    print(x).
    :param x:文章.
    :print:文字を出力.
    """
words()


def number(x,y,z,a=10,b=15):
    """
    return x+y+z+a+b.
    :param x:float.
    :param y:float.
    :param a:float.
    :param b:float.
    :return:float sum of x,y,z,a and b.
    """
result=number(1,2,3)
print(result)



def number_1(x):
    """
    return x/2.
    :param x:int.
    :return:x割る2.
    """
number_1(16)
y=number_1(16)
print(y)


def number_2(y):
    """
    return y*4.
    :param y:ｘを2で割った結果.
    :return:y掛ける4.
    """
number_2(y)
result=number_2(y)
print(result)





try:
    n=input("数字を入力してください。")
    n=float(n)
    """
    print(n).
    :param n: float.
    :print: floatを出力.
    """
   

except(ValueError):
    """
    print("Invalid input.").
    :print: Invalid inputを出力.
    """

