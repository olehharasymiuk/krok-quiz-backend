from typing import Union

from fastapi import FastAPI, Path
from pydantic import BaseModel
from pydantic.types import List

from misc.functions import get_new_question
from questions_storage import get_all_years

app = FastAPI()


class Question(BaseModel):

    index: str
    question: str
    options: list
    answer: str


@app.get("/{year}/{question_index}", response_model=List[Question])
def get_question_by_year_and_index(year: int = Path(ge=min(get_all_years()), le=max(get_all_years())), question_index: int = Path(ge=0)):

    return get_new_question(year, question_index)

