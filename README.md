# drive_api

<summary>Environment Install:</summary>
    
    pip install -r requirements.txt
    or
    python3 -m venv env;
    source env/bin/activate;
    pip install -r requirements.txt;
    
</details>

<summary>FileNotFoundError: [Errno 2] No such file or directory: 'credentials.json'</summary>
    
    1. https://console.cloud.google.com/welcome
    2. search "apis & services"
    3. license
    4. OAuth 2.0 client ID
    5. download json
    4. rename "credentials.json"
    
</details>

<summary>Upload upload_temp.txt to cloud:</summary>
    
    python uploader.py
    
</details>

<summary>Upload upload_temp.txt to cloud:</summary>

    raise exceptions.RefreshError(
    google.auth.exceptions.RefreshError: ('invalid_grant: Token has been expired or revoked.', {'error': 'invalid_grant', 'error_description': 'Token has been expired or revoked.'})

</details>
remove token.json and reauthorize on Chrome
