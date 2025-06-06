*** Settings ***
Library  DatabaseLibrary
Library  OperatingSystem

Suite Setup     Connect To Database     ${dbType}      ${dbName}       ${uername}      ${password}     ${host}     ${port}
Suite Teardown  Disconnect From Database


*** Variables ***
${dbName}      testdb
${uername}     root
${password}    Ama@123
${host}        localhost
${port}        3306
${dbType}      pymysql


*** Test Cases ***
Create Person Table
   ${output}=   Execute SQL String      create table person(id int,name varchar(20),mobile varchar(10))
   log to console   ${output}
   Should Be Equal As Strings  ${output}   None

Inserting Data In Person Table
   # Single Record
   ${output}=   Execute SQL String      insert into person values(101,'Abhay','9158565478')
   log to console   ${output}
   Should Be Equal As Strings  ${output}   None

   # Multiple record
   ${output}=   Execute SQL Script     ./test_data/db.sql
   log to console   ${output}
   Should Be Equal As Strings  ${output}   None

Validating Name Present
   Check Row Count     select id,mobile from person where name = 'Viky'    ==    1

Validating Name Not
   Check Row Count     select mobile from person where name = 'dfds'    ==    0

Check Person Table Exists
    Table Must Exist    person

Verfiy Row Count Is Zero
    Row Count     select id from person where name='sdf'

Verfiy Row Count Is Equal to Some Value
    Row Count     select id from person where name='Rahul Moundekar'    1

Update Record
    ${output}=   Execute SQL String      update person set name='Rahul Moundekar' where id=101
    log to console   ${output}
    Should Be Equal As Strings  ${output}   None

Select All Record from Table
    ${data}=   Query      select * from person
    FOR    ${person}  IN    ${data}
        log to console   ${person}
    END

Delete Record From Table
    ${output}=   Execute SQL String     delete from person where id=105
    log to console   ${output}
    Should Be Equal As Strings  ${output}   None