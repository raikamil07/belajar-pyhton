questions = ("apakah ibu kota indonesia?: ", 
            "berapa banyak pohon di taman?: ", 
            "berapa benua di dunia?: ", 
            "hewan apa yang dijuluki raja hutan?: ", 
            "berapa banyak samudra di dunia?: ")

options = (("A. Jakarta", "B. Bandung ", "C. Bogor ", "D. Depok "),
           ("A. 10", "B. 20", "C. 30", "D. 5"),
           ("A. 1", "B. 2", "C. 4", "D. 5"),
           ("A. semut", "B. singa", "C. gajah", "D. macan"),
           ("A. 1", "B. 5", "C. 4", "D. 3"))

answers = ("A", "C", "D", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 20
        print ("Benar!")
    else:
        print("Salah!")
        print(f"Jawaban yang benar adalah {answers[question_num]}")
    question_num += 1
print("-------------------------")
print(f"results {score}/ 100")
print(f"guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
print(f"answer: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("SELESAI")