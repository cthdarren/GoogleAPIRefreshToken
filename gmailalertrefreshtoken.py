import requests, json

redir = "urn:ietf:wg:oauth:2.0:oob"

#####################################################
#
# Change this to your own desired scope
scope = "https://www.googleapis.com/auth/gmail.readonly"
#
#####################################################



client_id = input("Client ID: ")
client_secret = input("Client Secret: ")

print("\n##################################################\n\nhttps://accounts.google.com/o/oauth2/v2/auth?scope=" scope + "&response_type=code&state=security_token%3D138r5719ru3e1%26url%3Dhttps%3A%2F%2Foauth2.example.com%2Ftoken&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&client_id="+ client_id)

code = input("\n##################################################\nPlease visit the link above in your browser\nPaste the given code here:")

res = requests.post("https://oauth2.googleapis.com/token", data={"client_id": client_id, "client_secret": client_secret,"redirect_uri":redir, "grant_type":"authorization_code", "code":code})

jsonOutput = json.loads(res.text)

print("Your refresh token is: " + jsonOutput["refresh_token"])
