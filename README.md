# word-opposites-quiz-game

Task 2:
The second application is a word-opposites quiz game to help young students practice
language. The program must randomly select two different pairs of words from either of
the lists below, and then display a question based on the selection. You must ensure that
you are not selecting the same synonym-antonym pair i.e. repeating the question.

Table 1Word lists
hot, summer, hard, dry, simple,
light, weak, male, sad, win, small,
ignore, buy, succeed, reject,
prevent, exclude
cold, winter, soft, wet, complex,
darkness, strong, female, happy,
lose, big, pay attention, sell, fail,
accept, allow, include
The quiz takes the following form:
(* assuming the words hot and happy were randomly selected.)


“Q1: Hot is to cold, as happy is to …. ?”
Answer: sad  user types this.
“Q2: Ignore is to pay attention, as darkness is to …. ?”
Answer: …..
The program will ask 10 questions. Ensure that each of the questions would not give
away the previous answers:
e.g.
“Q1: Hot is to cold, as happy is to …. ?”
“Q2: Ignore is to pay attention, as Hot is to …. ?”  the answer was printed in Q1! You
need to avoid this scenario.
Return the score to the student and show the correct answers for those that were
wrongly typed.
Extension:
This is a much harder extension, but if you feel like a challenge then read on. Extend the
program to read the wordlists from a file. The file is available here, look at the structure
of the document – you are required to parse the text and extract the contents. It is
presented as KEY, SYNONYM_LIST, ANTONYM_LIST. Select any two random keys, and
have the program quiz the student as before. Maintain a total running score as the
students answer the questions.
Note: The given wordlist is interesting, there are entries in the text that are enclosed in
square brackets, with a reference [See XXXXX]. For extra kudos points, can you derive the
link and present the contents of the link as an extension to the relevant KEY entry?
