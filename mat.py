# importing required modules 
import PyPDF2

files = ["exams/2015_ANS.pdf", "exams/2016_ANS.pdf", "exams/2017_ANS.pdf", "exams/2018_ANS.pdf"]

dict_year_exercise_to_core_curriculum = dict()

for file_name in files:
    with open(file_name, 'rb') as file:
        pdfReader = PyPDF2.PdfFileReader(file)
        # for i in range(pdfReader.numPages):
        year = file_name[6:10]
        for i in range(1, 5):  # on pages [1, 2, 3, 4] there are answers for closed questions
            pageObj = pdfReader.getPage(i)
            print("#] " + year, " p", i, "ex", 0)
            exercises_on_page = pageObj.extractText().split("Zadanie ")[1::]  # first el is "Strona x z y"
            for exercise_str in exercises_on_page:
                print(exercise_str.split('.')[0])
