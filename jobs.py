CFF_JOB = 0
DBF_JOB = 1

class Job:

  def __init__(self, batch_number, batch_size, batch_ri, batch_min_request_date,cff_or_dbf, cast_house, alloy, width_of_RI):
    self.batch_number = batch_number
    self.batch_size = batch_size
    self.batch_ri = batch_ri
    self.batch_min_request_date = batch_min_request_date
    self.cff_or_dbf = cff_or_dbf
    self.cast_house = cast_house
    self.alloy = alloy
    self.width_of_RI = width_of_RI

  def __hash__(self):
    return hash(self.batch_number)
	
  def __repr__(self):
    return self.batch_number