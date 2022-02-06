import pandas as pd
import numpy 
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import load_model
import streamlit as st
import altair as alt


@st.cache(allow_output_mutation=True)
def predict(file_path,split_percent,predict_model):

    numpy.random.seed(7)
   
    def create_dataset(dataset, look_back):
	    dataX, dataY = [], []
	    for i in range(len(dataset)-look_back-1):
		    a = dataset[i:(i+look_back), 0]
		    dataX.append(a)
		    dataY.append(dataset[i + look_back, 0])
	    return numpy.array(dataX), numpy.array(dataY)
 
    # fix random seed for reproducibility
    # load the dataset

    dataframe = read_csv(file_path, usecols=[1], engine='python')
    dataset = dataframe.values
    dataset = dataset.astype('float32')

    # normalize the dataset
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset = scaler.fit_transform(dataset)

    # split into train and test sets
    train_size = int(len(dataset) * split_percent)
    train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
    look_back = 3

    # reshape into X=t and Y=t+1

    trainX, trainY = create_dataset(train, look_back)
    testX, testY = create_dataset(test, look_back)

    # reshape input to be [samples, time steps, features]
    trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

    # load mode
    
    model = load_model(predict_model)

    # make predictions
    trainpredict = model.predict(trainX)
    testPredict = model.predict(testX)

    # invert predictions
    trainpredict = scaler.inverse_transform(trainpredict)
    trainY = scaler.inverse_transform([trainY])
    testPredict = scaler.inverse_transform(testPredict)
    testY = scaler.inverse_transform([testY])

    # calculate root mean squared error
    trainScore = math.sqrt(mean_squared_error(trainY[0], trainpredict[:,0]))
    #print('Train Score: %.2f RootMSE' % (trainScore))
    testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
    #print('Test Score: %.2f RootMSE' % (testScore))

    # shift train predictions for plotting
    trainpredictPlot = numpy.empty_like(dataset)
    trainpredictPlot[:, :] = numpy.nan
    trainpredictPlot[look_back:len(trainpredict)+look_back, :] = trainpredict

    # shift test predictions for plotting
    testPredictPlot = numpy.empty_like(dataset)
    testPredictPlot[:, :] = numpy.nan
    testPredictPlot[len(trainpredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

    df1 = pd.read_csv(file_path)
    df1['__timestamp'] = pd.to_datetime(df1['__timestamp'], format='%Y/%m/%d')

     
    t = scaler.inverse_transform(dataset)
    p = testPredictPlot
    data = [x for i in t for x in i]
    predicted =  [x for i in p for x in i]
 
    if 'wallet' in predict_model:
        titY = 'Wallet Count →'
    else:
        titY = 'Volume →'    

    dff = pd.DataFrame({'date':df1['__timestamp'].to_list(),'data':data},columns=['date','data'])    
    dff1 = pd.DataFrame({'date':df1['__timestamp'].to_list(),'data':predicted},columns=['date','data'])  



    base = alt.Chart(dff).transform_calculate(
        Actual="'Actual'",
    )
    base1 = alt.Chart(dff1).transform_calculate(
        Predicted="'Predicted'",   
    )

    scale = alt.Scale(domain=["Actual","Predicted"], range=['Yellowgreen','Red'])
    
    basic_chart = base.mark_line(color="Yellowgreen").encode(
    x=alt.X('date:T', axis=alt.Axis(titleFontSize=12, title='Time →', labelColor='#999999', titleColor='#AF7AC5', titleAlign='right', titleAnchor='end', titleY=45,labelAngle = -45, labelOverlap = False)),
    y=alt.Y('data:Q', axis=alt.Axis(format="$s", tickCount=3, titleFontSize=12, title=titY, labelColor='#999999', titleColor='#3498DB', titleAnchor='end')),
    color=alt.Color('Actual:N', scale=scale, title='')
    ).properties(    
    width=1280,
    height=500).interactive()

    basic_chart1 = base1.mark_line(color="Red").encode(
    x=alt.X('date:T', axis=alt.Axis( titleFontSize=12, title='Time →', labelColor='#999999', titleColor='#AF7AC5', titleAlign='right', titleAnchor='end', titleY=45,labelAngle = -45, labelOverlap = False)),
    y=alt.Y('data:Q', axis=alt.Axis(format="$s", tickCount=3, titleFontSize=12, title=titY, labelColor='#999999', titleColor='#3498DB', titleAnchor='end')),
    color=alt.Color('Predicted:N', scale=scale, title='')
    ).properties(
    width=1280,
    height=500).interactive()


    return alt.layer(basic_chart, basic_chart1)

