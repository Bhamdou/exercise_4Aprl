from bs4 import BeautifulSoup

def read_html_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_job_listings(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    job_listings = soup.find_all('div', class_='job-listing')

    jobs = []
    for listing in job_listings:
        job_title = listing.find('h2', class_='job-title').text
        company = listing.find('p', class_='company').text
        location = listing.find('p', class_='location').text
        description = listing.find('p', class_='description').text
        job = {'job_title': job_title, 'company': company, 'location': location, 'description': description}
        jobs.append(job)
    return jobs

def main():
    html_content = read_html_file('job_listings.html')
    job_listings = parse_job_listings(html_content)

    for job in job_listings:
        print("Job Title:", job['job_title'])
        print("Company:", job['company'])
        print("Location:", job['location'])
        print("Description:", job['description'])
        print('\n')

if __name__ == "__main__":
    main()
sorted