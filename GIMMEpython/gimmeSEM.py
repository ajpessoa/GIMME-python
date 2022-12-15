
import semopy as sem
from semopy import Model
from semopy import ModelMeans
import pandas as pd

def gimmeSEM_python(data: str, out: str):
    """ Function used to calculate the SEM of multiple individuals in various datasets

    Args:
        data (str): name of the file containing the data
        out (str): name of the folder where the results are to be stores

    Returns:
        list: A list of Data Frames with the resulting SEM models for each individual
    """
    print(data)

    # create the latent variable model
    model = '''L1 =~ V1 + V2 + V3 
    L2 =~ V4 + V5 + V6
    L3 =~ V7 + V8 + V9
    '''

    lv_model_all = sem.Model(model)

    lv_obs_all = list()
    # fit the model to all the dataframes
    for i in data['simDataLV']:
        res = lv_model_all.fit(data['simDataLV'][i].to_pandas())
        lv_obs_all.append(print (lv_model_all.inspect()))
        sem.report(lv_model_all, out+"\\"+i)

    return lv_obs_all