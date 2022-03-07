import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import NEXUS, PROBE, PYLON, ASSIMILATOR


class StarcraftBoi(sc2.BotAI):
    async def on_step(self, iteration):
        # what to do every step
        await self.build_workers()
        await self.distribute_workers()  # in sc2/bot_ai.py
        await self.expand()
        await self.build_assimilators()
        await self.offensive_force_buildings()
        
    async def build_workers(self):
        for nexus in self.units(NEXUS).ready.noqueue:
            if self.can_afford(PROBE):
                await self.do(nexus.train(PROBE))
                await build_pylon()

    async def build_pylon(self):
        if self.supply_left < 5 and not self.already_pending(PYLON):
                nexuses = self.units(NEXUS).ready
                if nexuses.exists:
                    if self.can_afford(PYLON):
                        await self.build(PYLON, near=nexuses.first)
      
    async def expand(self):
        if self.units(NEXUS).amount < 2 and self.can_afford(NEXUS):
            await self.expand_now()
    async def build_assimilators(self):
        for nexus in self.units(NEXUS).ready:
            geysers = self.state.vespene_geyser.closer_than(25.0, nexus)
            print(geysers)
            if not self.can_afford(ASSIMILATOR):
                    break
            

run_game(maps.get("AbyssalReefLE"), [
    Bot(Race.Protoss, StarcraftBoi()),
    Computer(Race.Terran, Difficulty.Easy)
], realtime=True)