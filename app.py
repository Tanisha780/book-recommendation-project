import pickle
import streamlit as st
import numpy as np
st.header("Book Recommender System ")
popular_df  = pickle.load(open('popular.pkl.pkl','rb'))
books_name = pickle.load(open('book.pkl','rb'))
filtered_rating = pickle.load(open('filter.pkl','rb'))
pivot_table = pickle.load(open('pt.pkl','rb'))

def fetch_poster(similar_items):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in similar_items:
        book_name.append(pivot_table.index[book_id])

    for name in book_name[0]:
        ids= np.where(filtered_rating['Book-Title']==name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = filtered_rating.iloc[idx]['Image-URL-M']
        poster_url.append(url)

    return poster_url    

def recommend_books(books_name):
    book_list = []
    book_id = np.where(pivot_table.index==books_name)[0][0]
    similar_items = sorted(list(enumerate(pivot_table[book_id,:])),key = lambda x:x[1],reverse=True[1:6])
    
    poster_url = fetch_poster(similar_items)
    
    for i in similar_items:
      print(pivot_table.index[i[0]])
  
    for j in books:
        book_list.append(j)
    return book_list,poster_url       

selected_books = st.selectbox(
    "Type or select a Book",
    books_name
)

if st.button('Show Recommendation'):
    Recommendation_books,poster_url = recommend_books(selected_books)
    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.text(Recommendation_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(Recommendation_books[2])
        st.image(poster_url[2])
    with col3:
        st.text(Recommendation_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(Recommendation_books[4])
        st.image(poster_url[4])    
    with col5:
        st.text(Recommendation_books[1])
        st.image(poster_url[5])    
