in 3 weeks: visit to IL cluster

~today: first task info

NERSC PDSF
* a "classical" cluster
* 18k jobs pending
* cluster security
	* can actually create account there, if you're from a group
* a "farm of computers" - each core has memory, disk space. no need to communicate.
* nodes
	* interactive (login, ~100 user sessions) - 16 cores, 125 gb memory, 200 gb scratch space
	* transfer nodes - just moving data - 10gb/s network
	* compute nodes
		* various processors, hardware due to upgrades being spaced in time		   * throw away old power inefficient nodes
			* TITAN 9MW includes a whole lot of cooling
	* file systems
		* tape!

* online monitoring
* buying computing time on cluster - responsibility of person running hardware

LHC prouction pass with ALIroot - 188y CPU time, 9y saving time

Xrootd - middleman, integrates any hardware and represents it outside as single file

ALICE LEGO trains: plug job into a specific setup, someone runs that centrally (on many nodes, more than you have permissions)
