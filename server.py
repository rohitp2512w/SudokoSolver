from flask import Flask,request
import numpy as np
import os
import pprint
from flask_cors import CORS, cross_origin
from flask import jsonify
from collections import defaultdict
import math
import random
import algorithm.sudoko_solver_fn as solver

app= Flask(__name__)
CORS(app)

def dataprep(inpData):
    outData= [[0 for i in range(len(inpData))] for j in range(len(inpData))]
    for row in range(len(inpData)):
        for col in range(len(inpData)):
            if(inpData[row][col]!=''):
                outData[row][col]=int(inpData[row][col])
    return(outData)



@app.route('/solution',methods = ['POST'])
@cross_origin()
def returnSolution():
    inputData= request.json['data']
    processedData=dataprep(inputData)
    solution=solver.getSolution(processedData)
    pprint.pprint(solution)
    return(jsonify([solution]))

if __name__== '__main__':
    app.run(debug=True)