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

# Coding Problems
## Solution Approach
* 
### Problem 1.1 : 	
It is observed that series of repeated sum of squares of digits of any number always converge to a 
single digit number at some point. So it is not necessary to find this series for all numbers.
As an optimal approach, we calculate this series for numbers from 1 to 9 and find the set of numbers 
S whenever the series gets stuck in a loop. 

For example, for number 2, the series looks like:

    [2, 4, 16, 37, 58, 89, 145, 42, 20, 4]

For number 3, the series looks like:

    [3, 9, 81, 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37]

For number 7, the series ends up in 1:

    [7, 49, 97, 130, 10, 1]
    
To find the common set S where each series that does not converge to 1 end up in, the intersection of 
all such series is taken.

### Problem 1.2 :

The solution utilizes 2 important facts about the problem:

* The common set of numbers where all the non converging series end up is found to be:

        Set S:  {4, 37, 42, 16, 145, 20, 89, 58}
    So we store that once sum of digits of any number lies in this set, it will never converge to 1.

* In the range [1, 10^9], the number with largest sum of squares of digits is 999999999. That is, 9*(9^2) = 729. 
Thus, any number in the set [1, 10^9] will have its sum of squares of digits mapped to [1, 729]. 

* A naive approach to solution will check for every number upto k, if convergent sum series will end up in a loop.

* For numbers in the set [1, 729], the solution approach stores if the number's series converges to 1 or not. 
If the given k is less than 729, we calculate the series of sum of squares for each number less than k and find 
if the series converges to 1, and set convergence_list[number] = 1. convergence_list is a list of size 730. 
If the given k is greater than 729, we apply the same logic for all numbers upto 729 and and for numbers greater 
than 729, we calculate the sum of squares of its digits only once (as opposed to finding the complete convergence series), 
and directly access the convergence_list with sum of squares of its digits as index. Not having to calculate the 
convergence series for numbers greater than 729 saves computation time.

* For example, when processing number 3, we know that all the numbers in its series will never converge to 1, store that these numbers 
(3, 9, 81, 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37) will never converge to 1, for any other number if sum of squared digits 
end up in any of these numbers, we know it can never converge to 1. For example, 56-> 5^2+6^2 = 61, we know it will not converge, so we stop 
calculating the series, mark in convergence_list that 56 will never converge to 1, and move on to the next number. This saves a lot of computation time.

### Problem 2 :

* Note: If special characters and numbers are given in the input, the program will still be able to count character pairs 
in words and print the number of occurrence as a Histogram.

## How to run the solution files
1. Folder "Coding_Problems" contain solutions to the two coding problems. Solution files are named prob_1_1.py, prob_1_2.py, and prob_2.py according to the problem number.

2. Each problem can be run using any python interpreter. For example:

   ```bash
   $> python prob_1_1.py  
   ```