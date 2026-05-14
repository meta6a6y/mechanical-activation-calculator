from typing import List, Optional  # Добавляем Optional в импорт
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from app.services.calculator_service import calculate_samples


class SampleIn(BaseModel):
    name: str
    crystal_system: str
    h: int
    k: int
    l: int
    d_values: List[float]
    time_values: List[float]
    a_parameter: Optional[float] = None  # Optional теперь определен


class RequestBody(BaseModel):
    samples: List[SampleIn]


app = FastAPI(title="Crystal Lattice Calculator")

# Добавляем CORS для разработки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/templates")


@app.post("/calculate")
def calculate(body: RequestBody):
    from app.models.sample import Sample

    samples = [
        Sample(
            name=s.name,
            crystal_system=s.crystal_system,
            h=s.h,
            k=s.k,
            l=s.l,
            d_values=s.d_values,
            time_values=s.time_values,
            a_parameter=s.a_parameter
        )
        for s in body.samples
    ]

    results = calculate_samples(samples)

    # Конвертируем в JSON-совместимый формат
    return [
        {
            "sample_name": r.sample_name,
            "parameter_type": r.parameter_type,
            "lattice_parameters": r.lattice_parameters,
            "deviations": r.deviations,
            "time_values": r.time_values,
        }
        for r in results
    ]


@app.get("/ui", response_class=HTMLResponse)
def ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)