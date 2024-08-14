'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
import seaborn as sns
import matplotlib.pyplot as plt

def catplot_felony_rearrest(pred_universe):
    """
    Creates a catplot where the x-axis is whether the arrest had a felony charge, 
    and the y-axis is the prediction for felony rearrest.

    Parameters:
    - pred_universe: The dataframe containing prediction-related data for individuals, including the 'has_felony_charge' column.

    Returns:
    - A bar catplot saved as an image.
    """
    sns.catplot(data=pred_universe, 
                x='has_felony_charge', 
                y='prediction_felony', 
                kind='bar')
    
    plt.title('Prediction for Felony Rearrest by Felony Charge')
    plt.xlabel('Had Felony Charge')
    plt.ylabel('Prediction for Felony Rearrest')
    plt.savefig('./data/part4_plots/catplot_felony_rearrest.png', bbox_inches='tight')


# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
# In a print statement, answer the following question: What might explain the difference between the plots?
def catplot_nonfelony_rearrest(pred_universe):
    """
    Creates a catplot where the x-axis is charge degree and the y-axis is prediction for nonfelony rearrest.
    
    Parameters:
    - pred_universe dataframe

    Returns:
    - A bar catplot
    """
    sns.catplot(data=pred_universe, 
                x='has_felony_charge', 
                y='prediction_nonfelony', 
                kind='bar')
    plt.title('Prediction for Nonfelony Rearrest by Charge Degree')
    plt.savefig('./data/part4_plots/catplot_nonfelony_rearrest.png', bbox_inches='tight')
    

    print("The disparity between the felony and nonfelony rearrest prediction plots might arise because of distinct patterns of subsequent arrests stemming from the charge type. Higher overall risks of a repeat rearrest could be tied to felony charges, while nonfelonies’ forecasts might fluctuate contingent upon disparate factors such as nature of the crime or criminal history. The inconsistency reveals how different charges influence forecasts for recidivism and also highlights how effective a certain predictive model is in relation to crime types.")


# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
# 
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?
def catplot_felony_rearrest_hue(pred_universe):
    """
    Creates a catplot where the x-axis is charge degree and the y-axis is prediction for felony rearrest,
    with hue based on whether the person actually got rearrested for a felony crime.
    
    Parameters:
    - pred_universe dataframe

    Returns:
    - A bar catplot with hue
    """
    sns.catplot(data=pred_universe, 
                x='has_felony_charge', 
                y='prediction_felony', 
                hue='y_felony', 
                kind='bar')
    plt.title('Prediction for Felony Rearrest by Charge Degree and Actual Rearrest')
    plt.savefig('./data/part4_plots/catplot_felony_rearrest_hue.png', bbox_inches='tight')
    
    
    print("If there are more chance for those with a continuous crime of felony who do not get re-arrested under felony than for those with a current misdemeanor charge who were re-arrested under the same felony, then it could mean that this model is probably over-estimating the likelihood of rearrest under felony, among people facing felony charges but yet no such record. This might be an indication that this model is very much guided by what kind of present charge is in place and may so assign higher risk scores to felonies regardless of whether or not they end up being rearrested.")
    print("The higher predicted probability for non-re-offenders with felony charge than re-offenders on misdemeanor charges implies that the model may underestimate risks of some individuals and overestimate them among others. It indicates that the model may be misjudging certain individuals’ risks while exaggerating those of others. In this regard, recalibration might be necessary to make the model reflect real-world chances of being rearrested more accurately across different types of charges.")
