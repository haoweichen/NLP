1. Define a function "tokenize" as follows:
 * takes a string as an input
 * tokenizes the string into tokens using a <strong>customized NLTK regular expression tokenizer</strong>. A token <strong>only contains letters, "-", or "."</strong> . Moreover, in a token, <strong>"-" or "." cannot be the first character</strong>.
 * returns the list of tokens as the output

2. Define a function "sentiment_analysis" as follows:
 * takes a string as an input
 * invokes "tokenize" function defined above to get tokens
 * removes stop words and convert all tokens into lower cases
 * counts positive words and negative words in the remaining tokens using words from positive-words.txtPreview the documentView in a new window and negative-words.txtPreview the documentView in a new window respectively
 * determines the sentiment of the string as follows:
   * if the number of positive words > the number of negative words, the sentiment is positive
   * if the number of positive words < the number of negative words, the sentiment is negative
   * if the number of positive words = the number of negative words, the sentiment is neutral
   * return the sentiment as the output

3. Define a function to evaluate the accuracy of the sentiment analysis in (2) as follows:
 * takes an input file which has a list of reviews each with review text and a label (positive, negative, neutral). See "finding_dory_reviews.Preview the documentView in a new windowcsv" as an example
 * reads the input file to get a list of reviews including text and sentiment of each review
 * for each review, predicts its sentiment using the function defined in (2)
 * returns the accuracy as the number of correct sentiment predictions/total reviews
