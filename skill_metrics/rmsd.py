import numpy as np

def rmsd(predicted,reference):
    '''
    Calculate root-mean-square deviation (RMSD) between two variables

    Calculates the root-mean-square deviation between two variables 
    PREDICTED and REFERENCE. The RMSD is calculated using the 
    formula:

    RMSD^2 = sum_(n=1)^N [(p_n - r_n)^2]/N
 
    where p is the predicted values, r is the reference values, and
    N is the total number of values in p & r. Note that p & r must
    have the same number of values.
 
    Input:
    PREDICTED : predicted values
    REFERENCE : reference values
 
    Output:
    R : root-mean-square deviation (RMSD)

    Author: Peter A. Rochford
        Symplectic, LLC
        www.thesymplectic.com
        prochford@thesymplectic.com

    Created on Dec 9, 2016
    '''

    # Check that dimensions of predicted and reference fields match
    pdims= predicted.shape
    rdims= reference.shape
    if not np.array_equal(pdims,rdims):
        message = 'predicted and reference field dimensions do not' + \
            ' match.\n' + \
            'shape(predicted)= ' + str(pdims) + ', ' + \
            'shape(reference)= ' + str(rdims) + \
            '\npredicted type: ' + str(type(predicted))
        raise ValueError(message)

    # Calculate the RMSE
    r = np.sqrt(np.mean(np.square(predicted - reference)))
    #or 
#     r = np.sqrt(np.nanmean(np.square(predicted - reference)))


    return r
