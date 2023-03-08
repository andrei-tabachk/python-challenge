import csv
import os

election_csv = os.path.join("Resources", "election_data.csv")

# Open file
with open('election_csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # variables for vote counts
    total_votes = 0
    stockham_votes = 0
    degette_votes = 0
    doane_votes = 0

    # Read each row of data
    for row in reader:
        # Add up the total votes
        total_votes += int(row[1])

        # Count the votes for each candidate
        if row[2] == 'Charles Casper Stockham':
            stockham_votes += int(row[1])
        elif row[2] == 'Diana DeGette':
            degette_votes += int(row[1])
        elif row[2] == 'Raymon Anthony Doane':
            doane_votes += int(row[1])

    # Calculate the percentage 
    stockham_percent = stockham_votes / total_votes * 100
    degette_percent = degette_votes / total_votes * 100
    doane_percent = doane_votes / total_votes * 100

    #Print title
    print("Election Results")
    print("-----------------------")

    # Print the results
    print('Total Votes:', total_votes)
    print("-----------------------")
    print('Charles Casper Stockham:', '{:.3f}% ({})'.format(stockham_percent, stockham_votes))
    print('Diana DeGette:', '{:.3f}% ({})'.format(degette_percent, degette_votes))
    print('Raymon Anthony Doane:', '{:.3f}% ({})'.format(doane_percent, doane_votes))
    print("-----------------------")

    # Determine the winner
    if degette_votes > stockham_votes and degette_votes > doane_votes:
        print('Winner: Diana DeGette')
    elif stockham_votes > degette_votes and stockham_votes > doane_votes:
        print('Winner: Charles Casper Stockham')
    else:
        print('Winner: Raymon Anthony Doane')
    print("-----------------------")