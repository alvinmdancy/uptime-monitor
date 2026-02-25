from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from app.monitor import check_url

app = FastAPI(
    title="Uptime Monitor API",
    description="""
Monitor website uptime and response codes.

### Features
- Simple URL check
- One-page monitor UI
- Live dashboard
""",
    version="1.0.0",
    contact={
        "name": "Alvin Dancy",
        "url": "https://github.com/alvinmdancy",
    },
)

targets = []

# ---------------------------
# Homepage
# ---------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>Uptime Monitor</title></head>
        <body style="background:#0f172a;color:white;font-family:sans-serif;text-align:center;padding:60px;">
            <h1>🚀 Uptime Monitor</h1>
            <p>Simple website uptime checker.</p>
            <p>
                <a href="/monitor" style="color:#38bdf8;">Open Monitor</a> |
                <a href="/dashboard" style="color:#38bdf8;">Dashboard</a> |
                <a href="/docs" style="color:#38bdf8;">API Docs</a>
            </p>
        </body>
    </html>
    """

# ---------------------------
# Single-page Monitor UI
# ---------------------------
@app.get("/monitor", response_class=HTMLResponse)
def monitor():
    return """
    <html>
    <head>
        <title>Uptime Monitor</title>
        <script>
        async function checkStatus() {
            let url = document.getElementById('url').value;

            const res = await fetch(`/check?url=${url}`);
            const data = await res.json();

            const result = document.getElementById('result');
            const color = data.status === 'UP' ? 'lime' : 'red';

            result.innerHTML = `
                <p style="color:${color}; font-size:18px;">
                    ${data.url} — ${data.status}
                    ${data.status_code ? `(HTTP ${data.status_code})` : ''}
                </p>
            `;
        }
        </script>
    </head>
    <body style="background:#0f172a;color:white;font-family:sans-serif;text-align:center;padding:60px;">
        <h1>🌐 Uptime Monitor</h1>

        <input id="url" placeholder="Enter URL (e.g. google.com)"
               style="padding:10px;font-size:16px;width:300px;border-radius:6px;border:none;">
        <br><br>

        <button onclick="checkStatus()"
                style="padding:10px 20px;font-size:16px;border-radius:6px;border:none;background:#38bdf8;color:black;">
            Check Status
        </button>

        <div id="result" style="margin-top:30px;"></div>
    </body>
    </html>
    """

# ---------------------------
# API: Check Single URL
# ---------------------------
@app.get("/check")
def check_single(url: str = Query(...)):
    # Auto-add https if missing
    if not url.startswith("http"):
        url = "https://" + url

    result = check_url(url)

    return {
        "url": result.get("url", url),
        "status": "UP" if result.get("reachable") else "DOWN",
        "status_code": result.get("status_code"),
    }

# ---------------------------
# API: Add/List Targets
# ---------------------------
@app.post("/targets")
def add_target(url: str):
    targets.append(url)
    return {"message": "Target added", "url": url}

@app.get("/targets")
def list_targets():
    return {"targets": targets}

@app.get("/status")
def check_status():
    results = [check_url(url) for url in targets]
    return {"results": results}

@app.get("/health")
def health():
    return {"status": "ok"}

# ---------------------------
# Dashboard
# ---------------------------
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return """
    <html>
    <head>
        <title>Dashboard</title>
        <script>
        async function loadStatus() {
            const res = await fetch('/status');
            const data = await res.json();
            const container = document.getElementById('status');
            container.innerHTML = '';

            data.results.forEach(site => {
                const color = site.reachable ? 'lime' : 'red';
                container.innerHTML += `
                    <p style="color:${color}; font-size:18px;">
                        ${site.url} — ${site.reachable ? 'UP' : 'DOWN'}
                        ${site.status_code ? `(HTTP ${site.status_code})` : ''}
                    </p>
                `;
            });
        }
        setInterval(loadStatus, 5000);
        window.onload = loadStatus;
        </script>
    </head>
    <body style="background:#0f172a;color:white;font-family:sans-serif;text-align:center;padding:40px;">
        <h1>📊 Uptime Dashboard</h1>
        <div id="status">Loading...</div>
    </body>
    </html>
    """
