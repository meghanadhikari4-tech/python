from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

emails = [
"Win a free iPhone now",
"Meeting at 5 pm today",
"Congratulations you won money",
"Lets study together tomorrow"
]

labels = [1,0,1,0]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)
model = MultinomialNB()
model.fit(X, labels)
test = ["You won a free ticket"]
test_vector = vectorizer.transform(test)
prediction = model.predict(test_vector)
print(prediction)
