import psycopg2
from config import config

import termtables as tt
from collections import Counter

## TODO : raintreele eraldi kasutaja, et saaksid andmeid RDL serverist pärida
## TODO : tõsta failid eraldi kausta, gerereeri uus reqs.txt, testi et töötab ilma django lisadeta

def test_connection():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Testing DB connetion')
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database test complete.')
            print("***********************")




'''
The script has to have the following functionality:
a) Display the following columns for each patient to the console:
    >> patient   >>   Patient number (pn),
    >> patient   >>   Patient last name (last), >> patient
    >> patient   >>   Patient first name (first), >> patient
    >> insurance >>   Insurance name, 
    >> insurance >>   Insurance from date (from_date) in US short date format (MM-DD-YY)
    >> insurance >>   Insurance to date (to_date) in US short date format (MM-DD-YY), 
    
    ordered by Insurance from date starting from earliest and then patient last name.
    
    Example output:
        000000002, Smith, John, Medicare, 01-01-09, 01-01-10
        000000002, Smith, John, Blue Cross, 06-01-09, 01-01-10
        000000001, Doe, John, Medicaid, 01-01-10, 01-01-11
        000000001, Doe, John, Blue Shield, 01-01-11, 01-01-12
    NB! Ordering must handled by script (or query) ie. it can not depend on the record insertion queue.
'''
# SQL query
patients_insurance_records_query = """SELECT 
                                        patient.pn, 
                                        patient.lname, 
                                        patient.fname,
                                        insurance.iname,
                                        TO_CHAR(insurance.from_date, 'MM-DD-YY') AS from_date,
                                        TO_CHAR(insurance.to_date, 'MM-DD-YY') AS to_date
                                    FROM patient
                                    JOIN insurance
                                    ON patient._id = insurance.patient_id
                                    ORDER BY insurance.from_date ASC, patient.lname;"""

patients_name_query = "SELECT fname, lname FROM patient;"
patient_cols_query = f"SELECT column_name FROM information_schema.columns WHERE table_name = 'patient';"
insurance_cols_query = f"SELECT column_name FROM information_schema.columns WHERE table_name = 'insurance';"


def get_records(query):
    
    query = query

    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()

	    # execute a statement
        cur.execute(query)

        # get all query results into a tuple
        records_tuple = cur.fetchall()

        print("Data from database fetched successfully")

        # close the communication with the PostgreSQL
        cur.close()

        return records_tuple

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def get_tables_col_names(records_tuple):
    records_tuple = records_tuple
    cols_list = [item for t in records_tuple for item in t]
    return cols_list


# takes data tuple from db query and transforms it to list
def transform_data(records_tuple):
    
    records_tuple = records_tuple
    #print(records_tuple)
    # convert records into list for further processing
    table = []
    for record in records_tuple:
        
        # add data to table list
        record_list = list(record)
        table.append(record_list)

    print(f'table from transform data def: {table}')
    return table

def print_records(headers, records_table):
    
    
    headers = headers
    records_table = records_table

    print(f'records table: {records_table}')
    print("Results from query")
    print("***********************")
    
    
    tt.print(records_table, header=headers)


'''
b) Create statistics about how many times (in count and in percentages with two decimal points from total) 
    each letter occurs in first and last names. This has to be considered as case insensitive and only 
    considering alphabetic characters. 
    Do not output letters, which do not occur in the strings.
    Output has to be sorted alphabetically ascending order.
    
    Example output for names “ John Smith“ and „John Doe“:
        D 1 6,25 %
        E 1 6,25 %
        H 3 18,75 %
        I 1 6,25 %
        J 2 12,5 %
        M 1 6,25 %
        N 2 12,5 %
        O 3 18,75 %
        S 1 6,25 %
        T 1 6,25 %
    NB! Separate each field of the row with tab character (like show in example above)
'''

def records_stats():

    record_tuple = get_records(patients_name_query)
    #print(record_tuple)
    flat_list = [item for t in record_tuple for item in t]
    print(f'flat_list: {flat_list}')
    char_list = []
    
    c = Counter()
    
    for name in flat_list:
        char_list += name.lower()
    
    c.update(char_list)

    
    print(f'char_list length: {len(char_list)}')

    def sort_tuple(my_tup):
        my_tup.sort(key = lambda x: x[0])
        return my_tup
    
    my_tup = c.most_common()
    #print(f'my_tup: {my_tup}')
    sorted_tup = sort_tuple(my_tup)
    print(f'sorted tuple: {sorted_tup}')

    total_char = len(char_list)
    stats_list = []
    for item in sorted_tup:
        stats_list.append([item[0], item[1], f"{(item[1]/total_char):.2%}"])

    print(f'stats_list: {stats_list}')



    
    


if __name__ == '__main__':
    test_connection()

    #transform_data_3_1(get_records(patients_insurance_records_query))

    # print(get_records(patients_insurance_records_query))
    # print("")
    # print(get_records(patient_cols_query))
    # print(get_records(insurance_cols_query))
    
    ''' print records for patient insurance data'''
    headers = ["Patient number", "Last name", "First name", "Insurance", "Valid from", "Valit until"]
    records_tuple = get_records(patients_insurance_records_query)
    records_table = transform_data(records_tuple)
    print_records(headers, records_table)

    ''' print records for char stats'''
    headers = ["Character", "Occurrence", "Prevalence"]
    stats_table = records_stats()
    print_records(headers, stats_table)

    