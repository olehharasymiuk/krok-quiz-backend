from typing import Union

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from pydantic.types import List

from misc.functions import get_new_question
from questions_storage import get_all_years

app = FastAPI(
    title='Krok'
)


class Question(BaseModel):

    index: str
    question: str
    options: list
    answer: str


@app.get("/shuffle")
def get_question_by_year_and_index():

    return get_new_question(shuffle=True)


@app.get("/{year}")
def get_question_by_year_and_index(year: int = Path(ge=min(get_all_years()), le=max(get_all_years())), question_index: int = Query(None)):

    if question_index is None:
        return get_new_question(year, shuffle=True)

    return get_new_question(year, question_index)

