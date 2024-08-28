DROP PROCEDURE IF EXISTS Migration_to_cetral_db;

CREATE OR REPLACE PROCEDURE Migration_to_cetral_db(source_schema_name TEXT, dest_schema_name TEXT, source_table_name TEXT, dest_table_name TEXT, source_key_col TEXT, dest_key_col TEXT)
LANGUAGE plpgsql
AS $$
DECLARE
    max_row_count INT;
    sql_query_1 TEXT;
    sql_query_2 TEXT;
    source_total_row INT;
	total INT;
BEGIN
    -- Construct the dynamic SQL query to get the maximum value from the key column
    sql_query_1 := format('SELECT MAX(%I) FROM %I.%I', dest_key_col, dest_schema_name, dest_table_name);
    sql_query_2 := format('SELECT COUNT(%I) FROM %I.%I', source_key_col, source_schema_name, source_table_name);
    
    -- Execute the dynamic SQL query and store the result into max_row_count
    EXECUTE sql_query_1 INTO max_row_count;
    EXECUTE sql_query_2 INTO source_total_row;
    
    -- Print the max_row_count
    RAISE NOTICE 'Maximum row at destination % is: %', dest_key_col, max_row_count;
    RAISE NOTICE 'Total rows from source % is: %', source_key_col, source_total_row;
	total := max_row_count + source_total_row;
	RAISE NOTICE 'Expected row count : %',total;

END;
$$;

-- Call the procedure

CALL Migration_to_cetral_db('cdm_aphrc_covid', 'demo_cdm','person','person', 'person_id','person_id');