# function to get names and emails
def get_name(filename):
	name_list = []
	emails = get_email(filename)
	for email in emails:
		index = email.find("@")
		name_list.append(email[:index])
	return name_list



def get_email(filename):
	email_list = []
	with open(filename) as fhand:
		for line in fhand:
			line = line.rstrip()
			if line.startswith("From:"):
				email_list.append(line[6:])
	return email_list

get_name("mbox-short.txt")

# storing the names and email as dictionary key value pair
