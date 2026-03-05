# College_Football_Transfer_Value
Quantifying the talent departed in the transfer portal by team.

Article on findings here:
https://www.mwcconnection.com/peak-perspective/81129/peak-perspective-revamped-transfer-portal-analysis
Each player is given a rating when they enter the portal, similar to when they are recruited out of high school. The ratings referenced come from 247sports.

I did this to account for positional differences, and because the data was in a single location. I tried in the past to merge this with data from PFF to track snap counts, but it became too much of a challenge to accurately merge everything. Plus, the recruiting ratings reflected potential rather than accomplishments, which helps balance out everything. My formula for each player was to add their star rating plus their numeric rating. So for my example with Jackson Harris, who left Hawaii, his 3 stars and a numeric rating of 0.89 equaled transfer value of 3.89.

For quarterbacks I did an extra modification. They tend to get scouted more, and the original formula skewed in favor of highly recruited quarterbacks with little playing time. I took their total attempts from the prior year, divided them by 100, and multiplied that by their transfer value, with a max of 1.3 - that was the highest difference, percentage wise, between what quarterbacks in the NFL make compared to non-quarterbacks. I felt that was a way to adjust a quarterbacks value based on their usage, without being biased towards those in pass-heavy schemes. I then squared the final total to help magnify the difference between the best and worst players.

The overall team score was the sum of each player’s value. A lower score meant more talent was retained, which resulted in a higher grade.

As far as the grades, those are comparing how they did this past year to trends since 2021. A+ means very little talent left, F- means a lot of talent went out the door. Since this is based on historical trends, no school is guaranteed an A+ each year.

There were a few modifications I had to make.

    First, I only looked at players who switched schools. If they weren’t picked up in the portal, they likely were a player who would have ridden the bench, and consequently aren’t too difficult to replace. It also addressed the few cases where a player entered the portal and decided to return to their school.
    Second, while most players were given a star rating, not all were given a numeric rating (i.e. 0.98, 0.76). From what I found, this applied to players who didn’t get enough playing time to be properly scouted, and their star rating was largely based on what they did in high school. To address this, after playing around with some numbers I gave them a numeric rating of -.5. They get the high star rating to get credit for their potential, but are hurt for lack of playing time.

This admittedly isn’t a perfect way to look at this, isn’t meant to compare positions, and isn’t meant to quantify how much more value one player has than another. It’s a first step in trying to measure the value of players leaving through the portal. Ideally I’d look at NIL or other player income, but those numbers aren’t publicly available; anything you see online is an estimate, and collectives aren’t required to publish NIL funds (and I doubt they ever will). The main reason I did this was to try and compare losing a star player to losing several backup players. I call this version 1.0 because I plan on doing more to clean this up, so everything should be taken with a grain of salt.
