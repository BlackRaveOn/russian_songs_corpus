# russian_songs_corpus
 This repository implements text corpus of russian popular songs
## Install
Run elasticsearch-7.1.0 on localhost:9200 (it's default address) and place your corpus in json format to **data** folder
```
git clone https://github.com/BlackRaveOn/russian_songs_corpus.git
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
cd es_utils
python create_corpus.py
cd ..
uvicorn main:app --reload
```
Go to http://127.0.0.1:8000/ and work with it :)
