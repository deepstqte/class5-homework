#### Introduction

The `data-processor.py` script processes the `housing.data` Boston housing dataset, shows some basic information about the dataset, generates multiple plots, and saves them in a `/plots` folder for exploratory reasons.

#### Usage

In order to use the script, and generate the plots:

1- Clone this repository with `git clone git@github.com:gzork/class5-homework.git`

2- Assuming that you have `pip3` or `pip` installed and using `python3`, run the following command to install the required python packages:

`pip3 install -r requirements.txt`

3- Now, run the script, please note that the script generates a lots of plots, this takes some time, but it shows the progress of the generation.

#### The generated plots

There are three sets of plots generated:

##### `/plots/histograms`

These are histograms generated for the features of the dataset, one for each feature.

##### `/plots/scatters`

These are scatter plots generated for each combination of 2 features of the dataset.

##### `/plots/heatmaps`

In order to generate these, each combination of 2 features of the dataset was converted to a pivot table, using each one of the remaining features for the values. Since we have 14 features, this generates a lots of heatmaps, most of them don't really show any pattern, not have any useful insights, but many of them do, we'll talk in detail about one example in the next section.

The generation of these heatmaps (1092 files) takes a couple of minutes, but a progress bar is shown.

#### Example of a heatmap with useful insights

We'll briefly analyse the plot `/plots/heatmaps/DIS_to_LSTAT_by_AGE.png`

![image](https://user-images.githubusercontent.com/7915931/57978868-05010200-79e3-11e9-85ab-6b9446a179a1.png)

This heatmap shows that about 30% of the tracts that are closest to employment centres have tracts with both low and high percentages of population with low social status.

Although, the hidden insight, that this heatmap is allowing us to extract, is that in that sample of about 30% of the tracts that are the closes to the employment centers, the tracts with mostly lower status population are composed of relatively newly built units (after 1940) and that the ones with low percentages of lower status population (richer population) are relatively old owner-occupied units, which were built before 1940.