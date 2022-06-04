import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob
import datetime

lfs_var_labels = {"rec_num" : "Order of record in file",
"survyear" : "Survey year",
"survmnth" : "Survey month",
"lfsstat" : "Labour force status",
"prov" : "Province",
"cma" : "Nine largest CMAs",
"age_12" : "Five-year age group of respondent",
"age_6" : "Age in 2 and 3 year groups, 15 to 29",
"sex" : "Sex of respondent",
"marstat" : "Marital status of respondent",
"educ" : "Highest educational attainment",
"mjh" : "Single or multiple jobholder",
"everwork" : "Not currently employed, worked in the past",
"ftptlast" : "Full- or part-time status of last job",
"cowmain" : "Class of worker, main job",
"immig" : "Immigrant status",
"naics_21" : "Industry of main job",
"noc_10" : "Occupation at main job",
"noc_40" : "Occupation at main job",
"yabsent" : "Reason of absence, full week",
"wksaway" : "Number of weeks absent from work",
"payaway" : "Paid for time off, full-week absence only",
"uhrsmain" : "Usual hours worked per week at main job",
"ahrsmain" : "Actual hours worked per week at main job",
"ftptmain" : "Full- or part-time status at main or only job",
"utothrs" : "Usual hours worked per week at all jobs",
"atothrs" : "Actual hours worked per week at all jobs",
"hrsaway" : "Hours away from work, part-week absence only",
"yaway" : "Reason for part-week absence",
"paidot" : "Paid overtime hours in reference week",
"unpaidot" : "Unpaid overtime hours in reference week",
"xtrahrs" : "Number of overtime or extra hours worked",
"whypt" : "Reason for part-time work",
"tenure" : "Job tenure with current employer (months)",
"prevten" : "Job tenure with previous employer (months)",
"hrlyearn" : "Usual hourly wages, employees only",
"union" : "Union status, employees only",
"permtemp" : "Job permanency, employees only",
"estsize" : "Establishment size",
"firmsize" : "Firm size",
"durunemp" : "Duration of unemployment (weeks)",
"flowunem" : "Flows into unemployment",
"unemftpt" : "Unemployed, type of job wanted",
"whylefto" : "Reason for leaving job during previous year ",
"whyleftn" : "Reason for leaving job during previous year ",
"durjless" : "Duration of joblessness (months)",
"availabl" : "Availability during the reference week",
"lkpubag" : "Unemployed, used public employment agency",
"lkemploy" : "Unemployed, checked with employers directly",
"lkrels" : "Unemployed, checked with friends or relatives",
"lkatads" : "Unemployed, looked at job ads",
"lkansads" : "Unemployed, placed or answered ads",
"lkothern" : "Unemployed, other methods",
"prioract" : "Main activity before started looking for work",
"ynolook" : "Reason for not looking for work during the reference week",
"tlolook" : "Temporary layoff, looked for work during the last four weeks",
"schooln" : "Current student status",
"efamtype" : "Type of economic family",
"agyownk" : "Age of youngest child",
"finalwt" : "Standard final weight"
}

# Below is a function that takes the subset of the labour force data and replaces qualitatives columns with their string meaning from csv files. The CSV files should be named with lower case versions of the LFS variable names and stored as separate csv's in a folder called "Metadata"
def join_lfs_var_labels(df,path, replace_variables = True):
    '''This function replaces the numerical values for LFS variables with their labels as strings for any subset of the labour force survey data. '''

    columns = df.columns.to_list()
    print(columns)
    print(columns[0].lower())
    print(type(columns[0].lower()))
    print(path)
    
    for var in columns:
        #df[var] = df[var].astype(int)
        print(path + '/Metadata/{}.csv'.format(var.lower()))

        print('variable: ' + var.lower())

        pathexists = os.path.exists(path + '/Metadata/{}.csv'.format(var.lower()))
        #read in csv corresponding to the name of the lfs variable
        if pathexists == True:
            meaning = pd.read_csv(path + '/Metadata/{}.csv'.format(var.lower()), encoding = 'cp1252', dtype = np.object)

            #store the variable name for later use when using replace variable
            var_name = meaning.columns[0]
            print(meaning.columns)
        
            #join the dimension table to the LFS fact table
            df = pd.merge(df, meaning, left_on = var, right_on = 'id', how = 'left')
            df = df.drop(var, axis = 1)
            df = df.drop('id', axis = 1)
            
            print(df.head())
        else:
            df = df.rename(columns = {var : lfs_var_labels[var.lower()]})

        #if we want to save the original 
        if replace_variables == False:
                df = df.rename(columns = {var_name : var})
    return df  

