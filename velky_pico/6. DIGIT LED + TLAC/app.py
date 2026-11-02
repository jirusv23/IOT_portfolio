from flask import Flask, jsonify, render_template_string
from gpiozero import LED, Button

app = Flask(__name__)

# BCM číslování: Pin 11 = GPIO 17, Pin 13 = GPIO 27
led = LED(17)
button = Button(27, pull_up=True, bounce_time=0.05)

# Fyzické tlačítko přepíná stav LED
button.when_pressed = led.toggle

HTML_PAGE = """
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>Raspberry Pi LED Controller</title>
    <style>
        body { font-family: system-ui, sans-serif; text-align: center; margin-top: 80px; background: #f4f4f9; }
        .card { background: white; padding: 40px; border-radius: 12px; display: inline-block; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .status { font-size: 24px; margin: 20px 0; font-weight: bold; }
        .on { color: #2ecc71; }
        .off { color: #e74c3c; }
        button { font-size: 18px; padding: 14px 28px; cursor: pointer; border: none; border-radius: 8px; background: #007bff; color: white; }
        button:active { transform: scale(0.98); }
    </style>
</head>
<body>
    <div class="card">
        <h1>Raspberry Pi 4 – LED Control</h1>
        <div class="status">Stav LED: <span id="state" class="off">VYPNUTO</span></div>
        <button onclick="toggleLed()">Přepnout LED</button>
    </div>

    <script>
        async function toggleLed() {
            const res = await fetch('/api/toggle', { method: 'POST' });
            const data = await res.json();
            updateUI(data.is_on);
        }

        async function syncState() {
            const res = await fetch('/api/state');
            const data = await res.json();
            updateUI(data.is_on);
        }

        function updateUI(isOn) {
            const el = document.getElementById('state');
            el.textContent = isOn ? 'ZAPNUTO (ON)' : 'VYPNUTO (OFF)';
            el.className = isOn ? 'on' : 'off';
        }

        // Automatická synchronizace každých 500ms pro okamžité promítnutí stisku fyzického tlačítka
        setInterval(syncState, 500);
        syncState();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/api/toggle', methods=['POST'])
def api_toggle():
    led.toggle()
    return jsonify({'is_on': led.is_lit})

@app.route('/api/state', methods=['GET'])
def api_state():
    return jsonify({'is_on': led.is_lit})

if __name__ == '__main__':
    # Naslouchá na všech rozhraních na portu 5000
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
