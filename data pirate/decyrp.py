from PyPDF2 import PdfFileReader, PdfFileWriter
def decrypt_pdf(input_path, output_path, password):
  input_file =open(input_path, 'rb')
  output_file =   open(output_path, 'wb') 
  reader = PdfFileReader(input_file)
  reader.decrypt(password)
  writer = PdfFileWriter()
  for i in range(reader.getNumPages()):
      writer.addPage(reader.getPage(i))
  writer.write(output_file)

decrypt_pdf('C:/Users/Nirmal/Desktop/CNS_Ch01_AJ.pdf', 'C:/Users/Nirmal/Desktop/decrypted.pdf', 'mypass')