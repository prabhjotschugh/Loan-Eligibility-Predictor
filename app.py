from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':
        gender = (request.form['gender'])
        married = request.form['married']
        dependents = (request.form['dependents'])
        education = (request.form['education'])
        employed = (request.form['employed'])
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        credit = float(request.form['credit'])
        area = (request.form['area'])  
            
        totalincomelog = np.log(ApplicantIncome+CoapplicantIncome)
        LoanAmountlog = np.log(LoanAmount)
        Loan_Amount_Termlog = np.log(Loan_Amount_Term)
        
        prediction = model.predict([[gender, dependents, education, employed, totalincomelog, LoanAmountlog, Loan_Amount_Termlog, area]])

        # print(prediction)
        if(prediction==0):
            prediction="REJECTED"
        else:
            prediction="ACCEPTED"

        return render_template("predict.html", prediction_text="Your Loan is {}".format(prediction))
    else:
        return render_template("predict.html")

if __name__ == "__main__":
    app.run(debug=True)