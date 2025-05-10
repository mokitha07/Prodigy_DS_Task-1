.

🚢 Titanic Dataset - Task 1: Data Analysis & Exploration
This project is part of Task 1 of Titanic dataset analysis and exploration. The goal is to perform initial data understanding, preprocessing, and visual exploration using Python in Visual Studio Code (VS Code).

📁 Project Structure
bash
Copy
Edit
titanic-task1/
│
├── data/
│   └── titanic.csv            # Original Titanic dataset
│
├── notebooks/
│   └── task1_analysis.ipynb   # Jupyter notebook with EDA code
│
├── scripts/
│   └── task1_analysis.py      # Python script with analysis code
│
├── images/
│   └── *.png                  # Visualizations and plots
│
└── README.md                  # Project documentation
📌 Objectives
Load and inspect the dataset

Identify missing data and data types

Understand key columns (e.g., Survived, Sex, Pclass, Age)

Visualize survival statistics

Build initial hypotheses about survival factors

🧰 Tools & Libraries Used
Python 3.x

VS Code

Pandas

NumPy

Matplotlib

Seaborn

Jupyter Notebook

📊 Key Steps
Data Loading – Used pandas.read_csv() to load the dataset.

Initial Exploration – Used .head(), .info(), and .describe() to understand the structure.

Missing Value Check – Identified missing values in Age, Cabin, and Embarked.

Basic Visualizations – Created bar plots for:

Survival rate by gender

Survival rate by class

Age distribution

Embarked distribution

📈 Sample Insights
Females had a higher survival rate.

Passengers in 1st class were more likely to survive.

Many young children also survived.

A significant number of values were missing in the Cabin column.

▶️ How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/titanic-task1.git
cd titanic-task1
Install required libraries:

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn
Open the Jupyter notebook (task1_analysis.ipynb) in VS Code and run all cells.

📌 Dataset Source
Kaggle Titanic: Machine Learning from Disaster
vedio : https://drive.google.com/file/d/18sRDs-ozFw2EZG3ewhWrdednIHVfatGJ/view?usp=sharing
contact me : http://www.linkedin.com/in/mokitha007

