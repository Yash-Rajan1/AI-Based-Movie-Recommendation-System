#  🎬 Movie Recommender System

A content-based movie recommendation engine built with Python and Machine Learning, featuring a dynamic web interface and real-time poster fetching.

## 🚀 Live Demo
https://ai-based-movie-recommendation-system.streamlit.app/

## 📌 Project Overview
This project provides personalized movie recommendations by analyzing metadata such as genres, keywords, cast, and crew. It uses Natural Language Processing (NLP) to find mathematical similarities between films, delivering a seamless discovery experience for users.

### Key Features:
* *Content-Based Filtering:* Recommends movies similar to a user's choice based on metadata "tags."
* *Real-time Posters:* Fetches high-quality movie posters using the *TMDb API*.
* *Cloud-Optimized:* Implements automated large-file handling and memory caching for stable deployment.

---

## 🛠️ Technical Stack
* *Language:* Python 3.13
* *Frontend:* [Streamlit](https://streamlit.io/)
* *Machine Learning:* Scikit-Learn (CountVectorizer, Cosine Similarity)
* *Data Handling:* Pandas, Pickle
* *Cloud Storage:* Google Drive (via gdown)

---

## 🧠 How it Works

### 1. Vectorization & Similarity
We convert movie "tags" into vectors using a Bag-of-Words model. To find the relationship between movies, we calculate the *Cosine Similarity* between these vectors.



### 2. Large File Management (The "502 Fix")
Due to the size of the similarity matrix (~400MB+), standard GitHub uploads and small RAM server environments (like Render's free tier) often fail. 
* *Storage:* The similarity.pkl is hosted on Google Drive and downloaded programmatically.
* *Memory Management:* Used @st.cache_resource to ensure the matrix is loaded into RAM only once, preventing 502 Bad Gateway errors.

