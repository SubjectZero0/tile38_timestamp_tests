from flask import Flask,request,abort

app=Flask(__name__)

@app.route('/hook',methods=['POST'])
def webhook():
    #create a webhook
    if request.method=='POST':

        print("Webhook Triggered!") #message

        # Create a .txt with the request json
        with open("request.txt", "w") as f:
            f.write('{\n')
            for key in request.json:
                f.write(f"  '{key}' : {request.json[key]},\n")
                
            f.write("}\n")

        return "request.txt"
    else:
        
        return abort(400)
    
        
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)