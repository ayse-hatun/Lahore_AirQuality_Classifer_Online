import joblib
from flask import Flask, render_template, request
app = Flask(__name__)
model = joblib.load('air_quality_model.pkl')
from flask import send_from_directory

@app.route('/hero_bg.png')
def hero_bg():
    return send_from_directory('templates', 'hero_bg.png')
@app.route('/')
def home():
  return render_template('index.html')
@app.route ("/predict",methods = ["POST"])
def predict():  
  pm10 = float(request.form['pm10'])
  pm2_5 = float(request.form['pm2_5'])
  carbon_monoxide = float(request.form['carbon_monoxide'])
  nitrogen_dioxide = float(request.form['nitrogen_dioxide'])
  sulphur_dioxide = float(request.form['sulphur_dioxide'])
  ozone = float(request.form['ozone'])
  aerosol_optical_depth = float(request.form['aerosol_optical_depth'])
  dust = float(request.form['dust'])
  uv_index = float(request.form['uv_index'])


  features = [[pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone,aerosol_optical_depth,dust,uv_index]]
  prediction = model.predict(features)
  if prediction[0]=="good":
    result = "Good Air Quality"
  else:
    result = "Poor Air Quality"

  return render_template('index.html',result=result)


if __name__ == "__main__":
  app.run(debug=True)