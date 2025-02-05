-- goal is to implement a condition. area >= 3mil or population >= 25mil

select name, population, area
from World
where area >= 3000000 or population >= 25000000