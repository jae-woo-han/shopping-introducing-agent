import dotenv

import hotdeal_crew
dotenv.load_dotenv()

from hotdeal_crew import HotdealAgent

result = HotdealAgent().crew().kickoff(inputs={"goods": "BW-100"})

print(result)