# from rest_app.dal import githubreo_sqlalchemy
# Program entry point
from sqlalchemy_sqlite import githubreo_sqlalchemy


def main():
    dbms = githubreo_sqlalchemy.MyDatabase(githubreo_sqlalchemy.SQLITE, dbname='mydb.sqlite')
    # Create Tables
    dbms.create_db_tables()
    # dbms.insert_single_data()
    dbms.print_all_data(githubreo_sqlalchemy.USERS)
    dbms.print_all_data(githubreo_sqlalchemy.ADDRESSES)
    # dbms.sample_query() # simple query
    # dbms.sample_delete() # delete data
    # dbms.sample_insert() # insert data
    # dbms.sample_update() # update data
# run the program
if __name__ == "__main__": main()