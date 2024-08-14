'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
import seaborn as sns
import matplotlib.pyplot as plt
def scatterplot_felony_prediction(pred_universe):
    """
    Creates a scatter plot of felony vs. nonfelony predictions, hued by whether the current charge is a felony.
    
    Parameters:
    - pred_universe dataframe

    Returns:
    - Scatter plot saved as a PNG file
    """

    pred_universe['charge_type'] = pred_universe['prediction_felony'].apply(lambda x: 'Felony' if x > 0.5 else 'Misdemeanor')

    sns.lmplot(data=pred_universe, 
               x='prediction_felony', 
               y='prediction_nonfelony', 
               hue='charge_type', 
               markers=["o", "s"])  # 'o' for felony, 's' for misdemeanor

    plt.savefig('./data/part5_plots/scatterplot_felony_vs_nonfelony.png', bbox_inches='tight')
    
    print("The dots on the right hand side of the plot represent a group of people who are predicted to have high chances of committing either a felony or non-felony crime again. The individuals in this group are expected to have high overall probabilities of being rearrested regardless of the type of offense. It could be an indication of a group with high chances according to the model.")

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
def scatterplot_felony_prediction_vs_actual(pred_universe):
    """
    Creates a scatter plot of felony rearrest predictions vs. actual rearrest outcomes.
    
    Parameters:
    - pred_universe dataframe

    Returns:
    - Scatter plot saved as a PNG file
    """
    sns.scatterplot(data=pred_universe, 
                    x='prediction_felony', 
                    y='y_felony')  
    
    plt.savefig('./data/part5_plots/scatterplot_felony_prediction_vs_actual.png', bbox_inches='tight')
    
    print("By looking at this diagram, if there is a distinction between anticipated probabilities and genuine consequences, one can understand the calibration of this model. In case predictions closely match actual rearrests, then these models seem well-calibrated. Nonetheless, when there is substantial mismatch, it indicates that some improvements should be made for better prediction accuracy.")