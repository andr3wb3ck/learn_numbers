import sequences
from essential import *
from res import *
diff_list = ((0,20),(21,100),(101,200))
revolver = denester(revolver,16,len(revolver)/16)
revolver_shot = denester(revolver_shot,16,len(revolver_shot)/16)
cowboy_alive = denester(cowboy_alive,16,len(cowboy_alive)/16)
cowboy_dead = denester(cowboy_dead,16,len(cowboy_dead)/16)
heart = denester(heart,2,len(heart)/2)
#x = int(input())-1
x = 2
print(sequences.lucky_numbers(diff_list[x]))
print(sequences.prime_numbers(diff_list[x]))
print(sequences.ulam_numbers(diff_list[x]))


draw(revolver,cowboy_alive,heart,5,5,134)
