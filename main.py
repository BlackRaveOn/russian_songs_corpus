from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from es_utils.search_song import search


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def main_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/submit")
def submit_form(request: Request, name: str = Form(None), artist: str = Form(None), text: str = Form(None), size = Form(15)):
    search_list = []
    if name:
        search_list.append({"match": {"song_name": name}})
    if artist:
        search_list.append({"match": {"artist": artist}})
    if text:
        search_list.append({"match": {"song_txt": text}})

    search_results = search(search_list, size)

    if not search_results:
            return templates.TemplateResponse("no_results.html", {"request": request})

    return templates.TemplateResponse("search_results.html", {"request": request, "search_results": search_results})


@app.get("/similar-songs")
async def get_similar_songs(request: Request, song_id: int):
    # Здесь вы можете получить переданные параметры и выполнить нужные вам действия
    # Например, можно использовать song_name и artist для поиска похожих песен
    search_song = [{"match": {"song_id": song_id}}]
    # Вывод полученных параметров в консоль
    song = search(search_song)
    search_ids = song[0]["top_similar"]
    most_similar = search(search_ids, query_type="ids")
    return templates.TemplateResponse("search_results.html", {"request": request, "search_results": most_similar})
