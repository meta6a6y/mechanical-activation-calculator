from app.models.sample import Sample
from app.services.calculator_service import calculate_samples
import uvicorn

sample_1 = Sample(
    name="TaN",
    crystal_system="hexagonal",

    h=1,
    k=1,
    l=0,

    d_values=[
        2.5958,
        2.5938,
        2.5885
    ],

    time_values=[
        0,
        15,
        30
    ]
)


sample_2 = Sample(
    name="HfC",
    crystal_system="cubic",

    h=1,
    k=1,
    l=1,

    d_values=[
        2.6803,
        2.6814,
        2.6775
    ],

    time_values=[
        0,
        15,
        30
    ]
)


samples = [sample_1, sample_2]

results = calculate_samples(samples)

# for result in results:
#     print(result)


if __name__ == "__main__":
    uvicorn.run("app.api:app", host="127.0.0.1", port=8000, reload=True)