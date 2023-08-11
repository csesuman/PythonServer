
def html_view(data):
    html = f"""
    <html>
    <head>
    <style>
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
    """

    return html
