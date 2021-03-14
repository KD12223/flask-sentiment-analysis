# Sentiment Analysis API

This is a sentiment analysis API that allows users to see the sentiment of any text they wish to have analyzed. Requests
are processed using Flask. AWS Comprehend is used to analyze the text.

The API requires that users send a POST request to the `/analyze` route. The POST must contain a JSON body with a
`content` object. For example, `{ "content": "This is really cool!" }` is in a valid format.
