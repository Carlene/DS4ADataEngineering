# import organize_job_details as organize
# import filter_job_results as fjr
# import open_multiple_links as opening
# import scraper 
# import clean

# if __name__ == "__main__":
#     job_elements = scraper.scrape_HTML()
#     list_of_jobs = clean.split_and_clean(job_elements, "</tr>")
#     job_details_by_id = organize.separate_job_posts(list_of_jobs)[0]
#     list_of_paths = organize.separate_job_posts(list_of_jobs)[1]
#     messy_descriptions_by_job_id = opening.grab_job_data_from_multiple_links(list_of_paths)

#     for job_id, messy_descriptions in messy_descriptions_by_job_id.items():
#         for messy_description in messy_descriptions:
#             jobs_no_summary_by_job_id = fjr.replace_job_summary(messy_description)
#             no_disney_description = fjr.remove_disney_company_description(jobs_no_summary_by_job_id)
#             print(fjr.find_qualifications(no_disney_description))