import pandas as pd
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

from sklearn import model_selection
from sklearn.preprocessing import MinMaxScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB

import random
import math
import numpy as np
from sklearn import metrics

def SVCParameters(numberFeatures,icls):
    genome = list()
    #kernel
    listKernel = ["linear","rbf", "poly","sigmoid"]
    genome.append(listKernel[random.randint(0, 3)])
    #c
    k = random.uniform(0.1, 100)
    genome.append(k)
    #degree
    genome.append(random.uniform(0.1,5))
    #gamma
    gamma = random.uniform(0.001,5)
    genome.append(gamma)
    # coeff
    coeff = random.uniform(0.01, 10)
    genome.append(coeff)
    for i in range(0,numberFeatures):
        genome.append(random.randint(0, 1))
    return icls(genome)

def SVCParametersFitness(y,df,numberOfAtributtes,individual):
    split=5
    cv = model_selection.StratifiedKFold(n_splits=split)
    listColumnsToDrop = []
    # lista cech do usuniecia
    for i in range(numberOfAtributtes,len(individual)):
        if individual[i]==0:
            #gdy atrybut ma zero to usuwamy cechę
            listColumnsToDrop.append(i-numberOfAtributtes)
    dfSelectedFeatures=df.drop(df.columns[listColumnsToDrop], axis=1, inplace=False)

    mms = MinMaxScaler()
    df_norm = mms.fit_transform(dfSelectedFeatures)
    estimator = SVC(kernel=individual[0],C=individual[1],degree=individual[2],gamma=individual[3],coef0=individual[4],random_state=101)
    resultSum = 0
    for train, test in cv.split(df_norm, y):
        estimator.fit(df_norm[train], y[train])
        predicted = estimator.predict(df_norm[test])
        expected = y[test]
        matrix = metrics.confusion_matrix(expected, predicted)
        result = np.trace(matrix) / np.sum(
            matrix)  # w oparciu o macierze pomyłek https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/
        resultSum = resultSum + result  # zbieramy wyniki z poszczególnych etapów walidacji krzyżowej
    return resultSum / split,

def mutationSVC(individual):
    numberParamer= random.randint(0,len(individual)-1)
    if numberParamer==0:
        # kernel
        listKernel = ["linear", "rbf", "poly", "sigmoid"]
        individual[0]=listKernel[random.randint(0, 3)]
    elif numberParamer==1:
        #C
        k = random.uniform(0.1,100)
        individual[1]=k
    elif numberParamer == 2:
        #degree
        individual[2]=random.uniform(0.1, 5)
    elif numberParamer == 3:
        #gamma
        gamma = random.uniform(0.01, 5)
        individual[3]=gamma
    elif numberParamer ==4:
        # coeff
        coeff = random.uniform(0.1, 20)
        individual[2] = coeff
    else:  # genetyczna selekcja cech
        if individual[numberParamer] == 0:
            individual[numberParamer] = 1
        else:
            individual[numberParamer] = 0


def DecisionTreeParameters(numberFeatures, icls):
    genome = list()
    #criterion
    listCriterion = ["gini","entropy"]
    genome.append(listCriterion[random.randint(0, 1)])
    #max_depth
    max_depth = random.randint(1, 10)
    genome.append(max_depth)
    #min_samples_split
    min_samples_split = random.uniform(0.01,1)
    genome.append(min_samples_split)
    for i in range(0,numberFeatures):
        genome.append(random.randint(0, 1))
    return icls(genome)

def DecisionTreeParametersFitness(y,df,numberOfAtributtes,individual):
    split=5
    cv = model_selection.StratifiedKFold(n_splits=split)
    listColumnsToDrop = []
    # lista cech do usuniecia
    for i in range(numberOfAtributtes,len(individual)):
        if individual[i]==0:
            #gdy atrybut ma zero to usuwamy cechę
            listColumnsToDrop.append(i-numberOfAtributtes)
    dfSelectedFeatures=df.drop(df.columns[listColumnsToDrop], axis=1, inplace=False)

    mms = MinMaxScaler()
    df_norm = mms.fit_transform(dfSelectedFeatures)
    estimator = DecisionTreeClassifier(criterion=individual[0], max_depth=individual[1], min_samples_split=individual[2])
    resultSum = 0
    for train, test in cv.split(df_norm, y):
        estimator.fit(df_norm[train], y[train])
        predicted = estimator.predict(df_norm[test])
        expected = y[test]
        matrix = metrics.confusion_matrix(expected, predicted)
        result = np.trace(matrix) / np.sum(
            matrix)  # w oparciu o macierze pomyłek https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/
        resultSum = resultSum + result  # zbieramy wyniki z poszczególnych etapów walidacji krzyżowej
    return resultSum / split,

