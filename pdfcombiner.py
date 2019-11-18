import PyPDF2
import sys

new_file_name = sys.argv[1]
inputs = sys.argv[2:]

def pdf_combiner(pdf_list):
	try:
		merger = PyPDF2.PdfFileMerger()
		for pdf in pdf_list:
			print(pdf)
			merger.append(pdf)
		merger.write(new_file_name)
		print('All done!')
	except FileNotFoundError:
		print('File not found')
	except:
		print('Something went wrong')

pdf_combiner(inputs)
