#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random

##################################################
#################### VOTES SETUP #################
##################################################

VOTES = 100000
MEDIAN = VOTES/2
CANDIDATES = {          
    "hermione": "Hermione Granger", 
    "balou": "Balou", 
    "chuck-norris": "Chuck Norris", 
    "elsa": "Elsa", 
    "gandalf": "Gandalf", 
    "beyonce": "Beyoncé"
    }

MENTIONS = [
    "A rejeter", 
    "Insuffisant", 
    "Passable", 
    "Assez Bien", 
    "Bien", 
    "Très bien", 
    "Excellent"
    ]

def create_votes():
    votes = []
    for n in range(0, VOTES):
        votes.append({
          "hermione": random.randint(3,6), 
          "balou": random.randint(0,6), 
          "chuck-norris": random.randint(0,2), 
          "elsa": random.randint(1,2), 
          "gandalf": random.randint(3,6), 
          "beyonce": random.randint(2,6)
          })
    return votes

##################################################
#################### FUNCTIONS ###################
##################################################



##################################################
#################### MAIN FUNCTION ###############
##################################################

def main():
    votes = create_votes()

if __name__ == '__main__':
    main()
