import pandas as pd 

class ProblemSetup:
    
    #the path of all files that need to be used using sql connect. Decide all the input files you will need
    #master_data_file
    #batch processing files Omkar created 
    #Processing times of batches file 
    #file for identifying the alloy changeovers 
    #DBF and CFF input files 
    def _init_(self, file_path):
      self.master_data_file = pd.read_csv(file_path)
    
    
    #infeasible set = set of all infeasible alloy pairs
    def get_infeasible_alloy_pairs(self):
      pass

    #get random batches. Select the unique batches and create n lists of random batches 
    #input - n (the number of random lists you want to create)
    def get_random_batches(self, n):
      pass
    
    #YOU CAN LEAVE THIS FOR NOW 
    #feasible batches selection 
    def feasible_batches(self):
      pass
    
    # processing_times = { "furnace": {"jobA": 10, "jobB": 100}, "casting_machine": {"jobA": 100, "jobB": 200}}
    def get_processing_times(self):
      pass

    # postprocessing_time = 90 mins 
    def get_postprocessing_times(self):
      pass

    
    #-------------------------the below inputs are from batches or templates we have created-------------------------------#
    #this function should return a dictionary like {'batch_number' : [batch_size, batch_ri, batch_min_request_date,cff_or_dbf,cast_house}
    #see definition of job class below for more information 

    def get_batch_inputs(self):
      pass
    
