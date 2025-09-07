# Exception
errorFile =""
try:
  errorFile = open("error","a")
  errorFile.write("Go fuck yourself \n",)
except Exception as error:
  print(error)
finally:
  print("done processing file")