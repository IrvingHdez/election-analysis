# Election Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following task to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Determine the county which had the larges vote turnout

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The condidate results were:
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was:
    - Candidate: Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
- The county which had the largest vote turnout: Denver with 306,055 votes

![Terminal output](https://github.com/IrvingHdez/election-analysis/blob/master/analysis/election_results.PNG)

## Election Audit Summary
**Statement to the Election Commission**
1. This script can be reused for future elections by substituting the election results data file (csv)
* file_to_load = os.path.join("Resources", "election_results.csv") <> file_to_load = os.path.join("Resources", "any_other_election_results.csv")
2. The section to determine the largest county vote turnout can be optimized by sorting the vote nunmber from largest to smallest value by using the list.sort() function.