#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  all_possibilities = []
  options = ['rock', 'paper', 'scissors']
  
  def round(played, num_of_rounds):
    for i in range(3):
      played.append(options[i])
      if num_of_rounds == n: 
        all_possibilities.append(played[:1])
      else:
        round(played, num_of_rounds + 1)
      played.pop()
  round([], 1)
  return all_possibilities

# var rockPaperScissors = function( numOfRounds ) {
#   var options = ['rock', 'paper', 'scissors'];
#   var allPossibilities = [];
  
#   var roundChoice = function(round, roundNumber) {
#     for(var i = 0; i < options.length; i++){
#       round.push(options[i]);
#       if(roundNumber === numOfRounds){
#         allPossibilities.push(round.slice());
#       }else{
#         roundChoice(round, roundNumber + 1);
#       }
#      }
#    }
#   roundChoice([], 1);
#   return allPossibilities;
# }

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')