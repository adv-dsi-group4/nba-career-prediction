def confusion_matrix(true, pred):
    ''' Generate the confusion matrix in the dataframe format
    
    Parameters
    ----------
    true : an array
        An array of original target values to compare with
    pred: an array
        An array of predicted value

    Returns
    -------
    pd.DataFrame
        Pandas  dataframe with true: 0 / 1 in rows and pred: 0/1 in columns
    '''

    import numpy as np
    import pandas as pd
    from sklearn import metrics

    unique_label = np.unique([true, pred])
    cmtx = pd.DataFrame(
        metrics.confusion_matrix(true, pred, labels=unique_label), 
        index=['true:{:}'.format(x) for x in unique_label], 
        columns=['pred:{:}'.format(x) for x in unique_label]
    )
    return(cmtx)
    
def eval_report(m, X, true, pred):
    
    import numpy as np
    import pandas as pd
    from sklearn import metrics

    unique_label = np.unique([true, pred])
    cmtx = pd.DataFrame(
        metrics.confusion_matrix(true, pred, labels=unique_label), 
        index=['true:{:}'.format(x) for x in unique_label], 
        columns=['pred:{:}'.format(x) for x in unique_label]
    )
    print(cmtx)
    print(metrics.classification_report(true, pred))
    
    import matplotlib.pyplot as plt  
    metrics.plot_roc_curve(m, X, pred)
    plt.show()
    
        
