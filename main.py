n = int(input("Enter the number of students: ")) # Get the number of students from the user
student_marks = {}# Create a dictionary to store the student names and scores

for i in range(n):# Loop through the input and add each name and score to the dictionary
  print(f"Enter the name and scores for student #{i+1}:")
  name, *line = input("Name and scores (space-separated): ").split()
  scores = list(map(float, line))
  student_marks[name] = scores

query_name = input("Enter the name of the student to calculate the average score: ")# Get the name of the student to calculate the average score

if query_name in student_marks: # Calculate the average score for the given student
  avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
  print(f"The average score for {query_name} is: {avg_score:.2f}")
else:
  print(f"{query_name} is not in the list of students.")