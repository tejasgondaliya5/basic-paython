str1 = "my name is tejas"
str2 = str1
str3 = 'tejas is a good boy'
print(str1)
print(str2)
print(str3)

str3 = "Tejas is bad boy"
print(str3)
print()

print(str1.lower())
print(str1.upper())
print(str1.swapcase())
print(str1.title())
print()

print("split function : ")
str4 = "Gondaliya Tejas Girishbhai "
#used to store database name surname lastname in diffrent columns
print(str4.split(" "))
print()

print("join function : ")
str5 = ("tejas" , "gondaliaya" , "girishbhai")
#used to display datbase to user some columns string join and display
print('_' . join(str5))