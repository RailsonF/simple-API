from fastapi import APIRouter

about_router = APIRouter(prefix="/about", tags=["EndPoint voltado para exibição das informações"])

@about_router.get("/")
def about():
    student = {"name:":"Railson Furtado", "email:": "railsonfurtado16@gmail.com", "course:": "Sistenas de Informação", "Github:": "https://github.com/RailsonF/", "City:": "Brejo Santo", "Interests": ["Treinar, assistir, tecnologia e estudar"]}
    return student
    