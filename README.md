# Title
Unemployment Rate and GDP Growth Correlation in the United States

## Description

Understanding the link between unemployment rate and economic growth which can reveal key insights into the U.S. economy. In this project I'll explores the relationship between unemployment rates and real GDP growth over both long-term and recent periods. By analyzing annual data from 1960 to 2023 and quarterly data from the last 10 years, we aim to identify patterns, cycles, and short-term variations. Examining how these indicators move together or diverge can provide a clearer understanding of their impact on each other and potentially inform economic policies and forecasts. This dual-level analysis will help us see how changes in employment and economic output align or differ during various economic cycles.


## Work Packages

1. Data Collection [#1][i1]
2. Data Cleaning and Preprocessing [#2][i2]
3. Exploratory Data Analysis (EDA) [#3][i3]
4. Correlation Analysis [#4][i4]
5. Data Visualization [#5][i5]
6. Reporting [#6][i6]

[i1]: https://github.com/rebel47/MADE-Project/issues/1
[i2]: https://github.com/rebel47/MADE-Project/issues/2
[i3]: https://github.com/rebel47/MADE-Project/issues/3
[i4]: https://github.com/rebel47/MADE-Project/issues/4
[i5]: https://github.com/rebel47/MADE-Project/issues/5
[i6]: https://github.com/rebel47/MADE-Project/issues/6

# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.

## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones, so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to HTML: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervals, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/).

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions → Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```