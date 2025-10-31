from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79123456789"),
    Smartphone("Samsung", "Galaxy S24", "+79261234567"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79314567890"),
    Smartphone("Google", "Pixel 8", "+79551234567"),
    Smartphone("OnePlus", "12 Pro", "+79663451278")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")