from pydantic import BaseModel


class DetailWeatherSchema(BaseModel):
    hour: str
    temp: int
    condition: str


class GeneralWeatherSchema(BaseModel):
    date: str
    hours: list[DetailWeatherSchema]


class WeathersSchema(BaseModel):
    forecasts: list[GeneralWeatherSchema]
