# GHArchive_Analysis

## About the dataset
1. The GitHub Archive data for 12 hours is extracted and dumped into a PySpark dataframe for further processing.
2. The dataframe has nested fields and has details about GitHub users, events, repos, organizations, payloads, and timestamp. 
3. Users: There are two type of users in the given dataset. 
	org_users are who use GitHib for organizational collaboration. They pay fpr the GitHub services.
	individual_users are who use GitHub to document their work in personal repos.
4. Events: An event is any activity that a user performs on the GitHub site. There are 20+ possible events, and in the given dataset only 14 distinct events were present. 
5. Repos: Repositories have information about the owner of the repo, language used, contributors, forks_count, etc. 
6. Payloads: Payload is one of the important field and has more detailed data about an event. The structure of payload varies for every event type.

## Data Exploration

1. Since the dataset is huge, I have analyzed only the interesting fields to gather insights. 
For example, (a) volume of different type of events across two types of users. 
			(b) Which category does the majority of active users belong to? org_users or individual_users
			(c) What are the popular repositories? How do we measure popularity? Which organisations own those repositories? etc. 

## Data Wrangling

1. I created a master_df dataframe from the raw unprocessed json data. Then relevant data is sliced from the dataframe as required to answer the questions.

2. There are 5 custom dataframes created: main_df, repo_df, org_df, payload_df, top500_repos_df

3. Data cleaning (casting types of fields, imputing missing & null values) was done to transform the fields before loading them into these custom dataframes.  

4. These dataframes are then converted into csv to be used for aggregation & visualization in Tableau.

## How to run the notebook

1. Import the file into Databricks community edition or a local machine with Spark v2.4.5 installed. 