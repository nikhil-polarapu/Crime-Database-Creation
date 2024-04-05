# DATASHEET FOR ASSIGNMENT 2

## DATASET OVERVIEW

### BASICS: CONTACT, DISTRIBUTION, ACCESS

1. **Dataset name**
Norman Police Department Daily Incident Summary
2. **Dataset version number or date**
The website has incident report data for the years 2022 to 2024.
1. **Dataset owner/manager contact information, including name and email**
City of Norman, OK
PublicAffairs@normanok.gov
1. **Who can access this dataset (e.g., team only, internal to the company, external to the company)?**
This is a public dataset. Anyone on internet can access the dataset.
1. **How can the dataset be accessed?**
The dataset can be accessed from this link: https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports

### DATASET CONTENTS

6. **What are the contents of this dataset? Please include enough detail that someone unfamiliar with the dataset who might want to use it can understand what is in the dataset.**
**Specifically, be sure to include:**
    - **What does each item/data point represent (e.g., a document, a photo, a person, a country)?**
    - **How many items are in the dataset?**
    - **What data is available about each item (e.g., if the item is a person, available data might include age, gender, device usage, etc.)? Is it raw data (e.g., unprocessed text or images) or features (variables)?**
    - **For static datasets: What timeframe does the dataset cover (e.g., tweets from January 2010–December 2020)?**
  
    The dataset contains data related to the incidents that are reported to the Norman Police Department. It contains a table with the following columns:
    - Date/Time: The date and time the incident was reported
    - Incident Number: A unique number given to the incident
    - Location: Address where the incident was reported
    - Nature: Nature of the incident
    - Incident ORI: It is the Originating Record Identifier that is a unique alphanumeric code used to identify the agency or organization that created or reported an incident
    The website has daily incident summary data for the years of 2022, 2023 and 2024 (till April).

### INTENDED & INAPPROPRIATE USES

7. **What are the intended purposes for this dataset?**
The purpose of this dataset is to let the people know about the history of incidents that are reported to the Norman Police Department.
8. **What are some tasks/purposes that this dataset is not appropriate for?**
This dataset may not be appropriate for predicting future crimes, determining causality, ranking communities based on safety and making any legal decisions.

## DETAILS

### DATA COLLECTION PROCEDURES

9. **How was the data collected?**
**Describe data collection procedures and instruments.**
**Describe who collected the data (e.g., contractors).**
The data is collected based on the reports from officers of various departments such as Fire, Medical or Police that have been to the site of the incident. Sometimes, these incidents are based on the data given by the people themselves.
10. **Describe considerations taken for responsible and ethical data collection (e.g., procedures, use of crowd workers, recruitment, compensation).**
The dataset doesn't leak any private data of the people involved in the incident such as their names, contact details or their criminal record. It does not make public the same for the officers that responded to the incident.
11. **Describe procedures and include language used for getting explicit consent for data collection and use, and/or revoking consent (e.g., for future uses or for certain uses). If explicit consent was not secured, describe procedures and include language used for notifying people about data collection and use.**
The parties involved in the incident are explained regarding the details of the incident that will be made available to the public, they explain the ways in which this data will be beneficial and how it doesn't share confidential details.

### REPRESENTATIVENESS

12. **How representative is this dataset? What population(s), contexts (e.g., scripted vs. conversational speech), conditions (e.g., lighting for images) is it representative of?**
**How was representativeness ensured or validated?**
**What are known limits to this dataset’s representativeness?**
The representativeness of the dataset cannot be measured since the dataset only has the data related to incidents and doesn't talk anything about the people, their gender or race.
13. **What demographic groups (e.g., gender, race, age, etc.) are identified in the dataset, if any?**
**How were these demographic groups identified (e.g., self-identified, inferred)?**
**What is the breakdown of the dataset across demographic groups? Consider also reporting intersectional groups (e.g., race x gender) and including proportions, counts, means or other relevant summary statistics.**
**Note: This information can help a user of this dataset understand what groups are represented in the dataset. This has implications for the performance of models trained on the dataset and on its appropriateness for fairness evaluations – e.g., comparisons of performance across groups.**
The dataset does not identify any demographic groups.

### DATA QUALITY

14. **Is there any missing information in the dataset? If yes, please explain what information is missing and why (e.g., some people did not report their gender).**
**Note: Consider the impact of missing information on appropriate uses of this dataset.**
Some rows have location missing from the dataset. This could be because some owners did not give consent to sharing their address in a public dataset. Some rows also have nature missing, this could be due to manual error while reporting.
15. **What errors, sources of noise, or redundancies are important for dataset users to be aware of?**
**Note: Consider how errors, noise, redundancies might impact appropriate uses of this dataset.**
Some rows have missing values. Some location entries have address on two lines and some location entries have their coordinates instead of the address in the dataset.
16. **What data might be out of date or no longer available (e.g., broken links in old tweets)?**
Since, this is a data of all the incidents reported to Norman PD, this question is not applicable to this dataset.
17. **How was the data validated/verified?**
This data is pre-validated, as it comes from a city government's website.
18. **What are potential validity issues a user of this dataset needs to be aware of (e.g., survey answers might not be truthful, age was guessed by a model and might be incorrect, GPA was used to quantify intelligence)?**
There may have been some false reports or people playing pranks that were included as reports.
19. **What are other potential data quality issues a user of this dataset needs to be aware of?**
All the data quality issues have been addressed in question 15.

