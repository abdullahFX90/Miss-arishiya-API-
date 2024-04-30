import tkinter as tk
from tkinter import ttk
import requests


api_key = "6e065691f23ab4af3809eff24561360f"

def movie_search(query):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': api_key,
        'query': query
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get('results', [])

def search():
    query = entry.get()
    results = movie_search(query)
    
    listbox.delete(0, tk.END)
    for result in results:
        listbox.insert(tk.END, result['title'])
    
    global search_results
    search_results = results

def show_information():
    selected_index = listbox.curselection()
    if selected_index:
        movie_index = selected_index[0]
        movie = search_results[movie_index]
        movie_details = Get_details(api_key, movie['id'])
        
        details_window = tk.Toplevel(abd)
        details_window.title("Movie Details")
        details_label = ttk.Label(details_window, text=movie_details['title'])
        details_label.pack(padx=10, pady=5)
        overview_label = ttk.Label(details_window, text=movie_details['overview'])
        overview_label.pack(padx=10, pady=5)

def Get_details(api_key, movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data


abd = tk.Tk()
abd.title("Movie Search")
abd.configure(background="lightblue")

style = ttk.Style()


style.configure('TButton', background='black')

label = ttk.Label(abd, text="Enter movie name:")
label.pack(pady=5)
entry = ttk.Entry(abd)
entry.pack(pady=5)
search_button = ttk.Button(abd, text="Search", command=search )
search_button.pack(pady=5)
listbox = tk.Listbox(abd, width=50)
listbox.pack(pady=5)
details_button = ttk.Button(abd, text="Show about movie", command=show_information ,)
details_button.pack(pady=5)


abd.mainloop()