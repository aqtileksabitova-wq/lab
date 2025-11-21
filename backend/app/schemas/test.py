"""Test, question, and answer schemas."""

from pydantic import BaseModel, Field, ConfigDict

from app.models.enums import QuestionType


class AnswerBase(BaseModel):
    answer_text: str
    is_correct: bool = False


class AnswerRead(AnswerBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class QuestionBase(BaseModel):
    question_text: str
    question_type: QuestionType = QuestionType.SINGLE
    explanation: str | None = None


class QuestionRead(QuestionBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    answers: list[AnswerRead]


class QuestionCreate(QuestionBase):
    answers: list[AnswerBase]


class TestBase(BaseModel):
    title: str
    description: str | None = None


class TestRead(TestBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    lecture_id: int
    questions: list[QuestionRead]


class TestCreate(TestBase):
    lecture_id: int
    questions: list[QuestionCreate]


class TestUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    questions: list[QuestionCreate] | None = None


class AnswerSubmission(BaseModel):
    answer_ids: list[int] = Field(default_factory=list)


class QuestionSubmission(BaseModel):
    question_id: int
    selected_answer_ids: list[int]


class TestSubmission(BaseModel):
    answers: list[QuestionSubmission]



