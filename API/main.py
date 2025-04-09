from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from recommender import get_recommendations

app = FastAPI()

# Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Input model for recommendation request
class QueryInput(BaseModel):
    query: str

# Recommendation Endpoint
@app.post("/recommend")
def recommend(data: QueryInput):
    try:
        results = get_recommendations(data.query)
        return {"recommended_assessments": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
