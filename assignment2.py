import argparse
import src.assignment2_helper as src

def main(url):
    # Download data
    incident_data = []
    for url in urls:
        incident_data.append(src.fetchincidents(url))

    # Extract data
    incidents = src.extractincidents(incident_data)
	
    # Create new database
    db = src.createdb()
	
    # Insert data
    src.populatedb(incidents)
	
    # Print incident counts
    src.status()

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", type=str, required=True, 
                         help="CSV file that contains the URLs.")

    args = parser.parse_args()
    urls = []
    if(args.urls):
        with open(args.urls, 'r') as f:
            for url in f:
                url = url.strip('\n')
                if(url):
                    urls.append(url)
        main(urls)
