#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import progressbar

from itertools import combinations
import os
import shutil

SCALE = 25
SCALE_LIST = ["{0}".format(i+1) for i in range(0, SCALE)]

features = {
	"CRIM": "per capita crime rate by town",
	"ZN": "proportion of residential land zoned for lots over 25,000 sq.ft.",
	"INDUS": "proportion of non-retail business acres per town",
	"CHAS": "If tract bounds Charles River or not",
	"NOX": "nitric oxides concentration (parts per 10 million)",
	"RM": "average number of rooms per dwelling",
	"AGE": "proportion of owner-occupied units built prior to 1940",
	"DIS": "weighted distances to five Boston employment centres",
	"RAD": "index of accessibility to radial highways",
	"TAX": "full-value property-tax rate per $10,000",
	"PTRATIO": "pupil-teacher ratio by town",
	"B": "1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town",
	"LSTAT": "% lower status of the population",
	"MEDV": "Median value of owner-occupied homes in $1000's",
}

housing_df = pd.read_csv("housing.data", names=features.keys(), delim_whitespace=True)

# Printing the dataset in a table-like format
print(housing_df)

# Printing summary statistics
print(housing_df.describe())

if os.path.isdir("plots"):
	shutil.rmtree("plots")

for directory in ["plots", "plots/histograms", "plots/scatters", "plots/heatmaps"]:
	try:
	    os.stat(directory)
	except:
	    os.mkdir(directory)

print("Creating histogram figures...")
bar_histograms = progressbar.ProgressBar(maxval=len(features), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
i_histograms = 0
bar_histograms.start()
for feature, description in features.items():
	i_histograms += 1
	bar_histograms.update(i_histograms)
	# Plotting histograms and saving them
	plt.hist(housing_df[feature], bins=10, color='blue')
	plt.title(f"{feature} count: {description}")
	plt.xlabel(feature)
	plt.ylabel('Count')
	plt.savefig(f'plots/histograms/{feature}.png', format='png')
	plt.clf()
bar_histograms.finish()

feature_couples = list(combinations(features.keys(), 2))

print("Generating heatmap figures...")
bar_scatters = progressbar.ProgressBar(maxval=len(feature_couples), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
i_scatters = 0
bar_scatters.start()
for x, y in feature_couples:
	i_scatters += 1
	bar_scatters.update(i_scatters)
	# Plotting scatterplots and saving them
	plt.scatter(housing_df[x], housing_df[y], color='blue')
	plt.title(f'{x} to {y}')
	plt.xlabel(x)
	plt.ylabel(y)
	plt.savefig(f'plots/scatters/{x}_to_{y}.png', format='png')
	plt.clf()
	for heat_factor in features.keys():
		if heat_factor not in (x, y):
			grouped_housing_df = housing_df
			grouped_housing_df[f'{x}_GROUP'] = pd.cut(housing_df[f'{x}'], SCALE, labels=SCALE_LIST)
			grouped_housing_df[f'{y}_GROUP'] = pd.cut(housing_df[f'{y}'], SCALE, labels=SCALE_LIST)
			matrix = pd.pivot_table(grouped_housing_df, values=heat_factor, index=f'{x}_GROUP', columns=f'{y}_GROUP', aggfunc='mean')
			# Plotting heatmaps and saving them
			c = plt.pcolor(matrix, cmap='coolwarm')
			plt.title(f"Heat factor: {features[heat_factor]}")
			plt.xlabel(features[x])
			plt.ylabel(features[y])
			plt.tick_params(
			    axis='both',
			    which='both',
			    bottom=False,
			    labelleft=False,
			    left=False,
			    labelbottom=False)
			plt.colorbar(c)
			plt.savefig(f'plots/heatmaps/{x}_to_{y}_by_{heat_factor}.png', format='png')
			plt.clf()
bar_scatters.finish()
