# NLP_PROJECT_summary
Topic : Genre Detection from the Books abstracts Introduction: Books are one of the most important sources of knowledge and entertainment for humans. Determining the genre of books (such as psychology, crime, or romance) requires reading the entire book, which takes a lot of time.

Determining the genre of a book is important for two reasons: 1. To help those who are looking for books that match their tastes and interests. 2. For bookstores and publishers, it allows them to present their books to a specific group of readers with similar tastes and interests.

In this project, we aim to automatically detect the genre of a book (psychology, crime, or romance) from its abstract using data collected from the Goodreads website. We will collect data related to these two genres and train a model to detect the genre of a book from its abstract.

Information about the Goodreads website: This site allows readers to read books, review them, read other people's reviews, and talk to their friends about the books they have read. Founded in 2006 by Otis Chandler and Elizabeth Khuri, it is now a subsidiary of Amazon. It currently serves over 75 million users worldwide and has more than 2.5 billion reviews of various books on its website.

Method and Data: The data is in English and the writing style is formal. We will use the Beautifulsoup library to collect information about book abstracts from the Goodreads website. This site has an abstract for each book, and you can view books based on genre in the search section. Since this site has 97,000 books for the psychology genre, 97,000 books for the crime genre, and 266,000 books for the romance genre, we will limit the data to a smaller sample size to train our model.
