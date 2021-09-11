from resources import Casting, Resource, Furnace, Dbf
from jobs import Job, DBF_JOB, CFF_JOB


#defining job
jobA = Job('A01', 5, 'RI-8011-4250-1585-600-', '6/4/21', CFF_JOB, 'A2','1050',1665)
jobB = Job('A02', 4, 'RI-8011-4250-1585-600-', '6/4/21', DBF_JOB, 'A3','1100',1515)
jobC = Job('A03', 4, 'RI-8011-4250-1585-600-', '6/4/21', DBF_JOB, 'A3','1600',1515)

# order matters here
casting_machine = Casting({jobA: 10, jobB: 100, jobC:60}, 300, 30, next_job=None)
dbf = Dbf({jobA: 5, jobB: 10, jobC: 40}, 20, 30, next_job=casting_machine)
cff = Resource({jobA: 15, jobB: 30, jobC: 60}, 30, next_job=casting_machine)
furnace = Furnace({jobA: 50, jobB: 50, jobC: 50}, 30, next_job=[cff, dbf])

furnace.add_job(jobA)
furnace.add_job(jobB)
furnace.add_job(jobC)

while not (furnace.is_resource_free() and casting_machine.is_resource_free() and dbf.is_resource_free() and cff.is_resource_free() ):
  # order matters here
  casting_machine.incr_time()
  dbf.incr_time()
  cff.incr_time()
  furnace.incr_time()

print(furnace.book_keeping_jobs)
print(dbf.book_keeping_jobs)
print(cff.book_keeping_jobs)
print(casting_machine.book_keeping_jobs)
