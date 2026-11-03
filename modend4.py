feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': [
        'Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
        'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'
    ],

    'Feedback': [
        '   Very GOOD Service!!!',
        'poor support,        not happy   ',
        'GREAT experience! will come again.',
        'okay     okay...',
        '   not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

print(feedback_data)
n = int(input("How many feedbacks do you want to add? "))

for i in range(n):

    name = input("Enter customer name: ")

    feedback = input("Enter written feedback: ")

    rating = int(input("Enter rating (1-5): "))

    while rating < 1 or rating > 5:
        print("Invalid rating! Enter a rating between 1 and 5.")
        rating = int(input("Enter rating: "))

    sno = len(feedback_data['S_No']) + 1

    feedback_data['S_No'].append(sno)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

print("Updated feedback data:")
print(feedback_data)
for i in range(len(feedback_data['Feedback'])):

    text = feedback_data['Feedback'][i]

    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("!", "")
    text = text.replace("?", "")

    text = " ".join(text.split())

    text = text.lower()

    feedback_data['Feedback'][i] = text

print("Cleaned feedback:")
print(feedback_data['Feedback'])
def count_word_in_feedbacks(word):

    count = 0

    for feedback in feedback_data['Feedback']:

        words = feedback.split()

        if word.lower() in words:
            count += 1

    return count


print("Feedbacks containing good:",
      count_word_in_feedbacks("good"))

print("Feedbacks containing poor:",
      count_word_in_feedbacks("poor"))

print("Feedbacks containing excellent:",
      count_word_in_feedbacks("excellent"))
print("\nFINAL CLEANED FEEDBACK DATA")

for key, value in feedback_data.items():
    print(key, ":", value)
total = sum(feedback_data['Rating'])

count = len(feedback_data['Rating'])

average = total / count

print("Average Rating:", round(average, 2))
max_words = 0
longest_feedback = ""

for feedback in feedback_data['Feedback']:

    word_count = len(feedback.split())

    if word_count > max_words:
        max_words = word_count
        longest_feedback = feedback

print("Longest Feedback:", longest_feedback)
print("Word Count:", max_words)
unique_words = []

for feedback in feedback_data['Feedback']:

    words = feedback.split()

    for word in words:

        if word not in unique_words:
            unique_words.append(word)

print("Unique Words:")
print(unique_words)
sorted_data = sorted(
    zip(
        feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']
    ),
    key=lambda x: x[2],
    reverse=True
)

print("Feedbacks sorted by rating:")

for item in sorted_data:
    print(item)

