# importing required modules 
import PyPDF2 
  
files = ["exams/2015_ANS.pdf", "exams/2016_ANS.pdf", "exams/2017_ANS.pdf", "exams/2018_ANS.pdf"]


for file_name in files:
	with open(file_name, 'rb') as file:
		pdfReader = PyPDF2.PdfFileReader(file) 
  		for i in range(pdfReader.numPages):
  			pageObj = pdfReader.getPage(i)
			print("##################")
			print("##################")
			print(pageObj.extractText())
			print("##################")
