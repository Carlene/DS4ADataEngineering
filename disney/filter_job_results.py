# Separating all of the information I need by formatting used in the HTML 

def find_id(job):
    """Finds the job posting id for reference"""
    id_start = "data-job-id="
    id_end = "<h2>"

    starting_i = job.find(id_start) 
    ending_i = job.find(id_end) 
    id = job[starting_i + len(id_start) : (ending_i- 2)] # subratracing two from ending id to get rid of "> "
    id = id.replace("\"", "")
    return id

def find_path(job):
    """Finds the path to the job posting"""
    path_start = "a href="
    path_end = "data-job-id="

    starting_i = job.find(path_start) +1 #to get rid of leading "
    ending_i = job.find(path_end) -2 #to get rid of " and whitespace

    path = job[starting_i + len(path_start) : ending_i]
    return path

def find_title(job):
    """Finds the title of the position the job posting is for"""
    title_start = "<h2>"
    title_end = "</h2>"

    starting_i = job.find(title_start)
    ending_i = job.find(title_end)

    title = job[starting_i + len(title_start) : ending_i]
    return title

def find_brand(job):
    """Finds the specific Disney Org that this job posting is under (eg. ESPN, Disney Streaming Services, etc)"""
    brand_start = "job-brand industry"
    brand_end = "</span>"

    starting_i = job.find(brand_start) + 2 # to avoid " and >
    ending_i = job.find(brand_end, starting_i) # to start looking for spans after the brand start

    brand = job[starting_i + len(brand_start) : ending_i]
    return brand

def find_locations(job):
    """Finds location inside job posting. Job locations are formatted as City, State, Country"""
    location_start = "job-location"
    location_end = "</span>"

    starting_i = job.find(location_start) + 2 #to avoid " and >
    ending_i = job.find(location_end, starting_i) # to start looking for spans after the location start

    location = job[starting_i + len(location_start) : ending_i]

    locations = location.split("/") #multiple locations in HTML split up by a backslash
    return locations

def find_posting_date(job):
    """Finds the day that this job posting was added to the Disney Jobs site"""
    posting_date_start = "job-date-posted"
    posting_date_end = "</span>"

    starting_i = job.find(posting_date_start) + 2 #to avoid " and >
    ending_i = job.find(posting_date_end, starting_i+1) # to start looking for spans after the brand start

    posting_date = job[starting_i + len(posting_date_start) : ending_i]
    return posting_date

def separate(jobs):
    """Separates job postings into necessary fields: job_id, job_path, job location, job title, job brand"""
    job_details_by_id = {}
    job_details = {}
    paths = []

    for job in jobs:
        if len(job) > 0:
            path = find_path(job)
            id = find_id(job)
            title = find_title(job)
            brand = find_brand(job)
            locations = find_locations(job)
            posting_date = find_posting_date(job)
            job_details["path"] = path
            job_details["title"] = title
            job_details["brand"] = brand
            job_details["locations"] = locations
            job_details["posting_date"] = posting_date
            job_details_by_id[id] = job_details
            job_details = {}
            paths.append(path)

    return job_details_by_id, paths


def replace_job_summary(job_description):
    """Removes unecessary start of job description"""
    look_for = "<h4>"

    starting_i = job_description.find(look_for)
    ending_i = job_description.find(look_for, starting_i) # to start looking for header tags after the first one

    job_summary = job_description[starting_i + len(look_for) : ending_i]

    job_description_without_summary = job_description.replace(job_summary, "")
    return job_description_without_summary

#TODO: GET THIS TO REMOVE THE SUMMARY OMG
def remove_job_summary(description_dict):
    description_by_job_id = {}
    descriptions_list = []
    for id, desc in description_dict.items():
        for item in desc:
            desc_no_summary = replace_job_summary(item)
            descriptions_list.append(desc_no_summary)
        description_by_job_id[id] = descriptions_list
        descriptions_list = []
    return description_by_job_id