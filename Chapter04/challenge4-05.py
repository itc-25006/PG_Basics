try: 
    n=input("数字を入力してください。")
    n=float(n)
    print(n)

except(ValueError):
    print("Invalid input.")
