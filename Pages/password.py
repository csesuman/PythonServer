def password_generate_view():
    dropdown_options = ''.join([f'<option value="{i}">{i}</option>' for i in range(1, 513)])

    html = f"""
    <!DOCTYPE html>
    <html>  
    <head>
        <title>Strong Password Generator</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: black;
            }}

            .container {{
                text-align: center;
                padding: 20px;
                border-radius: 8px;
                background-color: white;
                box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
            }}

            #parameterInput {{
                padding: 8px;
                width: 200px;
                margin-right: 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }}

            #fetchButton {{
                padding: 8px 16px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }}

            #copyButton {{
                padding: 8px 16px;
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                display: none;
                margin-top: 10px;
            }}

            #result {{
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>



    <div class="container">
        <h1>Strong Password Generator</h1>
        <select id="parameterInput">
            {dropdown_options}
        </select>
        <button id="fetchButton">Fetch Value</button>
        <div id="result"></div>
        <button id="copyButton" style="display: none;">Copy Password</button>
        <p id="copyMessage" style="display: none;">Copied!</p>
    </div>

    <script>
        document.getElementById("fetchButton").addEventListener("click", fetchData);

        function fetchData() {{
            var parameterValue = document.getElementById("parameterInput").value;
            if (!parameterValue) {{
                alert("Please enter a parameter value");
                return;
            }}

            var encodedParameterValue = encodeURIComponent(parameterValue);
            var url = "http://127.0.0.1:5000/generate_password?length=" + encodedParameterValue;

            fetch(url)
                .then(response => response.json())
                .then(data => {{
                    var password = data.password; // Assuming the response has a property named "password"
                    document.getElementById("result").innerText  = "Fetched Password: " + password;
                    document.getElementById("copyButton").style.display = "block";
                }})
                .catch(error => {{
                    console.error("Error fetching data:", error);
                    document.getElementById("result").innerHTML = "Error fetching data";
                }});

            document.getElementById("copyButton").style.display = "block";
        }}

        document.getElementById("copyButton").addEventListener("click", copyPassword);

        function copyPassword() {{
            var passwordElement = document.getElementById("result");
            var password = passwordElement.textContent; // Get the password HTML

            var dummyTextArea = document.createElement("textarea");
            dummyTextArea.innerHTML = password;
            document.body.appendChild(dummyTextArea);
            dummyTextArea.select();
            document.execCommand("copy");
            document.body.removeChild(dummyTextArea);

            var copyMessage = document.getElementById("copyMessage");
            copyMessage.style.display = "block";
            setTimeout(function() {{
                copyMessage.style.display = "none";
            }}, 2000); // Display the message for 2 seconds
        }}

        document.getElementById("fetchButton").addEventListener("click", fetchData);
        document.getElementById("copyButton").addEventListener("click", copyPassword);

    </script>

    </body>
    </html>
    """

    return html
