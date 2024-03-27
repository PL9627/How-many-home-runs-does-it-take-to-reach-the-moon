The distance to the moon from Earth is 238,900 miles or roughly 1.261 billion feet.  Which MLB position player last season would be able to reach that distance with the smallesst amount of home runs?

  That journey begins by first searching through the Baseball Savant website for the necessary data.  This particular website and the people behind it have been tracking MLB related advanced statistics since 2015.  
Here I downloaded the csv files for the 2023 exit velocity and barrels leaderboard and a custom leaderboard containing home runs and plate appreances. These files contained the average home run distance and home run
numbers for each batter in the respective leaderboards.  The files are filtered by Statcasts qualified plate appearances.  This means that each batter has had at least 2.1 plate appearances per game their team has played.  
Using the Python library Pandas, the csv files are read and then changed to dataframes so that Python can be used to change parts of the dataframe.  

  The dataframes are then combined using the merge() method and duplicate columns are dropped from the new dataframe using the dropduplicates() method.  The new dataframe is then filtered by setting the parameters 
to batters who have greater than or equal to 20 home runs and an average home run distance greater than 400 feet.  This new filtered dataframe is then sorted by average home run distance descending.  
The batter who hit the longest home runs the most is Shohei Ohtani at an average home run distance of 422 feet.  If Ohtani never tires and never gains an injury from this hypothetical situation, 
it would take him roughly 2.988 million home runs to reach the same distance as from the Earth to the moon.  This is all assuming he hits off a pitching machine that will perfectly deliver fastballs right down 
the middle of home plate.

  If 
