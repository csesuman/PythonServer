

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
</style>
</head>
<body>
<div class="clock-container">
  <div class="clock" id="clock1"></div>
  <div class="clock" id="clock2"></div>
</div>
<script>
  function updateClock(clockId) {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');
    const timeString = `${hours}:${minutes}:${seconds}`;
    document.getElementById(clockId).textContent = timeString;
  }

  // Initial call to display clocks immediately
  updateClock('clock1');
  updateClock('clock2');

  // Update clocks every second
  setInterval(function() {
    updateClock('clock1');
    updateClock('clock2');
  }, 1000);
</script>
</body>
</html>

    """

    return html
