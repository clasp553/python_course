# Tetralith project

This project will allow me to quickly and more efficiently create and edit files to submit to the NSC Tetralith cluster.
I am currently running DFT calculations on the cluster, to optimize the structure of metal ions complexes which I am interested in studying experimentally.
The complexes consist in a metal center (mono or polinuclear) and short peptides surrounding it.

The project consists in three main steps:

	1) In order to run the simulation, I need a directory containing three files: 
			- an .sh file, which is the one that I actually run; it contains a "link" to the .inp file
			- an .inp file, in which I specify which kind of simulation I want to run; it contains a "link" to the .xyz file
			- an .xyz file, which is just a list of coordinates representing the geometrical structure of my starting molecule
		The format of the files is always the same, but now I am manually changing the characters providing the "links" between the files for each simulation that I run, a very time consuming process which often leads to typing mistakes etc.
		I would like to create a python package that allows me to efficiently create and edit these files.
		
	2) The ligands in my starting complexes are created manually using aminoacids as building blocks and linking them in different sequences with no particular pattern (in this initial stage of the project)
		I would like to create a program that lets me pick aminoacids and creates different sequences with them, in order to then test them in my simulations. 
		I will probably use Numpy and some statistical methods to reach this goal.
		
	3) The next step of the project (maybe to work on in the future) would be to create a package that is also able to quickly find, in the .out file which I obtain at the end of the simulation, the informations that I need to analyse the resulting optimized molecular geometries (es. Total energy, charge, oxidation state of the metal etc)
	
