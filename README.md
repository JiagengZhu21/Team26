# COMP208
Team26 Group Members: 

Jia Chen(201768810), Jiageng Zhu(201770214), Junqin Cheng(201768863), 	   Luyuan Huang(201769063), Xiankai Shi(201769457), Yifei Chen(201768854)

Project Title: DataCraft - An integrated, interactive tool for feature engineering in machine learning or data modeling

Project Description:
The general process of machine learning involves: feature engineering/data preprocessing – training – evaluating and analyzing the model's performance, and then iterating through this process. Examples of feature engineering include: handling missing values, cluster analysis (often enhanced with visualization for increased interactivity), encoding categorical variables (converting classes into numbers), normalization, standardization, etc. [1]
Feature engineering takes up a long time of a data scientist's work [2]. However, most packages specifically designed for feature engineering lack a user-friendly interactive interface. There are many python packages can be used in data preprocessing which must be loaded in programming environment such as pandas, scipy, numpy, ski-learn, etc. As a result, analysts or developers often find themselves engaged in repetitive coding tasks during the feature engineering process [2]. And there is almost no software available that facilitates interactive feature engineering work implemented by GUI.
The project we are developing focuses on addressing the challenge of repetitive code writing in feature engineering. This is achieved through an efficient computational system and a graphical interface with good interactivity.

Aims and Objectives:
Aims:
Our project goal is to create an interactive tool with GUI that integrates various feature engineering methods, aiming to simplify the feature engineering process and enhance the time efficiency of data scientists or machine learning engineers.

Objectives:
In order to achieve the aim above, the DataCraft has set the following specific goals:
1.	Integration of data preprocessing methods: DataCraft contains multiple methods for tasks include but not limited to data cleaning, encoding, transforming, clustering and dimension reduction.
2.	Ability to process multiple datasets: Ensure that this application could process different datasets parallelly. 
3.	User-friendly interface implementation: Develop an intuitive graphical user interface (GUI) that enables users to easily configure preprocessing steps, perform data transformations, view processing results and export dataset without writing code.
4.	Extensible and modular design: Ensure the flexibility of the software architecture to add new data processing modules and algorithms.
5.	High performance computation: Development will base on efficient data science libraries which is widely used to implement specific feature engineering task.

Development & Implementation Summary:
1. The development tool for this project will be integrated Python programming environment with specific data processing library such as pandas and skit-learn [2][3] and powerful UI developing libraries such as wxpython and PyGTK. 
2. This project will adopt the front&back - end architecture, which the final product being a desktop executable application. The front-end corresponds to the graphical user interface (GUI), while the back-end corresponds to the set of task implementations and its python interpreter kernel. This project will first develop the back-end and develop the graphical interface according to the set of back-end functions.
3. In data preprocessing or data cleaning, each task has several execution methods. For example, handling missing values can include dropping them, filling them with mean values, or utilizing advanced statistical methods such as the EM algorithm [3]. This application will use task – methods structure to manage functions (like data transforming – normalization, standardization and dimension reduction – PCA, ICA).   
Data Sources:
This application serves as a desktop application for processing input datasets. Since both its input and output data reside within the user's local machine, and the program itself does not generate additional cached data during operation, this application ensures users retain the right to acquire and deal all datasets by rules.
