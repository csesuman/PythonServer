def html_view(ip, city, region, country):
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{
            background-color: black;
            margin: 0;
            padding: 0;
            color: white;
            font-family: Arial, sans-serif;
        }}

        .center {{
            display: flex;
            flex-direction: column; /* Change to column layout */
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-size: 36px;
        }}

        .data {{
            margin: 10px; /* Add margin between data sections */
        }}
    </style>
    </head>
    <body>
    <div class="center">
        <h1 class="data">Public IP</h1>
        <h1 class="data">{ip}</h1>
        <h2 class="data"></h1>
        <h2 class="data"></h1>
        <h2 class="data">Location</h1>
        <h3 class="data">{city}, {region}</h1> <!-- Display the data twice -->
        <h3 class="data">{country}</h1> <!-- Display the data twice -->
    </div>
    </body>
    </html>
    '''

    return html
