# Labor Exploitation
Pulling together global human trafficking data in comparison to country wealth and labor force

//Process of Extraction, Transformation, and Loading//

Data Sources
1. Counter Trafficking Data Collaborative: https://www.ctdatacollaborative.org/download-global-dataset
   
   This dataset is the backbone of the project. Human Trafficking has always existed but it wasn't until 2020 that the US
   passed a law declaring it as a crime. This means that the exploitation of people was not tracked or measured with the 
   exception of the last 20 years. The lack of accurate, consistent data keeps us from identifying people who are suffering.
   The Counter Trafficking Data Collaborative is seeking to provide a solution by aggregating data 
   from five global agencies. This project was the perfect opportunity to attempt a database design for this challenging
   dataset.
   
2. World Bank API - Wealth of Countries: https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation
  Our main dataset focused on exploitation of people for labor. We decided to access the World Bank API to pull financial
  data on each country. The World Bank data provides the opportunity to explore instances of trafficking in relation to the     countries financial status. 

3. World Bank CSV - Labour Force By Year: https://data.worldbank.org/indicator/SL.TLF.TOTL.IN 
  Similarly with the fiancial data for each country, we wanted to pull in data related to the yearly labor force 
  from 2012 - 2017. 

Transformation

  Jessica: Restructured the main dataset to focus on reports and details of labor trafficking (the original included sex
  trafficking data, as well as recruiting relationships). Many rows contained "-99" as a value. At first we considered 
  removing or changing most of these values. After reading the documnentation associated with the data, we realized it was
  relevant to keep them in the database.
  
  Mahatmi: Deleted duplicate data from the country codes csv file. The Alpha-2 codes contained "" around the codes in her csv.
  She removed the "" from the codes so that they could act as keys in the database. 
    
  Jeff: Looped through the API response to create a list of dictionaries that were appended to a list. Converted to a
  dataframe and removed the aggregates entry. 
 
  
Database

  Initailly we determined that SQL would  provide a clear structure to our data. We wanted to use the country codes as the
  primary key for our tables. Definitely would use MongoDB next time. 
  
  Schema:https://files.slack.com/files-pri/TM10668R1-FS7B13PDZ/erd_image.png
  
Hypothetical Use Case

   Labor trafficking is a overly unidentified crime. Comparing instances of labor trafficking with the wealth 
   and labor force of a nation, will allow agencies to recognize trends of source and destination countries.
