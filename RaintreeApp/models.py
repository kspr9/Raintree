from django.db import models

# Create your models here.


'''
Table named „patient“ with following column names and types:
    „_id“, int with length of 10, unsigned, not null, auto increment,
    „pn“ varchar with field length of 11, default null;
    „first“ varcahr with field length of 15, default null;
    „last“ varchar with field length of 25, default null;
    „dob“ with type date, default null;
'''

'''
Table named „insurance“ with following column names and types:
    „_id“, int with length of 10, unsigned, not null, auto increment;
    „patient_id“ int with length of 10, unsigned, not null, foreign key referenced to patient table „_id“
    column;
    „iname“, varchar with field length of 40, default null;
    „from_date“ with type date, default null;
    „to_date“ with type date, default null;

'''

# Solution file has to contain the table creation and data population MySQL queries