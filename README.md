# codex-hello3

This repository contains a minimal Flask web server that exposes a `/hello` endpoint.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   python app.py
   ```
3. Visit `http://localhost:5000/hello` to receive the current date and time.
4. Visit `http://localhost:5000/image` to see the `static/logo.svg` image rendered in a simple HTML page.

## Utilities

### Play a 1 kHz tone (Windows)

To play a 1 kHz tone for one second on Windows, run:

```bash
python play_1khz.py
```
