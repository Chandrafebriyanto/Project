# constants adalah sebuah nilai variabel yang tidak berubah
# dalam program, biasanya digunakan untuk menyimpan nilai yang tetap

def area_of_circle(radius):
    """Menghitung luas lingkaran berdasarkan jari-jari."""
    PI = 3.14159  # nilai tetap untuk π
    return PI * (radius ** 2)

radius = float(input())
print(area_of_circle(radius))