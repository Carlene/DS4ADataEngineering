####################### Standard Libraries #####################################
####################### My Libraries ###########################################
from scraper import grab_job_data_from_multiple_links
import filter_job_results as fjr

def separate_job_posts(list_of_jobs):
    """Separates details found on the job search page into necessary fields: 
    job_id: unique identifier 
    job_path: path to the job posting
    job location: which locations this job is available in 
    job title: the job position the posting is offering 
    job brand: which Disney brand this posting is for (eg. Disney Streaming, ESPN, etc.)
    """
    job_details_by_id = {}
    job_details = {}
    paths = []

    for job in list_of_jobs:
        if len(job) > 0:
            path = fjr.find_path(job)
            id = fjr.find_id(job)
            title = fjr.find_title(job)
            brand = fjr.find_brand(job)
            locations = fjr.find_locations(job)
            posting_date = fjr.find_posting_date(job)
            job_details["path"] = path
            job_details["title"] = title
            job_details["brand"] = brand
            job_details["locations"] = locations
            job_details["posting_date"] = posting_date
            job_details_by_id[id] = job_details
            job_details = {}
            paths.append(path)
    return job_details_by_id, paths


def map_job_details_with_qualifications(list_of_jobs, job_id = ""):
    """ 1. Grabs a dictionary of job search details by job id
        2. Grabs a dictionary of inner job posting details by job id
        3. Combines them together
    """
    all_job_details_by_id = {}
    job_details_by_id = separate_job_posts(list_of_jobs)[0]
    list_of_paths = separate_job_posts(list_of_jobs)[1]
    post_descriptions_by_job_id = grab_job_data_from_multiple_links(list_of_paths)

    # to search for a specific job posting, for testing
    if job_id != "":
        all_job_details_by_id[job_id] = job_details_by_id[job_id] | post_descriptions_by_job_id[job_id]
        print(f"All job details after combining: {len(all_job_details_by_id)}")
        return all_job_details_by_id
    # otherwise, to combine multiple postings
    for id in job_details_by_id:
        if id in post_descriptions_by_job_id:
            all_job_details_by_id[id] = job_details_by_id[id] | post_descriptions_by_job_id[id]
    print(f"All job details after combining: {len(all_job_details_by_id)}")
    return all_job_details_by_id