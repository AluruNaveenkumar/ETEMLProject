from flask import Flask,render_template,request
from src.pipeline.predict_pipeline import CustomData,predictPipeline


app=Flask(__name__)

@app.route('/')
def indexpage():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            reading_score=request.form.get('reading_score'),
            writing_score=request.form.get('writing_score'),
            test_preparation_course=request.form.get('test_preparation_course')
            )
        df=data.get_data_as_data_frame()
        pred=predictPipeline()
        results=pred.predict(df)
        return render_template('home.html',results=results)

if __name__=='__main__':
    app.run(host='127.0.0.1',debug=True)