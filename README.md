# Integrated Water Information System (IWIS) - Backend

This is the FastAPI backend for the Integrated Water Information System (IWIS), a digital monitoring and analytics platform designed to address ecological degradation at Hartbeespoort Dam.

## Features
* **REST API:** Fast, asynchronous endpoints built with FastAPI.
* **Spatial Database:** PostgreSQL integration for mapping sensor locations and citizen reports.
* **Automated Alerting:** Processes alerts when ecological thresholds (e.g., nitrates > 5.0 mg/L) are breached.
* **Real-Time Analysis:** On-the-fly Pearson correlation matrices calculated using Pandas.
* **Live Updates:** WebSocket support for real-time sensor data and alerts.

## Prerequisites
* **Python 3.13+**
* **PostgreSQL:** Running and accessible on port `5432`.
* **PostGIS Extension:** (Optional, but recommended for advanced spatial features).

## Quick Start (New Users)

**1. Database Setup**
Ensure PostgreSQL is running and create the `iwis` database:
```bash
# Linux (example)
sudo -u postgres createdb iwis
```

**2. Configure Environment**
Create a `.env` file in the `iwis-backend` directory:
```env
DATABASE_URL=postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/iwis
```
*Note: Using `127.0.0.1` is recommended over `localhost` for faster and more reliable connections.*

**3. Install Dependencies**
The project uses a shared virtual environment in the root directory. From the project root:
```bash
./venv/bin/pip install -r iwis-backend/requirements.txt
./venv/bin/pip install websockets
```

**4. Start the FastAPI Server**
From the `iwis-backend` directory:
```bash
../venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
The server will be available at `http://127.0.0.1:8000`.

**5. Seed Historical Data (Optional)**
Populate the database with realistic trend data for testing:
```bash
../venv/bin/python seed_data.py
```

## API Documentation
Once the server is running, you can explore the API using:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Troubleshooting
- **Connection Refused (DB):** Ensure the `DATABASE_URL` matches your local PostgreSQL credentials and that the service is running.
- **WebSocket Error:** Ensure the `websockets` library is installed and you are connecting to `ws://127.0.0.1:8000/ws/live`.
