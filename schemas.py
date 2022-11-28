from pydantic import BaseModel


class DetailWeather(BaseModel):
    hour: str
    temp: int
    condition: str


class GeneralWeather(BaseModel):
    date: str
    hours: list[DetailWeather]


class Weathers(BaseModel):
    forecasts: list[GeneralWeather]
