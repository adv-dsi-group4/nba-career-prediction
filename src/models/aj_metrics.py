def confusion_matrix(true, pred):
    # Confusion matrix with labels

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

def plot_roc(y_true, y_pred):
    
    from sklearn.metrics import roc_curve, auc
    import matplotlib.pyplot as plt

    fpr, tpr = roc_curve(y_true, y_pred )
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, 'b', label='AUC = %0.3f' % roc_auc)
    plt.plot([0,1],[0,1], 'r--')
    plt.xlim([-0.1,1.0])
    plt.xlim([-0.1,1.01])
    return(plt)

def visualise_accuray(model, X, y, pred):

    from sklearn.metrics import plot_roc_curve,  accuracy_score
    plot_roc_curve(model, X, y)   
    print("Accuracy Score:", accuracy_score(y, pred))
    

