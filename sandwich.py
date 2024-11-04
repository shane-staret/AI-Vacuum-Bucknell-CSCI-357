import ccm
from ccm.lib.actr import *

class SandwichBuilder(ACTR):
	goal = Buffer()
	sandwich = []

	def init():
		goal.set("build_sandwich 1 prep")

	def prep_ingredients(goal="build_sandwich 1 prep"):
		#start building our sandwich!
		goal.set("build_sandwich 2 bottom_bread")

	def place_bottom_bread(goal="build_sandwich 2 ?ingred"):
		#Place the bottom piece of bread
		sandwich.append(ingred)
		goal.set("build_sandwich 3 mayo")

	def place_mayo(goal="build_sandwich 3 ?ingred"):
		sandwich.append(ingred)
		goal.set("build_sandwich 4 turkey")

	def place_turkey(goal="build_sandwich 4 ?meat"):
		sandwich.append(meat)
		goal.set("build_sandwich 5 provolone")

	def place_cheese(goal="build_sandwich 5 ?cheese"):
		sandwich.append(cheese)
		goal.set("build_sandwich 6 mayo")

	def forgot_mayo(goal="build_sandwich 6 ?ingred"):
		goal.set("build_sanwich 6 mayo")

	def place_mayo_top(goal="build_sandwich 6 ?ingred"):
		sandwich.append(ingred)
		goal.set("build_sanwich 7 top_bread")

	def place_top_bread(goal="build_sandwich 7 ?ingred"):
		sandwich.append(ingred)
		self.stop


class EmptyEnvironment(ccm.Model):
	pass

myEnv = EmptyEnvironment()
agent_name = SandwichBuilder()
myEnv.agent = agent_name
ccm.log_everything(myEnv)
myEnv.run()
print("sandwich complete! sounds  gross")
