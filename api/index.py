from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 154.31,
    "uptime_pct": 97.604,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 135.8,
    "uptime_pct": 98.531,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 222.7,
    "uptime_pct": 97.795,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 167.99,
    "uptime_pct": 97.752,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 209.35,
    "uptime_pct": 99.432,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 173.63,
    "uptime_pct": 99.27,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 198.84,
    "uptime_pct": 97.755,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 125.26,
    "uptime_pct": 98.432,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 161.78,
    "uptime_pct": 98.418,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 221.95,
    "uptime_pct": 97.886,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 217.73,
    "uptime_pct": 99.051,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 115.04,
    "uptime_pct": 99.118,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 180.38,
    "uptime_pct": 97.706,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 220.57,
    "uptime_pct": 97.936,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 235.82,
    "uptime_pct": 99.429,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 178.37,
    "uptime_pct": 97.419,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 186.57,
    "uptime_pct": 97.652,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 198.25,
    "uptime_pct": 98.982,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 197.74,
    "uptime_pct": 98.968,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 163.91,
    "uptime_pct": 97.701,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 153.64,
    "uptime_pct": 97.645,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 159.11,
    "uptime_pct": 99.426,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 145.8,
    "uptime_pct": 98.666,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 168.41,
    "uptime_pct": 98.284,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 173.64,
    "uptime_pct": 97.453,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 135.03,
    "uptime_pct": 98.22,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 136.41,
    "uptime_pct": 98.027,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 222.25,
    "uptime_pct": 97.477,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 217.19,
    "uptime_pct": 98.879,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 173.56,
    "uptime_pct": 99.22,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 202.3,
    "uptime_pct": 98.747,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 155.57,
    "uptime_pct": 98.795,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 188.88,
    "uptime_pct": 97.65,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 191.48,
    "uptime_pct": 99.092,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 123.57,
    "uptime_pct": 98.743,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 223.16,
    "uptime_pct": 98.576,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}