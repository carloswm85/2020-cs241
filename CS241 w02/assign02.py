"""
FILE: assign02.py
AUTHOR: Carlos W. Mercado
PROCESSING:
    - Informs the average commercial rate in a file.
    - Informs data about the utility companies with
    the highest and lowest commercial rates.
        
"""

def average_comm_rate(filename):
    '''
        INPUT: The name of a file.
        PROCESSING:
            - Loops through every line in the file.
            - Gets the commercial rate of every company.
            - Gets the average from all the commercial rates in the file.
        OUTPUT: Commercial rates average.
    '''
    file = open(filename, 'r')
    total_cr = 0
    counted_cr = 0
    for line in file:
        if not line.startswith('zip'):
            data = line.split(',')
            total_cr += float(data[6])
            counted_cr += 1
    average_cr = total_cr / counted_cr
    return average_cr

def highest_comm_rate_data(filename, high_mode):
    '''
        INPUT:
            - The name of a file.
            - Boolean value for setting the mode.
        PROCESSING:
            - Retrieves selected data from a chosen utility company,
            depending on the boolean value of high_mode.
            - MODE:
                > True: Data from the company with highest commercial rate.
                > False: Data from the company with highest commercial rate.
        OUTPUT: Selected data from a utility company.
    '''
    file = open(filename, 'r')
    lower_limit_cr = 0.0
    upper_limit_cr = 1.0
    for line in file:
        if not line.startswith('zip'):
            data = line.split(',')
            cr = float(data[6])
            if cr > lower_limit_cr and high_mode:
                lower_limit_cr = cr
                comm_rate = cr
                utility_name = data[2]
                zip_cr = data[0]
                state = data[3]
            elif cr < upper_limit_cr and not high_mode:
                upper_limit_cr = cr
                comm_rate = cr
                utility_name = data[2]
                zip_cr = data[0]
                state = data[3]
    file.close()
    requested_data = utility_name + ' (' + zip_cr + ', ' + state + ') - $' + str(comm_rate)
    return requested_data
    
def main():
    '''
        INPUT: From user, receives the name of a file.
        PROCESSING:
            - Implements 3 functions over the data of
            many utility companies.
        OUTPUT:
            - Average commercial rate of all companies in the file.
            - Selected data from the company with the highest commercial rate.
            - Selected data from the company with the lowest commercial rate.
    '''
    filename = input('Please enter the data file: ')
    average_cr = average_comm_rate(filename)
    highest_data = highest_comm_rate_data(filename, True)
    lowest_data = highest_comm_rate_data(filename, False)
    print('\nThe average commercial rate is:', average_cr)
    print('\nThe highest rate is:')
    print(highest_data)
    print('\nThe lowest rate is:')
    print(lowest_data)
    
if __name__ == '__main__':
    main()
    
    
