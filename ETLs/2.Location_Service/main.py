from incremental_api_call import *

# You can set small size_of_data_file below like: size_of_data_file = 10
#size_of_data_file = tab_data.iloc[0,0]
size_of_data_file = 50
#chunking_size can be set as 10,20,...100 keep it small

chunking_size = 10

# Call the mother function providing the above two args
sequential_api_call(size_of_data_file,chunking_size) 

# join api results to initial data set
merging_to_previous_data()
