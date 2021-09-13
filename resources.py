import queue


class Resource:
    # this function will initiate all variables that will hold process times of jobs and times when the machine finishes processing the jobs
    def __init__(self, processing_times, postprocessing_time, next_job = None ):
        # processing_time = {"jobA": 10, "jobB": 100}
        self.processing_times = processing_times

        #postprocessing_time = 90
        self.postprocessing_time = postprocessing_time
        self.current_postprocessing_time = 0

        # assuming processing times are in minutes
        self.current_time = 0
        self.current_job = None
        self.current_job_minutes_remaining = 0
        self.machine_processing_time = 0
        
        # bookeeping is a dict {"jobA": [start_time, end_time]}
        self.book_keeping_jobs = {}

        self.job_queue = queue.Queue()
        self.next_job = next_job
        self.previous_job = None
    
    # This method will be overridden by dbf, casting machine to add further contstraints.
    def maybe_add_extra_processing_time(self):
      return
    
    
    def maybe_schedule_job_from_queue(self):
      if self.is_resource_free():
        if not self.job_queue.empty():
          job = self.job_queue.get()
          self.current_job = job
          self.current_job_minutes_remaining = self.processing_times[job]
          self.current_postprocessing_time = self.postprocessing_time
          self.maybe_add_extra_processing_time()
          self.book_keeping_jobs[job] = [self.current_time,self.current_time+self.current_job_minutes_remaining]

    #this function will add new jobs into machine and keep track of when the jobs were completed 
    def add_job(self, job):
        self.job_queue.put(job)
        self.maybe_schedule_job_from_queue()       
        
        
    #this function keeps track of time in simulation
    def incr_time(self):
        self.current_time += 1
        
        
        # If there is a job running
        if self.current_job is not None:
            self.current_job_minutes_remaining -= 1
            self.machine_processing_time += 1
        
            if self.current_job_minutes_remaining == 0:
                self.handle_completed_job()
       
        # If machine is free or machine is postprocessing.
        else:
          if self.current_postprocessing_time == 0:
            pass
          else:
            self.current_postprocessing_time -= 1
        
        self.maybe_schedule_job_from_queue()

    def handle_completed_job(self):
      completed_job = self.current_job
      self.current_job = None
      self.previous_job = completed_job
      if self.next_job is not None:
        self.next_job.add_job(completed_job)
          

    
    #this function will tell when the resource is free

    def is_resource_free(self):
      if self.current_job is not None:
        return False 
      else:
        if self.current_postprocessing_time != 0:
          return False
      return True


class Furnace(Resource):
  def __init__(self, processing_times, postprocessing_time, next_job ):
     super().__init__(processing_times, postprocessing_time, next_job=next_job )


  def handle_completed_job(self):
    completed_job = self.current_job
    self.current_job = None
    if self.next_job is not None:
      self.next_job[completed_job.cff_or_dbf].add_job(completed_job)

class Dbf(Resource):
  def __init__(self, processing_times, postprocessing_time, dbf_flushing_time, next_job ):
     super().__init__(processing_times, postprocessing_time, next_job=next_job )
     self.dbf_flushing_time = dbf_flushing_time

  def maybe_add_extra_processing_time(self):
    if self.previous_job is not None and self.previous_job.alloy != self.current_job.alloy:
      self.current_job_minutes_remaining += self.dbf_flushing_time
        


class Casting(Resource):
  def __init__(self, processing_times, postprocessing_time, mould_changeover_time, next_job ):
     super().__init__(processing_times, postprocessing_time, next_job=next_job )
     self.mould_changeover_time = mould_changeover_time

  def maybe_add_extra_processing_time(self):
    if self.previous_job is not None and self.previous_job.width_of_RI != self.current_job.width_of_RI:
      self.current_job_minutes_remaining += self.mould_changeover_time
