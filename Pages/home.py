
def home_view():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Clickable Links from JSON</title>
        <style>
            body {{
                background-color: black;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
            }}
    
            .link-container {{
                margin: 20px;
                text-align: center;
            }}
    
            .link {{
                color: white;
                text-decoration: underline;
                margin: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="link-container" id="linkContainer1">
            <p class="message"></p>
            <a class="link" href="#" target="_blank"></a>
        </div>
    
        <div class="link-container" id="linkContainer2">
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
        
            <div class="link-container" id="linkContainer8">
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
            
            var jsonResponse2 = {{
                "message": "IP information",
                "link": "/ipinformation"
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
                "message": "Webhook echo Server",
                "link": "/webhook"
            }};
            
            var jsonResponse6 = {{
                "message": "Reload Counter",
                "link": "/reload"
            }};
            
            var jsonResponse7 = {{
                "message": "index",
                "link": "/index"
            }};
            
            var jsonResponse8 = {{
                "message": "Save Requests",
                "link": "/save"
            }};
            
            var jsonResponse9 = {{
                "message": "Call API by Type",
                "link": "/make_request"
            }};
    
            // Function to update link container
            function updateLinkContainer(containerId, jsonResponse) {{
                var container = document.getElementById(containerId);
                var messageElement = container.querySelector(".message");
                var linkElement = container.querySelector(".link");
    
                messageElement.textContent = jsonResponse.message;
                linkElement.href = jsonResponse.link;
                linkElement.textContent = jsonResponse.message;
            }}
    
            // Update both link containers
            updateLinkContainer("linkContainer1", jsonResponse1);
            updateLinkContainer("linkContainer2", jsonResponse2);
            updateLinkContainer("linkContainer3", jsonResponse3);
            updateLinkContainer("linkContainer4", jsonResponse4);
            updateLinkContainer("linkContainer5", jsonResponse5);
            updateLinkContainer("linkContainer6", jsonResponse6);
            updateLinkContainer("linkContainer7", jsonResponse7);
            updateLinkContainer("linkContainer8", jsonResponse8);
            updateLinkContainer("linkContainer9", jsonResponse9);
        </script>
    </body>
    </html>
    """

    return html
