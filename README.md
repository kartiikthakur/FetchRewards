# FetchRewards - Text Similarity

This challenge will focus on the similarity between two texts. The objective is to write a program that takes as inputs two texts and uses a metric to determine how similar they are. Documents that are exactly the same should get a score of 1, and documents that don’t have any words in common should get a score of 0.

## Technologies used
* Python
* Flask

## Building and Running the Application

1. Clone the repo  
2. Navigate to cloned folder in terminal  

For the below commands, please make sure you're in the root directory of the application.   
  
Before running the application, please run the below command to install all the python libraries.  

`pip install -r requirements.txt ` 
  
Use the below command on your terminal to build the application.  

`python app.py`

## Note
If some other service is running on port 5000, please edit app.py python file to some other port number that's free.

## Testing the Web Service

The web service expose only one endpoint -- /textSimilarity which accepts two string arguments string1 and string2

Once the application is running, enter the URL below with the text samples you want to test.
 Usage:
`http://localhost:5000/textSimilarity?sample1=<{yourValueForString1}>&sample2=<{yourValueForString2}> `
 
 Can either use postman or web browser to test the end point.
 
 or open another linux terminal and run the following command:
` curl -v http://localhost:5000/textSimilarity?sample1=test&sample2=lol`  
  
## Example

`http://localhost:5000/textSimilarity?sample1=test&sample2=lol`  

`http://localhost:5000/textSimilarity?sample1=test&sample2=test`   
  
`http://localhost:5000/textSimilarity?sample1=Earn free rewards just by scanning your grocery receipts&sample2=Scan every grocery receipt after you shop and Fetch Rewards finds you savings.`  


## Complexity Analysis

Time Complexity: O(m + n)  
where m is the length of text1 and n is the length of text2.

Space Complexity: O(m + n)  
where m is the length of text1 and n is the length of text2.


## Note
Please make sure you change the port number in the URL as well if you change the port number in the app.py file
