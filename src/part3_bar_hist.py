'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

# 1. Using the pre_universe data frame, create a bar plot for the fta column.

from matplotlib import pyplot as plt
import seaborn as sns

def barplot_fta(pred_universe):
    '''
    Creates and saves a bar plot for the 'fta' column from the pred_universe dataframe.

    Parameters:
    - pred_universe dataframe

    Saves:
    - PNG file of the bar plot in './data/part3_plots/barplot_fta.png'
    '''
    # Set the Seaborn theme and figure size
    sns.set_theme()
    sns.set(rc={'figure.figsize':(8, 6)})
    plt.figure(figsize=(8, 6))
    sns.countplot(data=pred_universe, x='fta')

    plt.title('Bar Plot of FTA')
    plt.xlabel('FTA')
    plt.ylabel('Count')

    plt.savefig('./data/part3_plots/barplot_fta.png', bbox_inches='tight')
    plt.close()

# 2. Hue the previous barplot by sex
def barplot_fta_hue(pred_universe):
    '''
    Creates and saves a bar plot for the 'fta' column from the pred_universe dataframe, with hue by 'sex'.

    Parameters:
    - pred_universe dataframe

    Saves:
    - PNG file of the bar plot with hue in './data/part3_plots/barplot_fta_hue.png'
    '''
    # Set the Seaborn theme and figure size
    sns.set_theme()
    sns.set(rc={'figure.figsize':(8, 6)})

    # Create a new figure
    plt.figure(figsize=(8, 6))

    sns.countplot(data=pred_universe, x='fta', hue='sex')

    plt.title('Bar Plot of FTA with Hue by Sex')
    plt.xlabel('FTA')
    plt.ylabel('Count')


    plt.legend(title='Sex')
    plt.savefig('./data/part3_plots/barplot_fta_hue.png', bbox_inches='tight')
    plt.close()


# 3. Plot a histogram of age_at_arrest
def histogram_age_at_arrest(pred_universe):
    '''
    Creates and saves a histogram for the 'age_at_arrest' column from the pred_universe dataframe.

    Parameters:
    - pred_universe dataframe

    Saves:
    - PNG file of the histogram in './data/part3_plots/histogram_age_at_arrest.png'
    '''
    sns.set_theme()
    sns.set(rc={'figure.figsize':(8, 6)})

    plt.figure(figsize=(8, 6))

    sns.histplot(data=pred_universe, x='age_at_arrest', bins=30)

    plt.title('Histogram of Age at Arrest')
    plt.xlabel('Age at Arrest')
    plt.ylabel('Frequency')

    # Save the plot to a file
    plt.savefig('./data/part3_plots/histogram_age_at_arrest.png', bbox_inches='tight')
    plt.close()

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def histogram_age_at_arrest_custom_bins(pred_universe):
    '''
    Creates and saves a histogram for the 'age_at_arrest' column from the pred_universe dataframe
    with custom bins representing specific age groups.

    Parameters:
    - pred_universe dataframe

    Saves:
    - PNG file of the histogram with custom bins in './data/part3_plots/histogram_age_at_arrest_custom_bins.png'
    '''
    # Set the Seaborn theme and figure size
    sns.set_theme()
    sns.set(rc={'figure.figsize': (8, 6)})

    # Define custom bins and labels
    bins = [18, 21, 30, 40, 100]
    bin_labels = ['18-21', '21-30', '30-40', '40-100']

    plt.figure(figsize=(8, 6))

    sns.histplot(data=pred_universe, x='age_at_arrest', bins=bins)

    plt.title('Histogram of Age at Arrest with Custom Bins')
    plt.xlabel('Age at Arrest')
    plt.ylabel('Frequency')

    # Set the x-ticks to the midpoints of the bins
    bin_midpoints = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins) - 1)]
    plt.xticks(ticks=bin_midpoints, labels=bin_labels)
    plt.savefig('./data/part3_plots/histogram_age_at_arrest_custom_bins.png', bbox_inches='tight')
    plt.close()