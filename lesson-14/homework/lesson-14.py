# 1

import json
s = { "first_name": "Ali", "age": 18}

with open('students.json', 'w') as students:
  json.dump(s, students)

# 2
biriinchi bolib yangi terminal ochiladi keyin pip install requests qilinadi undan keyin import qilinadi

import requests 
url = requests.get(https://openweathermap.org/)

 with open('ob-havo.json', 'w') as forecast:
 d1= json.dump(url, forecast)
 
# 3


import json
import os
from typing import Optional, List, Dict

BOOKS_FILE = "books.json"

def load_books() -> List[Dict]:
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books: List[Dict]) -> None:
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def next_id(books: List[Dict]) -> int:
    return (max((b["id"] for b in books), default=0) + 1)

def add_book(title: str, author: Optional[str] = None, year: Optional[int] = None) -> Dict:
    books = load_books()
    book = {
        "id": next_id(books),
        "title": title,
        "author": author,
        "year": year
    }
    books.append(book)
    save_books(books)
    return book

def update_book(book_id: int, title: Optional[str] = None,
                author: Optional[str] = None, year: Optional[int] = None) -> bool:
    books = load_books()
    for b in books:
        if b["id"] == book_id:
            if title is not None:
                b["title"] = title
            if author is not None:
                b["author"] = author
            if year is not None:
                b["year"] = year
            save_books(books)
            return True
    return False

def delete_book(book_id: int) -> bool:
    books = load_books()
    new_books = [b for b in books if b["id"] != book_id]
    if len(new_books) == len(books):
        return False  # topilmadi
    save_books(new_books)
    return True

def list_books() -> List[Dict]:
    return load_books()

if __name__ == "__main__":
    # 1) Dastlabki kitoblarni yaratish (faqat bir marta kerak bo‘ladi):
    if not os.path.exists(BOOKS_FILE):
        initial = []
        save_books(initial)
        # Siz aytgan kitoblar:
        add_book("Atomic Habits", author="James Clear", year=2018)
        add_book("Molxona")  # author/year keyin to‘ldirilsa ham bo‘ladi
        add_book("G‘arbiy frontda o‘zgarish yo‘q", author="Erich Maria Remarque")
        add_book("Qimorboz", author="Fyodor Dostoyevskiy")

    # 2) Ro‘yxatni ko‘rish
    print("Boshlang‘ich ro‘yxat:")
    for b in list_books():
        print(b)

    # 3) Yangilash (masalan, 'Molxona' yilini qo‘shamiz)
    books_now = list_books()
    molxona = next((b for b in books_now if b["title"] == "Molxona"), None)
    if molxona:
        update_book(molxona["id"], year=2000)

    # 4) O‘chirish (misol uchun, ID=1 bo‘lsa o‘chirib ko‘ramiz)
    delete_book(1)

    print("\nYangilangan ro‘yxat:")
    for b in list_books():
        print(b)


# 4

import requests
import random

API_KEY = "YOUR_API_KEY"
BASE_URL = "http://www.omdbapi.com/"

def get_movies_by_keyword(keyword):
    """Kalit so‘z bo‘yicha filmlar ro‘yxatini qaytaradi"""
    url = f"{BASE_URL}?apikey={API_KEY}&s={keyword}"
    response = requests.get(url)
    data = response.json()
    if "Search" in data:
        return data["Search"]
    return []

def get_movie_details(imdb_id):
    """IMDB ID bo‘yicha filmning to‘liq ma’lumotini oladi"""
    url = f"{BASE_URL}?apikey={API_KEY}&i={imdb_id}&plot=short"
    response = requests.get(url)
    return response.json()

def recommend_movie(genre_keyword):
    """Berilgan janr bo‘yicha tasodifiy film tavsiya qiladi"""
    movies = get_movies_by_keyword(genre_keyword)
    if not movies:
        print("Hech narsa topilmadi 😢")
        return
    movie = random.choice(movies)
    details = get_movie_details(movie["imdbID"])
    
    print("🎬 Sizga tavsiya etiladigan film:")
    print("Nomi:", details.get("Title"))
    print("Yili:", details.get("Year"))
    print("Janr:", details.get("Genre"))
    print("Rejissyor:", details.get("Director"))
    print("IMDB reyting:", details.get("imdbRating"))
    print("Qisqa mazmun:", details.get("Plot"))

if __name__ == "__main__":
    genre = input("Qaysi janrdagi filmni xohlaysiz? (masalan: Action, Drama, Comedy): ")
    recommend_movie(genre)

