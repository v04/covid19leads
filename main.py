
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib
import pickle
import sklearn as sk
from datetime import datetime
from datetime import date

app = Flask(__name__)

df = pd.DataFrame()
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    global df
    
    input_features = [ str(x) for x in request.form.values()]

    nm = input_features[0]
    ag = input_features[1]
    gen = input_features[2]
    stp="";
    stp2="";
    stp3="";

    print(input_features)

    input_features = input_features[3:23]
    

    
    features_value = np.array(input_features)
    features_value = features_value.astype(int)
    output = model.predict([features_value])
    print(str(output[0])," Output - ",output)
    print(features_value)
    msg2 = str(output[0])+""
    today = date.today()
    now = datetime.now()
    dt = str(today.strftime("%B %d, %Y"))
    tm2 = datetime.now()
    tm = str(now.strftime("%H:%M"))
    repo = ""
    #print("Output = ",output)

    stats = ((output[0]*100).round(2))
    
    print ("% Probab - ",stats)
    output2 = output[0]*100
    if(int(output2<30)):
      msg2 = "Negative"
      repo = str(stats)+"% Positive"
      stp = "No need to panic, take precautions and follow all safety norms."
      stp2="Always be in touch with a Physician."
      stp3 = "Take steps to boost your immunity."

    elif((int(output2>=30))and(int(output2<45))):
      msg2 = "Might be Negative"
      repo = str(stats)+"% Positive"
      stp="Get yourself be tested incase of appearance of any symptom even mild."
      stp2 = "Get in touch with doctors."
      stp3 = "Isolate yourself if possible."
     
    elif((int(output2>=45))and(int(output2<60))):
      msg2 = "Slightly Positive"
      repo = str(stats)+"% Positive"
      stp="Contact the Physician at the earliest."
      stp2 = "Get yourself tested"
      stp3 = "Take steps to boost immunity"

    elif((int(output2>=60))and(int(output2<75))):
      msg2 = "Positive"
      repo = str(stats)+"% Positive"
      stp = "Immediately get your RT-PCR test."
      stp2 = "Consult a doctor immeditely"
      stp3 = "Don't Panic and be calm"
    else:
      msg2 = "Critically Positive"
      repo = str(stats)+"% Positive"
      stp = "Immediately get your RT-PCR test."
      stp2 = "Consult a doctor immeditely"
      stp3 = "You might need hospitalization"

    

      

    
    return render_template('index.html', prediction_text=msg2,name=nm.upper(),age=ag,gender=gen.upper(),date33=dt,time33=tm,report=repo,naame=nm,agge=ag,gender2=gen,steps1=stp,steps2=stp2,steps3=stp3,c1=  str(input_features[0]),
      c2=  str(input_features[1]),
      c3=  str(input_features[2]),
      c4=  str(input_features[3]),
      c5=  str(input_features[4]),
      c6=  str(input_features[5]),
      c7=  str(input_features[6]),
      c8=  str(input_features[7]),
      c9=  str(input_features[8]),
      c10=  str(input_features[9]),
      c11=  str(input_features[10]),
      c12=  str(input_features[11]),
      c13=  str(input_features[12]),
      c14=  str(input_features[13]),
      c15=  str(input_features[14]),
      c16=  str(input_features[15]),
      c17=  str(input_features[16]),
      c18=  str(input_features[17]),
      c19=  str(input_features[18]),
      c20=  str(input_features[19]))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
