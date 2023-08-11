
def reload_view(hit):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="refresh" content="5">
    </head>
    <body>
        <h1>Auto-Refreshing Page</h1>
        <p>This page will automatically reload every 5 seconds.</p>
        <p>total hit: {hit}</p>
    </body>
    </html>
    """

    return html