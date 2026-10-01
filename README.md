# CardioAgent-Ops


## Run locally

From the project root:

```text
python app.py
```

Open <http://localhost:8050>, click the file picker, and choose a WAV file.

## Run with Docker

The image contains only the application and does not need the dataset:

```text
docker compose up --build
```

Then open <http://localhost:8050>.
