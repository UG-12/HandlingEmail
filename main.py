# function to get names and emails
def get_name(filename):
	pass


def get_email(filename):
	email_list = []
	with open(filename) as fhand:
		for line in fhand:
			line = line.rstrip()
			if line.startswith("From:"):
				email_list.append(line[6:])
	print(email_list)

get_email("mbox-short.txt")

# storing the names and email as dictionary key value pair