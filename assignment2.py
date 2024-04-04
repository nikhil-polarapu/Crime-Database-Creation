import argparse
import src.assignment1_helper as src

def main(url):
    # Download data
    incident_data = src.fetchincidents(url)

    # Extract data
    incidents = src.extractincidents(incident_data)
	
    # Create new database
    db = src.createdb()
	
    # Insert data
    src.populatedb(db, incidents)
	
    # Print incident counts
    src.status(db)

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", type=str, required=True, 
                         help="CSV file that contains the URLs.")

    args = parser.parse_args()
    if(args.urls):
        with open(args.urls, 'r') as f:
            for url in f:
                url = url.strip('\n')
                if(url):
                    main(url)
