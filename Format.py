print ("Format Paragraphs: v0.1.1\nBlueCereal\n")

punc = ['.', '!', '"', '\'', ',', '-', '?', ';', ' ']

def format(userText, linesize):	
	TotalLines = []
	while (len(userText) != 0):

		tempLine = (userText[:linesize])

		if (len(tempLine) < linesize):
			TotalLines.append(''.join(tempLine))
			userText = ''
			break

		if (tempLine[linesize-1] not in punc):
			if (userText[linesize] in punc):
				TotalLines.append(''.join(tempLine))
				userText = userText[linesize+1:]

			else:
				numberator = 0
				referPoint = linesize-1
				
				while (tempLine[referPoint-numberator] not in punc):
					tempLine = tempLine[:-1]							
					numberator += 1	
				
				userText = userText[referPoint-numberator+1:]
				TotalLines.append(''.join(tempLine))

		else:
			TotalLines.append(''.join(tempLine))
			userText=userText[linesize:]
			
	return (TotalLines)

print ("Enter the Size of each Line:\t")
linesize = int(input())

#This is where file handling (if required) goes

print ("\nEnter Line:\t")
userText =  str(input())

formattedLines = format(userText, linesize)

for line in formattedLines:
	print (line)

print ("\n---Completed Task---")




