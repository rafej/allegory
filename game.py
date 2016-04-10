import math
import random

print "** Allegory **", "\n", "An adventure through the life of a young man", "\n", "Made by @rafej", "\n"
print "You woke up.", "\n"
print "Light billows through the blinds.", "\n", "Peering through the slits in long strands"
getUp = str(raw_input("Do you want to get out of bed?:(y/n) "))
if getUp == "y":
	print "You got up"
	print "Slowly but surely, your body aches out of bed"
	print "You drudge to your wardrobe."
	drobe1 = str(raw_input("Do you want to put on your school uniform? (y/n): "))
	if drobe1 == "n":
		print "You think about putting on some clothes but then you are like, hmm maybe no"
		stairs1 = str(raw_input("Do you want to go downstairs?(y/n): "))
		if stairs1 == "y":
			print "You walk downstairs in your pyjamasa"
			print "Clunk, clunk clunk"
			print "The sun billows through the windows in streams of light"
			eat2 = str(raw_input("Do you want to have breakfast?(y/n): "))
			if eat2 == "y":
				eat1 = str(raw_input("Do you want to eat cereal or toast? (c/t): "))
				if eat1 == "c":
					cereal1 = str(raw_input("Nutri-Grain or Weet Bix? (n/w): "))
					if cereal1 == "n":
						print "You get the Nutri-Grain out of the cupboard slowly"
						print "Eventually pouring milk into the bowl of cereal, you eat your breakfast tediously."

	if drobe1 == "y":
		print "You put on your school uniform slowly"
		
		door1 = str(raw_input("Do you want to have breakfast? (y/n: "))
		if door1 == "y":
			print "You walk downstairs"
			print "Clunk, clunk clunk"
			print "The sun billows through the windows in streams of light"
			eat1 = str(raw_input("Do you want to eat cereal or toast? (c/t): "))
			if eat1 == "c":
				cereal1 = str(raw_input("Nutri-Grain or Weet Bix? (n/w): "))
				if cereal1 == "n":
					print "You get the Nutri-Grain out of the cupboard slowly"
					print "Eventually pouring milk into the bowl of cereal, you eat your breakfast tediously."
					breakeat1 = str(raw_input("Start to eat? (y/n): "))
					if breakeat1 == "y":
						print "You slowly life your spoon and move it up to your mouth, slurping up your Nutri-Grain with delight and indigity"
							
	
if getUp == "n":
	print "You stayed in bed"
	phone1 = str(raw_input ("Do you want to look at your phone?(y/n): "))
	if phone1 == "y":
		print "3 Notifications", "\n"
		print "1. (Instagram)(26) some0ne liked your photo"
		print "2. (Messenger)(4) Bella messeged you"
		print "3. (Facebook) (2) You have a new friend request"
		phone2 = int(raw_input("Which notification do you want to look further into (Choose 1,2 or 3): "))
		if phone2 == 1:
			print "Open Instagram"
			print "Loading..."
			print "(<3) - 7 (Comments) - 2"
			print "some0ne liked your photo", "\n", "ihateplacemats liked your photo", "\n", "dogsrule17 liked your photo", "\n", "yoyoha liked your photo", "\n", "lemonlyman liked your photo", "\n", "stickagrin liked your photo", "\n", "hellofromtheotherside liked your photo"
			print "some0ne commented: Gotta love sunsets dickface", "\n", "yoyoha commented: Nice pic"  
			photo1 = str(raw_input("Do you want to reply? (y/n): "))
			

