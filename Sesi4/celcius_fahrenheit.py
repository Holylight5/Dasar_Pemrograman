#Program untuk mengonversi suhu dari Celsius ke Fahrenheit atau sebaliknya, sesuai dengan input pengguna.
def fahrenheit_to_celcius(f):
    return (f - 32) * 5/9

def celcius_to_fahrenheit(c):
    return c * 9/5 + 32

#Fahrenheit ke celcius
print(40*"=")
fahrenheit = float(input("masukkan nilai fahrenheit: "))
celcius = fahrenheit_to_celcius(fahrenheit)
print(fahrenheit, "Fahrenheit sama dengan", "{:.2f}".format(celcius),"celcius")

#Celcius ke fahrenheit
print(40*"=")
celcius = float(input("masukkan nilai celcius: "))
fahrenheit = celcius_to_fahrenheit(celcius)
print(celcius, "celcius sama dengan", "{:.2f}".format(fahrenheit), "fahrenheit")