# importing required modules
from collections import Counter
import PyPDF2

files = ["exams/2015_ANS.pdf", "exams/2016_ANS.pdf", "exams/2017_ANS.pdf", "exams/2018_ANS.pdf"]

dict_year_exercise_to_core_curriculum = dict()
dict_core_curriculum_to_year_exercise = dict()
ans_counter = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

for file_name in files:
    with open(file_name, 'rb') as file:
        pdfReader = PyPDF2.PdfFileReader(file)
        # for i in range(pdfReader.numPages):
        year = file_name[6:10]
        for i in range(1, 5):  # on pages [1, 2, 3, 4] there are answers for closed questions
            pageObj = pdfReader.getPage(i)
            exercises_on_page = pageObj.extractText().replace('\n', '').split("Zadanie ")[
                                1::]  # first el is "Strona x z y"
            for exercise_str in exercises_on_page:
                ex_num = exercise_str.split('.')[0]
                l = exercise_str.rfind('(') + 1
                r = exercise_str.rfind(')')
                list_of_core_curriculum = exercise_str[l:r:].replace('\n', '').split(", ")
                dict_year_exercise_to_core_curriculum[year + "_" + ex_num] = list_of_core_curriculum
                for el in list_of_core_curriculum:
                    try:
                        dict_core_curriculum_to_year_exercise[el].append(year + "_" + ex_num)
                    except:
                        dict_core_curriculum_to_year_exercise[el] = [year + "_" + ex_num]
                # print(year + "_" + ex_num)
                right_ans = exercise_str.split("Wersja II ")[1][0]
                ans_counter[right_ans] += 1

# print(ans_counter)
# print(dict_year_exercise_to_core_curriculum)
# print(dict_core_curriculum_to_year_exercise)

# print("sorted by core curriculum name")
# for cc in sorted(dict_core_curriculum_to_year_exercise):
#     print(cc)
#     for ll in dict_core_curriculum_to_year_exercise[cc]:
#         print("\t", ll)

print("sorted by core curriculum popularity")
for cc in sorted(dict_core_curriculum_to_year_exercise, key=lambda elem: -len(dict_core_curriculum_to_year_exercise[elem])):
    print(cc + " (" + str(len(dict_core_curriculum_to_year_exercise[cc])) + ")")
    for ll in dict_core_curriculum_to_year_exercise[cc]:
        print("\t", ll)
