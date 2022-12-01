# Raintree-Patient

2.2 Create the following tables:  

a) Table named **„patient“** with following column names and types:  
<pre>    **„_id“**, int with length of 10, unsigned, not null, auto increment,  
<pre>    **„pn“** varchar with field length of 11, default null;  
<pre>    **„first“** varcahr with field length of 15, default null;  
<pre>    **„last“** varchar with field length of 25, default null;  
<pre>    **„dob“** with type date, default null;  

b) Table named „insurance“ with following column names and types:  
<pre>    **„_id“**, int with length of 10, unsigned, not null, auto increment;  
<pre>    **„patient_id“** int with length of 10, unsigned, not null, foreign key referenced to patient table „_id“
<pre>    column;  
<pre>    **„iname“**, varchar with field length of 40, default null;  
<pre>    **„from_date“** with type date, default null;  
<pre>    **„to_date“** with type date, default null;  

2.3 Populate tables with sample data – at least 5 records for patient table and 2 insurance records for
each patient.

2.4 Solution file has to contain the table creation and data population MySQL queries