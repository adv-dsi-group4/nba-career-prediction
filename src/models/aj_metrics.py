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

    fpr, tpr, thresh = roc_curve(y_true, y_pred)
    roc_auc = auc(fpr, tpr)
    print('AUC = %0.3f' % roc_auc)
    plt.plot(fpr, tpr, 'b', label='AUC = %0.3f' % roc_auc)
    plt.plot([0,1],[0,1], 'r--')
    plt.xlim([-0.1,1.0])
    plt.xlim([-0.1,1.01])
    return(plt)

def eval_report(true, pred):

    import numpy as np
    import pandas as pd
    from sklearn import metrics

    unique_label = np.unique([true, pred])
    cmtx = pd.DataFrame(
        metrics.confusion_matrix(true, pred, labels=unique_label), 
        index=['true:{:}'.format(x) for x in unique_label], 
        columns=['pred:{:}'.format(x) for x in unique_label]
    )
    print("Confusion Matrix:")
    print(cmtx)
    print("")
    print("Classification Report:")
    print(metrics.classification_report(true, pred))
    print("")
    print("ROC Curve:")

    import matplotlib.pyplot as plt  
    plot_roc(true, pred)
    plt.show()
    
        
