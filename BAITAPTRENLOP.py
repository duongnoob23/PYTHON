from math import *

def display_message():
    print("Mình đang làm Bài tập cá nhân phần Hàm số")

def favourite_book(s):
    print("Một trong những cuốn sách yêu thích là "+s)

def make_shirt(size, message):
    print("Áo size " + str(size) + " với thông điệp: " + message)

def description_city (city,country):
    print(city+" Là một trong các thành phố của "+country)

def city_country (city,country):
    return city+","+country

def make_album(artist, title, songs=None):
    album = {'Ca sĩ': artist, 'Tên album': title}
    if songs:
        album['songs'] = songs
    return album

def show_messages(messages):
    for message in messages:
        print(message)

def send_message(message, sent_messages):
    print("Gửi tin nhắn: " + message)
    sent_messages.append(message)

def sandwich(*ingredients):
    print("Bánh sandwich của bạn bao gồm:")
    for ingredient in ingredients:
        print("- " + ingredient)

def build_profile(first_name, last_name, **kwargs):
    profile = {'first_name': first_name, 'last_name': last_name}
    profile.update(kwargs)
    return profile

def make_car(manufacturer, model, **kwargs):
    car = {'manufacturer': manufacturer, 'model': model}
    car.update(kwargs)
    return car

def send_messages(messages):
    sent_messages = []
    while messages:
        current_message = messages.pop(0)
        print("Sending message:", current_message)
        sent_messages.append(current_message)
    return sent_messages





#7.1
display_message()
#7.2
favourite_book("Cừu Vui Vẻ Và Sói Xám")
#7.3
make_shirt(50,"Big Size")
#7.4
make_shirt(message="Mini Size",size=30)
#7.5
description_city("Hà Nội","VIỆT NAM")
description_city("HẢI PHÒNG","VIỆT NAM")
description_city(country="FRANCE",city="PARIS")
#7.6
print(city_country("NEW YORK","USA"))
print(city_country("SEOUL","KOREA"))
print(city_country("TRÙNG KHÁNH","CHINA"))
#7.7
print( make_album("Thái Hoàng", "Nhạc không thị trường"))
print(make_album("Hoàng Thùy Linh", "Link", 12))
print(make_album("Taylor Swift", "Lover ", 8))
#7.8
while True:
    print("Nhập thông tin album nhạc (hoặc 'q' để thoát):")
    artist = input("Tên nghệ sĩ: ")
    if artist == 'q':
        break
    title = input("Tiêu đề album: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)
#7.9
messages = ["Tin nhắn 1", "Tin nhắn 2", "Tin nhắn 3"]
show_messages(messages)
#7.10
messages = ["Tin nhắn 1", "Tin nhắn 2", "Tin nhắn 3"]
sent_messages = []
for message in messages:
    send_message(message, sent_messages)

print("Các tin nhắn đã gửi:")
show_messages(sent_messages)
print("Các tin nhắn ban đầu:")
show_messages(messages)
#7.11
messages = ['Hello', 'Hi', 'How are you?']
sent_messages = send_messages(messages[:])
print("Danh sách ban đầu:", messages)
print("Danh sách tin nhắn đã gửi:", sent_messages)
#7.12
sandwich('Thịt gà', 'Phô mai')
sandwich('Thịt bò', 'Rau xanh', 'Hành')
sandwich('Trứng', 'Bacon', 'Rau diếp')

#7.13
my_profile = build_profile('John', 'Doe', age=25, city='New York', occupation='Developer')
print(my_profile)

#7.14
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

#7.15
from print_models import print_models, show_completed_models

unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)