### PRE-PROCESSING, CLEANING, AND LABELING

20. **What pre-processing, cleaning, and/or labeling was done on this dataset?**
**Include information such as: how labels were obtained, treatment of missing values, grouping data into categories (e.g., was gender treated as a binary variable?), dropping data points.**
**Who did the pre-processing, cleaning, and/or labeling (e.g., were crowd workers involved in labeling?)**
**Note: Consider how this might impact appropriate users of this dataset (e.g., binary gender might be insufficient for fairness evaluations; imputing missing values with the mean may create anomalies in models trained on the data).**
I wrote a script to go through each page of the report, extract only the table from the page and remove all the other unnecessary lines. I then removed the table headers and divided rows into individual items in a list. These individual rows are further split based on column. I handled missing values in the dataset and I also handled the locations that have coordinates instead of addresses.
21.  **Provide a link to the code used to preprocess/clean/label the data, if available.**
Here is the link to the code used to preprocess the data: https://github.com/nikhil-polarapu/cis6930sp24-assignment2/blob/main/src/assignment1_helper.py
22.  **If there are any recommended data splits (e.g., training, development/validation, testing), please explain.**
Since, we are not performing any prediction or machine learning using the data, splitting the data is not necessary.

### PRIVACY
23. **What are potential data confidentiality issues a user of this dataset needs to be aware of?**
**How might a dataset user protect data confidentiality?**
Since the dataset has the locations of the people involved in the incident, a user should be mindful not to share the data to people with ill intentions. Also, the user should not perform his/her own investigation into any of the incidents reported.
24. **Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?**
**Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals race, sexual orientation, age, ethnicity, disability status, political orientation, religious beliefs, union memberships; location; financial or health data; biometric or genetic data; criminal history)?**
**If the answer to either of these questions is yes, please be sure to consult with a privacy expert and receive approvals for storing, using, or distributing this dataset.**
This dataset has the addresses of the places where the incidents were reported. While, the address in itself is not confidential, if it is combined the name of the person residing in the place it becomes confidential. Since, the data does not reveal any individual information it is not possible to identify the individuals directly.
25. **If an analysis of the potential impact of the dataset and its uses on data subjects (e.g., a data protection impact analysis) exists, please provide a brief description of the analysis and its outcomes here and include a link to any supporting documentation.**
No such analysis exists in the Norman PD website. But I've given my analysis in question 25.
26. **If the dataset has undergone any other privacy reviews or other relevant reviews (legal, security) please include the determinations of these reviews, including any limits on dataset usage or distribution.**
I am not aware of any privacy reviews or other relevant reviews (legal, security) that the data has went through.

### ADDITIONAL DETAILS ON DISTRIBUTION & ACCESS

27. **How can dataset users receive information if this dataset is updated (e.g., corrections, additions, removals)?**
**Note: Consider creating a distribution list people can subscribe to.**
Since this dataset has data that has already been reported and it is only published to the site after a few weeks of the incident, there won't be any updates to the data. If the dataset must be updated, that won't affect users as they would be reading it directly from the website.
28. **For static datasets: What will happen to older versions of the dataset? Will they continue to be maintained?**
The website has data divided based on the years. So the older versions of the data will be maintained in the website.
29. **For streaming datasets: If this dataset pulls telemetry data from other sources, please specify:**
    - **What sources**
    - **How frequently the dataset is refreshed**
    - **Who controls access to these sources**
    - **Whether access to these sources will remain available, and for how long**
    - **Any applicable access restrictions to these sources including licenses and fees**
    - **Any other available access points to these sources**
    - **Any relevant information about versioning**

    **Are there any other ways in which these sources might affect this dataset that a dataset user needs to be aware of?**
    This dataset does not collect any telemetry data, hence this question is not applicable.
30. **If this dataset links to data from other sources (e.g., this dataset includes links to content such as social media posts or, news articles, but not the actual content), please specify:**
    - **What sources**
    - **Whether access to these sources will remain available, and for how long**
    - **Who controls access to these sources**
    - **Any applicable access restrictions to these sources including licenses and fees**
    - **For static datasets: If an official archival version of the complete dataset exists (i.e., including the content as it was at the time the dataset was created), where it can be accessed**

    **Are there any other ways in which these sources might affect this dataset that a dataset user needs to be aware of?**
    This dataset does not link to data from other sources, hence this question is not applicable.
31. **Describe any applicable intellectual property (IP) licenses, copyright, fees, terms of use, export controls, or other regulatory restrictions that apply to this dataset or individual data points.**
**These might include access restrictions related to data subjects’ consenting or being notified of data collection and use, as well as revoking consent.**
**Provide links to or copies of any such applicable terms.**
Since this is a publicly available dataset, the restrictions mentioned in the question does not apply.