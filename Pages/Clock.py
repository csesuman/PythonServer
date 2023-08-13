

def digital_clock_view():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Large Clock</title>
    <style>
      body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        background-color: black; /* Changed background color to black */
      }

      #clock {
        font-size: 10vw; /* Clock size set to 10% of viewport width */
        font-weight: bold;
        text-align: center;
        color: white; /* Clock color changed to white */
      }
    </style>
    </head>
    <body>
    <div id="clock"></div>
    <script>
      function updateClock() {
        const now = new Date();
        const hours = now.getHours().toString().padStart(2, '0');
        const minutes = now.getMinutes().toString().padStart(2, '0');
        const seconds = now.getSeconds().toString().padStart(2, '0');
        const timeString = `${hours}:${minutes}:${seconds}`;
        document.getElementById('clock').textContent = timeString;
      }

      // Initial call to display clock immediately
      updateClock();

      // Update clock every second
      setInterval(updateClock, 1000);
    </script>
    </body>
    </html>
    """

    return html
