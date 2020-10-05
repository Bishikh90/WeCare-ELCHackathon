from flask import Flask, url_for, render_template,request,redirect,send_file
from markupsafe import escape
import source,os

app = Flask(__name__)

@app.route('/',methods = ["GET","POST"])
def index():
   return render_template('index.html')
@app.route('/convertaudio',methods=["GET","POST"])
def convertaudio():
     trans=""
     if request.method == "POST":
         print("FORM DATA RECEIVED")


         file = request.files["audio_data"]
         if file:
            s=source.support()
            #Conversion1
            
            #speach_record( path)
            #path = "Patient1.wav"
            lang='hi'
            fnl_Txt= s.audio_transcription(file,lang)
            print(fnl_Txt)
            lang='en'
            conversion_to_Lang2=s.Speach_conversion(fnl_Txt, lang)
            print(conversion_to_Lang2)
            trans=conversion_to_Lang2
            lang_to='en-IN'
            s.Text_to_speach(conversion_to_Lang2,lang_to)

         else:
            print("sorry")
     #file = "captured_voice.mp3"
     
     
     return  send_file("static/captured_voice.mp3"
     )

# POST router(recorded audio)
    # return {coverted audio, converted text}


   
    



if __name__ == "__main__":
    app.run(debug=True, threaded=True)