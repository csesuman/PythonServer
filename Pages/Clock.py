

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
          background-color: black;
        }
    
        .clock-container {
          display: flex;
          flex-direction: column; /* Display clocks vertically */
          align-items: center;
        }
    
        .clock {
          font-size: 10vw;
          font-weight: bold;
          text-align: center;
          color: white;
          margin: 10px; /* Added margin for spacing between clocks */
        }
        
        .dropdown {
          margin-top: 20px;
        }
      </style>
    </head>
    <body>
      <div class="clock-container">
        <div class="clock" id="clock1"></div>
        <div class="clock" id="clock2"></div>
        <div class="dropdown">
          <label for="countrySelect">Select a Country:</label>
          <select id="countrySelect" onchange="updateClock('clock2', this.value);">
            <option value="auto" selected>Auto (Local Time)</option>
            <option value="America/New_York">New York</option>
            <option value="Europe/London">London</option>
            <option value="Asia/Tokyo">Tokyo</option>
            <option value="Asia/Dhaka">Dhaka</option>
            <option value="Asia/Singapore">Singapore</option>
            <option value="Asia/Kolkata">Kolkata</option>
            <option value="Asia/Dubai">Dubai</option>
            <option value="Europe/London">London</option>
            <option value="America/Toronto">Toronto</option>
            <option value="Europe/Moscow">Moscow</option>
          </select>
        </div>
      </div>
      <script>
        
      
      
      
      
        function updateClock(clockId, timeZone) {
          const now = timeZone === 'auto' ? new Date() : new Date(new Date().toLocaleString('en-US', { timeZone }));
          const hours = now.getHours().toString().padStart(2, '0');
          const minutes = now.getMinutes().toString().padStart(2, '0');
          const seconds = now.getSeconds().toString().padStart(2, '0');
          const timeString = `${hours}:${minutes}:${seconds}`;
          document.getElementById(clockId).textContent = timeString;
        }
    
        // Initial call to display clocks immediately
        updateClock('clock1', 'auto');
        updateClock('clock2', 'auto');
    
        // Update second clock's time based on selected country
        document.getElementById('countrySelect').addEventListener('change', function() {
          updateClock('clock2', this.value);
        });
    
        // Update clocks every second
        setInterval(function() {
          updateClock('clock1', 'auto');
          updateClock('clock2', document.getElementById('countrySelect').value);
        }, 1000);
      </script>
    </body>
    </html>


    """

    return html