def mutationDecisionTree(individual):
    numberParamer= random.randint(0,len(individual)-1)
    if numberParamer==0:
        # crit
        crit = ["gini", "entropy"]
        individual[0]=crit[random.randint(0, 1)]
    elif numberParamer==1:
        #max_depth
        max_depth = random.randint(1, 10)
        individual[1]=max_depth
    elif numberParamer == 2:
        #min_samples_split
        individual[2]= random.uniform(0.001,1)
    else:  # genetyczna selekcja cech
        if individual[numberParamer] == 0:
            individual[numberParamer] = 1
        else:
            individual[numberParamer] = 0

def KNeighborsParameters(numberFeatures, icls):
    genome = list()
    #n_neighbors
    genome.append(random.randint(1, 10))
    #weights
    weights = ['uniform', 'distance']
    genome.append(weights[random.randint(0, 1)])
    #algorithm
    algorithm = ['auto', 'ball_tree', 'kd_tree', 'brute']
    genome.append(algorithm[random.randint(0, 3)])
    for i in range(0,numberFeatures):
        genome.append(random.randint(0, 1))
    return icls(genome)

def KNeighborsParametersFitness(y,df,numberOfAtributtes,individual):
    split=5
    cv = model_selection.StratifiedKFold(n_splits=split)
    listColumnsToDrop = []
    # lista cech do usuniecia
    for i in range(numberOfAtributtes,len(individual)):
        if individual[i]==0:
            #gdy atrybut ma zero to usuwamy cechę
            listColumnsToDrop.append(i-numberOfAtributtes)
    dfSelectedFeatures=df.drop(df.columns[listColumnsToDrop], axis=1, inplace=False)

    mms = MinMaxScaler()
    df_norm = mms.fit_transform(dfSelectedFeatures)
    estimator = KNeighborsClassifier(n_neighbors=individual[0], weights=individual[1], algorithm=individual[2])
    resultSum = 0
    for train, test in cv.split(df_norm, y):
        estimator.fit(df_norm[train], y[train])
        predicted = estimator.predict(df_norm[test])
        expected = y[test]
        matrix = metrics.confusion_matrix(expected, predicted)
        result = np.trace(matrix) / np.sum(
            matrix)  # w oparciu o macierze pomyłek https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/
        resultSum = resultSum + result  # zbieramy wyniki z poszczególnych etapów walidacji krzyżowej
    return resultSum / split,

def mutationKNeighbors(individual):
    numberParamer= random.randint(0,len(individual)-1)
    if numberParamer==0:
        # nneig
        individual[0] = random.randint(1, 10)
    elif numberParamer==1:
        # weights
        weights = ['uniform', 'distance']
        individual[1] = weights[random.randint(0, 1)]
    elif numberParamer==2:
        # algorithm
        algorithm = ['auto', 'ball_tree', 'kd_tree', 'brute']
        individual[2] = algorithm[random.randint(0, 3)]
    else:  # genetyczna selekcja cech
        if individual[numberParamer] == 0:
            individual[numberParamer] = 1
        else:
            individual[numberParamer] = 0

def MLPParameters(numberFeatures, icls):
    genome = list()
    #hidden_layer_sizes
    genome.append((random.randint(50, 200),))
    #activation
    weights = ['identity', 'logistic', 'tanh', 'relu']
    genome.append(weights[random.randint(0, 3)])
    #solver
    algorithm = ['lbfgs', 'sgd', 'adam']
    genome.append(algorithm[random.randint(0, 2)])
    #learning_rate
    algorithm = ['constant', 'invscaling', 'adaptive']
    genome.append(algorithm[random.randint(0, 2)])
    for i in range(0,numberFeatures):
        genome.append(random.randint(0, 1))
    return icls(genome)

