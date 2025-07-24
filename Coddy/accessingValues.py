# accessing values adalah cara untuk mengambil nilai dari sebuah dictionary berdasarkan kunci yang diberikan.
# Dalam contoh ini, kita akan mengambil nilai dari dictionary yang berisi nama negara dan ibu kotanya.


def get_capital(country_capitals, country_name):
    country = country_capitals
    print(country[country_name])
    
get_capital({"Indonesia": "Jakarta", "Malaysia": "Kuala Lumpur"}, "Indonesia")  # Should print Jakarta