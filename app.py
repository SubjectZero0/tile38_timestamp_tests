from flask import Flask,request

app=Flask(__name__)

@app.route('/hook',methods=['POST'])
def webhook():
    #create a webhook
    if request.method=='POST':
        print("Webhook Triggered!") #message
        # Create a .txt with the request json
        with open("request.txt", "w") as f:
            f.write(f"{request.json}")
        return "request.txt"
    return "OK"
        
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)