#!/usr/bin/python3
########################################################################
#                          Action Dino                                 #
########################################################################
# Description:                                                         #
# This program hacks a toy dinosaur. A button is pressed to make the   #
# dinosaur move and roar.                                              #
# This program is also a demonstration of controlling a motor using    #
# the gpiozero module.                                                 #
# This program is also an example of adding color to text displayed to #
# the screen.                                                          #
#                                                                      #
#                                                                      #
# Author: Paul Ryan                                                    #
#                                                                      #
########################################################################

########################################################################
#                          Import files                                #
########################################################################

from gpiozero import Motor, Button, OutputDevice
from time import sleep
from signal import pause
import pygame
import random
import os, sys

########################################################################
#                           Variables                                  #
########################################################################

t_rex_motor = Motor(23, 24, True)
t_rex_motor_enable = OutputDevice(25)
red_button = Button(2) 
green_button = Button(17) 

########################################################################
#                           Initialize                                 #
########################################################################

pygame.mixer.init()

########################################################################
#                            Functions                                 #
########################################################################
'''
The file_check function checks to see if the necessary files exist.
If they all exist, the program will continue.
If a file is missing, the program print a message and exit.
'''
def file_check():
	
	dinosaur_facts_flag = 0
	t_rex1_flag = 0
	t_rex2_flag = 0
	t_rex3_flag = 0
	t_rex4_flag = 0
	
	print("Checking for necessary files:")
	# Check to see if dinosaur_facts.txt file exists
	print("Looking for dinosaur_facts.txt...", end="")
	if os.path.isfile('Files/dinosaur_facts.txt'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		dinosaur_facts_flag = 1
	# Check to see if T_Rex1.wav file exists
	print("Looking for T_rex1.wav...", end="")
	if os.path.isfile('Sounds/T_rex1.wav'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		t_rex1_flag = 1	
	# Check to see if T_Rex2.wav file exists
	print("Looking for T_rex2.wav...", end="")
	if os.path.isfile('Sounds/T_rex2.wav'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		t_rex2_flag = 1
	# Check to see if T_Rex3.wav file exists
	print("Looking for T_rex3.wav...", end="")
	if os.path.isfile('Sounds/T_rex3.wav'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		t_rex3_flag = 1
	# Check to see if T_Rex4.wav file exists
	print("Looking for T_rex4.wav...", end="")
	if os.path.isfile('Sounds/T_rex4.wav'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		t_rex4_flag = 1
	# If there are no missing files, return to the main function
	# Otherwise print out messages and exit the program
	if dinosaur_facts_flag == 0  and t_rex1_flag == 0 and t_rex2_flag == 0 and t_rex3_flag == 0 and t_rex4_flag == 0:
		return
	else:
		if dinosaur_facts_flag == 1:
			print("\033[1;31;40mCheck to make sure that the dinosaur_facts.txt file exists in the 'Files' folder.")
		if t_rex1_flag == 1: 	
			print("\033[1;31;40mCheck to make sure that the T_rex1.wav file exists in the 'Sounds' folder.")
		if t_rex2_flag == 1:
			print("\033[1;31;40mCheck to make sure that the T_rex2.wav file exists in the 'Sounds' folder.") 
		if t_rex3_flag == 1:
			print("\033[1;31;40mCheck to make sure that the T_rex3.wav file exists in the 'Sounds' folder.")
		if t_rex4_flag == 1:
			print("\033[1;31;40mCheck to make sure that the T_rex4.wav file exists in the 'Sounds' folder.")
		print("\033[1;37;40mExiting program.\n")
		release_gpio_pins()
		exit()

'''
This function checks to see if the user has permission to read the
necessary files. If so, the program will continue. If not, messages are
printed out and the program will exit.
'''
def access_file_check():
	
	dinosaur_facts_flag = 0
	t_rex1_flag = 0
	t_rex2_flag = 0
	t_rex3_flag = 0
	t_rex4_flag = 0
	
	print("Checking to see if user has permission to read the necessary files:")
	# Check to see if user has read access to dinosaur_facts.txt
	print("Does user have read permissions for dinosaur_facts.txt?...", end="")
	if os.access('Files/dinosaur_facts.txt', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		dinosaur_facts_flag = 1
	# Check to see if user has read access to  T_Rex1.wav
	print("Does user have read permissions for T_rex1.wav?...", end="")
	if os.access('Sounds/T_rex1.wav', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		t_rex1_flag = 1
	# Check to see if user has read access to  T_Rex2.wav
	print("Does user have read permissions for T_rex2.wav?...", end="")
	if os.access('Sounds/T_rex2.wav', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		t_rex2_flag = 1
	# Check to see if user has read access to  T_Rex3.wav
	print("Does user have read permissions for T_rex3.wav?...", end="")
	if os.access('Sounds/T_rex3.wav', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		t_rex2_flag = 1
	# Check to see if user has read access to  T_Rex4.wav
	print("Does user have read permissions for T_rex4.wav?...", end="")
	if os.access('Sounds/T_rex4.wav', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		t_rex4_flag = 1
	
	if dinosaur_facts_flag == 0  and t_rex1_flag == 0 and t_rex2_flag == 0 and t_rex3_flag == 0 and t_rex4_flag == 0:
		return
	else:
		if dinosaur_facts_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Files' folder and the dinosaur_facts.txt file.")
		if t_rex1_flag == 1: 	
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'T_rex1.wav' file.")
		if t_rex2_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'T_rex2.wav' file.") 
		if t_rex3_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'T_rex3.wav' file.")
		if t_rex4_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'T_rex4.wav' file.")
		print("\033[1;37;40mExiting program.\n")
		release_gpio_pins()
		exit()
'''
The read_file function will read the dinosaur facts file and each 
line of the file will be an element in the fun_facts list. It will then
return the dino_facts list to the main function.
If the program is unable to read the file, it will display an error
message and then exit the program.
If the dino_facts file is empty, an error message will be displayed 
and the program will exit.
'''
def read_file(file_name):
	print("\033[1;37;40mReading the dinosaur_facts.txt file...", end="")
	f = open(file_name, "r")     # open the file as read-only
	dino_facts = f.readlines()
	f.close()
	print("\033[1;32;40mdone\033[1;37;40m!")

	return dino_facts
	
'''
This function checks to see if the file is empty.
'''
def empty_file_check(file_name):		
	print("\033[1;37;40mIs the dinosaur_facts.txt file empty?...", end="")
	if file_name == []:
		print("\033[1;31;40mYes\033[1;37;40m!")
		print("\033[1;31;40mThe dinosaur.txt file is empty. The program won't work.")
		release_gpio_pins()
		exit()
	else:
		print("\033[1;32;40mNo\033[1;37;40m!")
		
'''
This function will print out the program header to the screen.
'''
def print_header():
	print("\033[1;32;40m==========================================================================")
	print("\033[1;32;40m               _        _   _               ____  _                       ")
	print("\033[1;32;40m              / \   ___| |_(_) ___  _ __   |  _ \(_)_ __   ___            ")
	print("\033[1;32;40m             / _ \ / __| __| |/ _ \| '_ \  | | | | | '_ \ / _ \           ")
	print("\033[1;32;40m            / ___ \ (__| |_| | (_) | | | | | |_| | | | | | (_) |          ")
	print("\033[1;32;40m           /_/   \_\___|\__|_|\___/|_| |_| |____/|_|_| |_|\___/           ")
	print("\033[1;32;40m                                                                          ")
	print("\033[1;32;40m==========================================================================")
                                                      

'''
The get_roar function will randomly select one of the T. rex roar
files and return it and its file length to the main function.
'''

def get_roar():
	
	roar1 = "Sounds/T_rex1.wav"
	roar2 = "Sounds/T_rex2.wav"
	roar3 = "Sounds/T_rex3.wav"
	roar4 = "Sounds/T_rex4.wav"

	roar1_length = 6    # lenth of file in seconds
	roar2_length = 3    # lenth of file in seconds
	roar3_length = 4    # lenth of file in seconds
	roar4_length = 5    # lenth of file in seconds
	
	roars = [roar1, roar2, roar3, roar4]
	
	roar = random.choice(roars)   # Selects random sound file
	
	if roar == roar1:
		return roar, roar1_length
	elif roar == roar2:
		return roar, roar2_length
	elif roar == roar3:
		return roar, roar3_length
	else:
		return roar, roar4_length

'''
The activate_T_rex funciton takes 2 inputs: roar and roar_length. 
This function will play the sound file and then activate the motor for 
the duration of the sound file. 
'''

def activate_T_rex(roar, roar_length):
	try:
		t_rex_motor.value = 0.2       # Controls the motor speed
	except ValueError:
		print("\033[1;31;40mBad value specified for t_rex_motor. Enter a value between 0 and 1.\n")
		release_gpio_pins()
		exit()
	pygame.mixer.music.load(roar)     # Loads the sound file
	t_rex_motor_enable.on()           # Starts the motor
	pygame.mixer.music.play()         # Plays the sound file
	sleep(roar_length)                # Length of sound file in seconds
	t_rex_motor_enable.off()          # Stops the motor

'''
This function realeases the gpio pins.
'''
def release_gpio_pins():
	t_rex_motor.close()
	t_rex_motor_enable.close()
	red_button.close()
	green_button.close()
'''
This is the main fucntion. It will wait until one of two buttons is 
pressed. One button will start the program and the other button will
stop the program. Pressing Ctrl-C will also stop the program.
'''

def main():
	try:
		# Check to see that the necessary files exist
		file_check()
		# Check to see if files are accessible
		access_file_check()
		# Read the dinosaur_facts.txt file to populate the dino_facts list.
		dino_facts = read_file("Files/dinosaur_facts.txt")
		# Check to see if the file is empty
		empty_file_check(dino_facts)
		# Acknowledge that prelimiary checks are complete
		print("\033[1;37;40mPrelimiary checks are complete. Starting program...\n")
		# Display program header
		print_header()
		# Pre-load the first sound file
		roar, roar_length = get_roar()
		# Prompt the user to press a button
		print("\n\033[1;37;40mPush the \033[1;32;40mgreen button \033[1;37;40mto activate the \033[1;32;40mT. Rex\033[1;37;40m.")
		print("\033[1;37;40mPush the \033[1;31;40mred button \033[1;37;40mor press Ctrl-C to \033[1;31;40mstop \033[1;37;40mthe program.\n")
		
		while True:
			
			if green_button.is_pressed:
				# Print out a random dinosaur fun fact
				print("\033[1;34;40mDINOSAUR FUN FACT:")
				print(random.choice(dino_facts))
				# Move the T. rex for the duration of the sound file
				activate_T_rex(roar, roar_length)
				# Prompt the user again to press a button
				print("\033[1;37;40mPush the \033[1;32;40mgreen button \033[1;37;40mto activate the \033[1;32;40mT. Rex\033[1;37;40m.")
				print("\033[1;37;40mPush the \033[1;31;40mred button \033[1;37;40mor press Ctrl-C to \033[1;31;40mstop \033[1;37;40mthe program.\n")
				# Load the next sound file
				roar, roar_length = get_roar()
				
			if red_button.is_pressed:
				print("\nExiting program.\n")
				release_gpio_pins()
				exit()
				
	except KeyboardInterrupt:
		release_gpio_pins()
		print("\nExiting program.\n")
		
if __name__ == '__main__':
	main()