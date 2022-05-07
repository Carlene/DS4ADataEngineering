# TODO: Continue looping through this function until I get the correct amount of jobs (getting 14, should be 25) 
# Since "find" stops at the first instance of finding a substring, have to keep looping until there's no more new jobs
# job_counter needs to eventually equal the amount of jobs on page or reloop

def grab_job_paths(job_data):
    """ Used to find job links within the Meta Job Search page source"""
    job_url = "/v2/jobs/"
    paths = []
    # job_counter = 0
    for line in job_data:
        if line.find(job_url) > -1:
            # job_counter+=1
            link_start = line.find(job_url)
            link_end = line.find("/", link_start + len(job_url)) #making sure to grab the end of the job url
            paths.append(line[link_start : link_end])
    # return job_counter, paths
    return paths

def add_meta_url(paths):
    """Concats the start of the url to the list of job paths"""
    full_links = []
    url_start = "https://www.metacareers.com"
    for path in paths:
        full_links.append(url_start + path)
    return full_links

# print(add_meta_url(grab_job_link_paths()[1]))