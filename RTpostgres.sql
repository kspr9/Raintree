
'''
Table named „patient“ with following column names and types:
    „_id“, int with length of 10, unsigned, not null, auto increment,
    „pn“ varchar with field length of 11, default null;
    „first“ varcahr with field length of 15, default null;
    „last“ varchar with field length of 25, default null;
    „dob“ with type date, default null;
'''


CREATE TABLE patient(
    _id int GENERATED ALWAYS AS IDENTITY
    (START WITH 1010000000 INCREMENT BY 1),
    pn varchar(11) DEFAULT null,
    fname varchar(15) DEFAULT null,
    lname varchar(25) DEFAULT null,
    dob date DEFAULT null,
    PRIMARY KEY(_id)
);

INSERT INTO patient VALUES(DEFAULT, '12345678915', 'Meeli', 'Moos', '2022-06-03');
INSERT INTO patient VALUES(DEFAULT, '12345678914', 'Koit', 'Kelder', '2020-03-17');
INSERT INTO patient VALUES(DEFAULT, '12345678913', 'Laine', 'Hari', '2017-05-21');
INSERT INTO patient VALUES(DEFAULT, '12345678912', 'Eha', 'Viik', '1991-09-30');
INSERT INTO patient VALUES(DEFAULT, '12345678911', 'Voldemar', 'Viik', '1986-09-30');

'''
Table named „insurance“ with following column names and types:
    „_id“, int with length of 10, unsigned, not null, auto increment;
    „patient_id“ int with length of 10, unsigned, not null, foreign key referenced to patient table „_id“
    column;
    „iname“, varchar with field length of 40, default null;
    „from_date“ with type date, default null;
    „to_date“ with type date, default null;

'''

CREATE TABLE insurance(
    _id int GENERATED ALWAYS AS IDENTITY
    (START WITH 2020000000 INCREMENT BY 1),
    patient_id int,
    iname varchar(40) DEFAULT null,
    from_date date DEFAULT null,
    to_date date DEFAULT null,
    CONSTRAINT fk_patient
        FOREIGN KEY(patient_id)
            REFERENCES patient(_id)
            ON DELETE CASCADE
);



INSERT INTO insurance VALUES(DEFAULT, '1010000000', 'Medicare', '2022-06-03', '2022-12-30');
INSERT INTO insurance VALUES(DEFAULT, '1010000000', 'Blue Cross', '2022-06-03', '2029-06-03');
INSERT INTO insurance VALUES(DEFAULT, '1010000001', 'Medicaid', '2020-03-19', '2022-12-30');
INSERT INTO insurance VALUES(DEFAULT, '1010000001', 'Blue Shield', '2020-06-30', '2021-12-30');
INSERT INTO insurance VALUES(DEFAULT, '1010000002', 'Medicare', '2017-05-25');
INSERT INTO insurance VALUES(DEFAULT, '1010000002', 'Blue Cross', '2019-02-14', '2022-12-30');
INSERT INTO insurance VALUES(DEFAULT, '1010000003', 'Medicare', '1997-09-30', '2000-12-30');
INSERT INTO insurance VALUES(DEFAULT, '1010000003', 'Medicaid', '2022-06-03', '2025-12-30');
INSERT INTO insurance VALUES(DEFAULT, '1010000004', 'Blue Shield', '2009-03-15', '2021-12-30');
INSERT INTO insurance VALUES(DEFAULT, '1010000004', 'Medicare', '1995-01-01');

'''
 Solution file has to contain the table creation and data population MySQL queries
 insurances = 'Blue Cross', 'Medicare', 'Blue Shield', 'Medicaid'
'''


select 
    patient.pn, 
    patient.lname, 
    patient.fname,
    insurance.iname,
    to_char(insurance.from_date, 'MM-DD-YY') as from_date,
    to_char(insurance.to_date, 'MM-DD-YY')
from patient
join insurance
on patient._id = insurance.patient_id;