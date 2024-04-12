
def home_view():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Suman Tech</title>
        <style>
        body {{
                background-color: black;
                display: flex;
                flex-direction: column;
                align-items: center; /* Center horizontally */
                justify-content: center; /* Center vertically */
                height: 100vh; /* Change 0vh to 100vh to fill the viewport */
                margin: 0; /* Adjusted to remove extra margin */
                font-family: Arial, sans-serif;
            }}

            .link-container {{
                background-color: transparent;
                margin: 10px;
                text-align: center;
            }}
    
            .link {{
                color: white;
                text-decoration: underline;
                margin: 5px;
            }}
        </style>
    </head>
    <body>
        <div class="link-container" id="linkContainer1">
            <p class="message"></p>
            <a class="link" href="#" target="_blank"></a>
        </div>
        <div class="link-container" id="linkContainer3">
            <p class="message"></p>
            <a class="link" href="#" target="_blank"></a>
        </div>
        <div class="link-container" id="linkContainer4">
            <p class="message"></p>
            <a class="link" href="#" target="_blank"></a>
        </div>
        <div class="link-container" id="linkContainer5">
            <p class="message"></p>
            <a class="link" href="#" target="_blank"></a>
        </div>
        <div class="link-container" id="linkContainer6">
            <p class="message"></p>
            <a class="link" href="#" target="_blank"></a>
        </div>
                <div class="link-container" id="linkContainer7">
            <p class="message"></p>
            <a class="link" href="#" target="_blank"></a>
        </div>

        <div class="link-container" id="linkContainer9">
            <p class="message"></p>
            <a class="link" href="#" target="_blank"></a>
        </div>
    
        <script>
            // Simulating JSON responses (replace these with actual data from your server)
            var jsonResponse1 = {{
                "message": "My Public IP",
                "link": "/myip"
            }};
            var jsonResponse3 = {{
                "message": "Random Password Generator",
                "link": "/new_password"
            }};
            
            var jsonResponse4 = {{
                "message": "Digital Clock",
                "link": "/clock"
            }};
            
            var jsonResponse5 = {{
                "message": "Echo Server",
                "link": "/echo"
            }};

            var jsonResponse6 = {{
                "message": ">>>> Webhook Server <<<<<",
                "link": "/webhook-received"
            }};
            
            var jsonResponse7 = {{
                "message": "Give Me Advice",
                "link": "/index"
            }};

            var jsonResponse9 = {{
                "message": "Call API by Type",
                "link": "/make_request"
            }};
    
            // Function to update link container
            function updateLinkContainer(containerId, jsonResponse) {{
                var container = document.getElementById(containerId);
                var linkElement = container.querySelector(".link");
                linkElement.href = jsonResponse.link;
                linkElement.textContent = jsonResponse.message;
            }}
    
            // Update both link containers
            updateLinkContainer("linkContainer1", jsonResponse1);
            updateLinkContainer("linkContainer3", jsonResponse3);
            updateLinkContainer("linkContainer4", jsonResponse4);
            updateLinkContainer("linkContainer5", jsonResponse5);
            updateLinkContainer("linkContainer6", jsonResponse6);
            updateLinkContainer("linkContainer7", jsonResponse7);
            updateLinkContainer("linkContainer9", jsonResponse9);
        </script>
    </body>
    </html>
    """

    return html
