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
  
  Mahathi: The CSV file has country name, 2- digit , 3-digit , numeric country codes, also average Latitude and Longitude. 
  We grabbed the columns Country, 2-digit country code in a dataframe, the 2-digit code has (""), So the string "replace"
  function is used to filled the quotes("") with white spaces and the datframe is exported as CSV, which can be used for
  importing in the database table.
    
  Jeff: As we wanted to be able to see if the income level of a country might impact exploitation trends, we made use of the
  World Bank API to obtain income level for each country in the world.  The API also returned other data, such as latitude and
  longitude, that we did not deem important, so we retained only the country code and country income.  These variables would
  allow us to complete future research objectives.
 
  
Database

  Initailly, we determined that SQL would provide a clear structure to our data. We wanted to use the country codes as the
  primary key for our tables. Definitely would use MongoDB next time. 
  
  Schema:https://files.slack.com/files-pri/TM10668R1-FS7B13PDZ/erd_image.png
  
Hypothetical Use Case

   Labor trafficking is a overly unidentified crime. Comparing instances of labor trafficking with the wealth 
   and labor force of a nation, will allow agencies to recognize trends of source and destination countries.