def MLPParametersFitness(y,df,numberOfAtributtes,individual):
    split=5
    cv = model_selection.StratifiedKFold(n_splits=split)
    listColumnsToDrop = []
    # lista cech do usuniecia
    for i in range(numberOfAtributtes,len(individual)):
        if individual[i]==0:
            #gdy atrybut ma zero to usuwamy cechę
            listColumnsToDrop.append(i-numberOfAtributtes)
    dfSelectedFeatures=df.drop(df.columns[listColumnsToDrop], axis=1, inplace=False)

    mms = MinMaxScaler()
    df_norm = mms.fit_transform(dfSelectedFeatures)
    estimator = MLPClassifier(hidden_layer_sizes=individual[0], activation=individual[1], solver=individual[2], learning_rate=individual[3])
    resultSum = 0
    for train, test in cv.split(df_norm, y):
        estimator.fit(df_norm[train], y[train])
        predicted = estimator.predict(df_norm[test])
        expected = y[test]
        matrix = metrics.confusion_matrix(expected, predicted)
        result = np.trace(matrix) / np.sum(matrix)  # w oparciu o macierze pomyłek https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/
        resultSum = resultSum + result #zbieramy wyniki z poszczególnych etapów walidacji krzyżowej
    return resultSum / split,

def mutationMLP(individual):
    numberParamer= random.randint(0,len(individual)-1)
    if numberParamer==0:
        #hidden_layer_sizes
        individual[0] = (random.randint(80, 120),)
    elif numberParamer==1:
        # activation
        weights = ['identity', 'logistic', 'tanh', 'relu']
        individual[1] = weights[random.randint(0, 3)]
    elif numberParamer==2:
        # solver
        algorithm = ['lbfgs', 'sgd', 'adam']
        individual[2] = algorithm[random.randint(0, 2)]
    elif numberParamer==3:
        # learning_rate
        algorithm = ['constant', 'invscaling', 'adaptive']
        individual[3] = algorithm[random.randint(0, 2)]
    else:  # genetyczna selekcja cech
        if individual[numberParamer] == 0:
            individual[numberParamer] = 1
        else:
            individual[numberParamer] = 0

def NBParameters(numberFeatures, icls):
    genome = list()
    #var_smoothing
    genome.append(random.uniform(1e-10, 1e-8))
    for i in range(0,numberFeatures):
        genome.append(random.randint(0, 1))
    return icls(genome)

def NBParametersFitness(y,df,numberOfAtributtes,individual):
    split=5
    cv = model_selection.StratifiedKFold(n_splits=split)
    listColumnsToDrop = []
    # lista cech do usuniecia
    for i in range(numberOfAtributtes,len(individual)):
        if individual[i]==0:
            #gdy atrybut ma zero to usuwamy cechę
            listColumnsToDrop.append(i-numberOfAtributtes)
    dfSelectedFeatures=df.drop(df.columns[listColumnsToDrop], axis=1, inplace=False)

    mms = MinMaxScaler()
    df_norm = mms.fit_transform(dfSelectedFeatures)
    estimator = GaussianNB(var_smoothing=individual[0])
    resultSum = 0
    for train, test in cv.split(df_norm, y):
        estimator.fit(df_norm[train], y[train])
        predicted = estimator.predict(df_norm[test])
        expected = y[test]
        matrix = metrics.confusion_matrix(expected, predicted)
        result = np.trace(matrix) / np.sum(matrix)  # w oparciu o macierze pomyłek https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/
        resultSum = resultSum + result #zbieramy wyniki z poszczególnych etapów walidacji krzyżowej
    return resultSum / split,

def mutationNB(individual):
    numberParamer= random.randint(0,len(individual)-1)
    if numberParamer==0:
        #var_smoothing
        individual[0] = random.uniform(1e-10, 1e-8)
    else:  # genetyczna selekcja cech
        if individual[numberParamer] == 0:
            individual[numberParamer] = 1
        else:
            individual[numberParamer] = 0