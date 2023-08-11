
def html_view(data):
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
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-size: 36px;
        }}
    </style>
    </head>
    <body>
    <div class="center">
        <h1>{data}</h1>
    </div>
    </body>
    </html>
    '''

    return html
