## Description
Example data for the database for the [Bookshelf](https://github.com/willy-it-wonka/Bookshelf-backend) application to test it. Prepared for localhost and AWS RDS (Amazon Relational Database Service) and all other hosting.
</br></br>

## Practical tips
- On localhost, all you need to do is import JSON files into the tables. For RDS, you need to use SQL scripts.
- On localhost you may fail to import the `book_categories.json` due to the lack of a primary key column, then use SQL script.
- Notice the comment in the `notes.py` file. Follow it depending on whether you use `notes.json` for import or in SQL script.
- If you want to use this data for more users, use Python scripts to automatically modify the JSON files.\
  Just change the values of the variables at the beginning of the scripts.
</br></br>

## Change RDS settings
To connect to your database in Amazon Relational Database Service, for example through MySQL Workbench, you need to log in to your AWS account and change RDS settings.
1. RDS → Databases → identifier-of-your-database\
   In the „Connectivity & security” section, in „Security”, in „VPC security groups”, select active group.\
   In the „Security group ID” column, select active group.\
   In the „Inbound rules” section, select „Edit inbound rules”, add new rule: type – Custom TCP, source – Anywhere-IPv4. Save changes.
2. RDS → Databases → identifier-of-your-database\
   Select „Modify”.\
   In the „Connectivity” section, expand „Additional configuration”.\
   Check „Publicly accessible" and confirm.\
   **Warning:** when you have finished working with the database, undo the above changes (paragraph 2). Even on the Free Tier, public access to the database is paid.
