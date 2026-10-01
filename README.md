# WAV Analyser

A small web application that lets a user choose one `.wav` file from their
device. The selected file is previewed in the browser; no dataset is scanned
or loaded automatically. The **Analyse** button is reserved for the future
analysis implementation.

## Run locally

From the project root:

```text
python app.py
```

Open <http://localhost:8000>, click the file picker, and choose a WAV file.

## Run with Docker

The image contains only the application and does not need the dataset:

```text
docker compose up --build
```

Then open <http://localhost:8000>.
