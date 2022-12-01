# Raintree-Patient

2.2 Create the following tables:  

a) Table named **„patient“** with following column names and types:  
<pre>    **„_id“**, int with length of 10, unsigned, not null, auto increment,  
    **„pn“** varchar with field length of 11, default null;  
    **„first“** varcahr with field length of 15, default null;  
    **„last“** varchar with field length of 25, default null;  
    **„dob“** with type date, default null;  </pre>

b) Table named „insurance“ with following column names and types:  
<pre>    **„_id“**, int with length of 10, unsigned, not null, auto increment;  
    **„patient_id“** int with length of 10, unsigned, not null, foreign key referenced to patient table „_id“
    column;  
    **„iname“**, varchar with field length of 40, default null;  
    **„from_date“** with type date, default null;  
    **„to_date“** with type date, default null;  </pre>

2.3 Populate tables with sample data – at least 5 records for patient table and 2 insurance records for
each patient.

2.4 Solution file has to contain the table creation and data population MySQL queries