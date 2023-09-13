from pydantic import BaseModel

class NewsArticle(BaseModel):
    title:str=""
    authors:list[str]=[""]
    article_text:str=""
    image_href:list[str] = [
        ''
    ]
class NewsInfo(BaseModel):
    title:str=""
    description:str=""
    href:str=""
    article:NewsArticle = NewsArticle()