# invoice ident (id) or customers last name (name)
#try/except error message - print statment
with open ('sales_data.csv','r') as csvfile:
    file_data = csvfile.read()
    file_data = file_data.split('\n')
#open data file then search within the column for input value
#print results
if ' ' in file_data:
    file_data.remove('')
user_entry = input('Search by invoice id (id) or customer last name (lname)? ')
while user_entry not in ['id','lname']:
    print('Error: You must enter either \'id\' for invoice id search or \'lname\' for customer last name search')
    
#user_entry = input('Search by invoice id (id) or customer last name (lname)? ')
search_term = input('Enter search term: ')
term_searched = 0
if user_entry == 'id':
    for information in file_data:
        if information.split(',')[0] == search_term:
            term_searched = term_searched + 1
            print (information)
        print('{0} records found.'.format(term_searched))
    else:
        if user_entry == 'lname':
            for information in file_data:
                if information.split(',')[1] == search_term:
                    term_searched = term_searched + 1
                    print(information)
                print('{1} records found.'.format(term_searched))